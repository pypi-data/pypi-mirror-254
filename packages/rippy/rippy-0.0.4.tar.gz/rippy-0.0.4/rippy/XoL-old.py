import numpy as np
from .FreqSevSims import FreqSevSims
import numba as nb


@nb.jit(nopython=True, cache=True)
def _cumulate_within(index: np.ndarray, values: np.ndarray):
    result = values.copy()
    for i in range(1, len(index)):
        if index[i] == index[i - 1]:
            result[i] = result[i - 1] + values[i]
    return result


@nb.jit(nopython=True, cache=True)
def _diff_within(index: np.ndarray, values: np.ndarray):
    result = values.copy()
    for i in range(1, len(index)):
        if index[i] == index[i - 1]:
            result[i] = values[i] - values[i - 1]
        else:
            result[i] = values[i]
    return result


class ContractResults:
    def __init__(self, recoveries: FreqSevSims, reinstatement_premium: FreqSevSims):
        self.recoveries = recoveries
        self.reinstatement_premium = reinstatement_premium


class XoL:
    def __init__(
        self,
        name: str,
        limit: float,
        excess: float,
        premium: float,
        reinstatement_premium_rate: list[tuple[int, float]] | None = None,
        aggregate_limit: float = None,
        aggregate_deductible: float = None,
        franchise: float = None,
        reverse_franchise: float = None,
    ):
        self.name = name
        self.limit = limit
        self.excess = excess
        self.aggregate_limit = aggregate_limit
        self.premium = premium
        self.aggregate_deductible = aggregate_deductible
        self.franchise = franchise
        self.reverse_franchise = reverse_franchise
        self.summary = None
        self.num_reinstatements = (
            aggregate_limit / limit - 1 if aggregate_limit is not None else None
        )
        self.reinstatement_premium_rate = (
            np.array([r for n, r in reinstatement_premium_rate]) / 100
            if reinstatement_premium_rate is not None
            else None
        )
        self.reinstatement_premium_number = (
            np.array([n for n, r in reinstatement_premium_rate]).cumsum()
            if reinstatement_premium_rate is not None
            else None
        )

    def apply(self, claims: FreqSevSims) -> ContractResults:
        """Apply the XoL contract to a set of claims"""
        # apply franchise
        if self.franchise is not None or self.reverse_franchise is not None:
            claims = np.maximum(claims - self.franchise, 0)
            claims = np.minimum(claims, self.reverse_franchise)
        individual_recoveries_pre_aggregate = np.minimum(
            np.maximum(claims - self.excess, 0), self.limit
        )
        if self.aggregate_limit is None and self.aggregate_deductible is None:
            return individual_recoveries_pre_aggregate
        aggregate_limit = (
            self.aggregate_limit if self.aggregate_limit is not None else np.inf
        )
        aggregate_deductible = (
            self.aggregate_deductible if self.aggregate_deductible is not None else 0
        )
        temp = _cumulate_within(
            claims.sim_index, individual_recoveries_pre_aggregate.values
        )
        cumulative_recoveries_pre_aggregate = FreqSevSims(
            claims.sim_index, temp, claims.n_sims
        )
        cumulative_recoveries = np.minimum(
            np.maximum(cumulative_recoveries_pre_aggregate - aggregate_deductible, 0),
            aggregate_limit,
        )
        recoveries = _diff_within(
            cumulative_recoveries.sim_index, cumulative_recoveries.values
        )
        losses = FreqSevSims(claims.sim_index, recoveries, claims.n_sims)
        results = ContractResults(losses, None)
        if self.reinstatement_premium_rate is not None:

            limits_used = cumulative_recoveries / self.limit
            cumulative_reinstatements_used = np.minimum(
                limits_used, self.num_reinstatements
            )
            cumulative_reinstatements_used_full = np.floor(
                cumulative_reinstatements_used
            )
            cumulative_reinstatements_used_fraction = (
                cumulative_reinstatements_used - cumulative_reinstatements_used_full
            )
            cumulative_reinstatement_premium_proportion = (
                self.reinstatement_premium_rate[
                    self.reinstatement_premium_number.searchsorted(
                        cumulative_reinstatements_used_full.values, side="left"
                    )
                ]
                * cumulative_reinstatements_used_full
                + self.reinstatement_premium_rate[
                    self.reinstatement_premium_number.searchsorted(
                        cumulative_reinstatements_used.values, side="left"
                    )
                ]
                * cumulative_reinstatements_used_fraction
            )
            reinstatement_premium_proportion = _diff_within(
                cumulative_recoveries.sim_index,
                cumulative_reinstatement_premium_proportion.values,
            )

            reinstatement_premium = FreqSevSims(
                claims.sim_index,
                reinstatement_premium_proportion * self.premium,
                claims.n_sims,
            )
            results.reinstatement_premium = reinstatement_premium

        self.calc_summary(losses)
        return results

    def calc_summary(self, losses):
        aggregate_recoveries = losses.aggregate()
        self.summary = {
            "mean": aggregate_recoveries.mean(),
            "std": aggregate_recoveries.std(),
            "prob_attach": np.sum((aggregate_recoveries > 0))
            / len(aggregate_recoveries),
            "prob_vert_exhaust": np.sum((losses.values >= self.limit))
            / len(losses.values),
            "prob_horizonal_exhaust": (
                np.sum((aggregate_recoveries >= self.aggregate_limit))
                / len(aggregate_recoveries)
                if self.aggregate_limit is not None
                else 0
            ),
        }

    def print_summary(self):
        """Print a summary of the losses to the layer"""
        print("Layer Name : {}".format(self.name))
        print("Mean Recoveries: ", self.summary["mean"])
        print("SD Recoveries: ", self.summary["std"])
        print("Probability of Attachment: ", self.summary["prob_attach"]),

        print(
            "Probability of Vertical Exhaustion: ", self.summary["prob_vert_exhaust"]
        ),
        print(
            "Probability of Horizontal Exhaustion: ",
            self.summary["prob_horizonal_exhaust"],
        ),
        print("\n")


class XoLTower:
    def __init__(
        self,
        limit: list,
        excess: list,
        premium: float,
        reinstatement_premium_rate: list[list[tuple[float, float]] | None] = None,
        aggregate_deductible: float = None,
        aggregate_limit: float = None,
        franchise: float = None,
        reverse_franchise: float = None,
    ):
        self.limit = limit
        self.excess = excess
        self.aggregate_limit = aggregate_limit
        self.aggregate_deductible = aggregate_deductible
        self.franchise = franchise
        self.reverse_franchise = reverse_franchise
        self.n_layers = len(limit)
        self.layers = [
            XoL(
                "Layer {}".format(i + 1),
                limit[i],
                excess[i],
                premium[i],
                reinstatement_premium_rate[i],
                aggregate_limit[i] if aggregate_limit is not None else None,
                aggregate_deductible[i] if aggregate_deductible is not None else None,
                franchise[i] if franchise is not None else None,
                reverse_franchise[i] if reverse_franchise is not None else None,
            )
            for i in range(self.n_layers)
        ]

    def apply(self, claims: FreqSevSims) -> FreqSevSims:
        """Apply the XoL contract to a set of claims"""
        recoveries = claims.copy() * 0
        for layer in self.layers:
            recoveries += layer.apply(claims).recoveries

        return recoveries

    def summary(self):
        """Print a summary of the losses to the layer"""
