from typing import Any, Optional

import numpy as np
import pandas as pd


def combine_rates(rate1: pd.Series, rate2: pd.Series) -> pd.Series:
    rate1, rate2 = rate1.align(rate2, fill_value=0)
    rates = rate1 + rate2
    rates.index.names = ["from", "to"]
    return rates


def calculate_transfers_out(
    initial_population: pd.Series, transition_rates: pd.Series
) -> pd.DataFrame:
    """
    Calculate the population count that will be transferred out of each state
    """
    # We start with the full population
    df_out = pd.DataFrame(initial_population)
    df_out.columns = ["initial"]
    df_out.index.names = ["from"]

    # Make sure we don't drop levels
    summed_rates = transition_rates.groupby(level=0).sum()
    df_out, summed_rates = df_out.align(summed_rates, axis=0, fill_value=0)

    # Add the transition 'out' rates (so summed for the particular level)
    df_out["out_rate"] = summed_rates

    # Calculate the number of people that will be transferred out
    df_out["transfer_out"] = df_out.initial * df_out.out_rate

    # If at any point the transfers out exceed the population, we set the transfers out to the population
    df_out.loc[df_out.transfer_out > df_out.initial, "transfer_out"] = df_out.initial
    df_out.loc[df_out.transfer_out < 0, "transfer_out"] = 0

    # Fill any NaNs with 0
    df_out = df_out.fillna(0)
    return df_out


def calculate_transfers_in(
    transfers_out: pd.DataFrame,
    transition_rates: pd.Series,
    external_bin_identifier: Optional[Any] = None,
) -> pd.DataFrame:
    """
    Calculate the population count that will be transferred in to each state
    """

    # We start with all of the transitions
    df_in = pd.DataFrame(transition_rates)
    df_in.columns = ["transition_rates"]
    df_in.index.names = ["from", "to"]
    df_in.reset_index(level=1, inplace=True)

    # Make sure we don't drop levels
    df_in, transfers_out = df_in.align(transfers_out)

    # Add rates for the from groups
    df_in["group_rates"] = transfers_out.out_rate

    # Calculate fraction for each individual transition
    df_in["fraction"] = df_in.transition_rates / df_in.group_rates

    # Now insert the numbers that have been transferred out
    df_in["out"] = transfers_out.transfer_out

    # And calculate the transfer in numbers
    df_in["transfer_in"] = df_in.fraction * df_in.out

    # For transfers in, we always assume a ratio of 1 days
    if not pd.isna(external_bin_identifier):
        df_in["transfer_in"] = np.where(
            df_in.index == external_bin_identifier, df_in.transition_rates, df_in.transfer_in
        )

    df_in.set_index(["to"], append=True, inplace=True)

    return df_in


def calculate_rate_from_numbers(
    initial_population: pd.Series,
    transition_numbers: pd.Series,
    external_bin_identifier: Optional[Any] = None,
) -> pd.Series:
    df_num = pd.DataFrame(transition_numbers)
    df_num.columns = ["transition_numbers"]
    df_num.index.names = ["from", "to"]
    df_num.reset_index(level=1, inplace=True)
    df_num["population"] = initial_population

    # For transfers in, we always assume a population of 1
    if not pd.isna(external_bin_identifier):
        df_num.loc[
            df_num.index.get_level_values(0) == external_bin_identifier, "population"
        ] = 1
    df_num["rate"] = df_num.transition_numbers / df_num.population

    df_num.set_index(["to"], append=True, inplace=True)

    return df_num.rate


def transition_population(
    initial_population: pd.Series,
    transition_rates: pd.Series = None,
    transition_numbers: pd.Series = None,
    days: int = 1,
    external_bin_identifier: Optional[Any] = None,
) -> pd.Series:
    assert days > 0, "Days must be greater than 0"

    if transition_rates is None and transition_numbers is None:
        return initial_population.copy()

    if days > 1:
        if transition_rates is not None:
            transition_rates = 1 - (1 - transition_rates) ** days
        if transition_numbers is not None:
            transition_numbers = transition_numbers * days

    if transition_numbers is not None:
        # Calculate transition rates from transition numbers
        transition_numbers = calculate_rate_from_numbers(
            initial_population, transition_numbers, external_bin_identifier
        )

    if transition_numbers is not None and transition_rates is not None:
        # Combine rates
        transition_rates = combine_rates(transition_numbers, transition_rates)
    elif transition_numbers is not None:
        transition_rates = transition_numbers

    df_out = calculate_transfers_out(initial_population, transition_rates)
    df_in = calculate_transfers_in(df_out, transition_rates, external_bin_identifier)

    initial_population = initial_population.reindex(df_out.index, fill_value=0)
    transfer_in = (
        df_in.transfer_in.groupby(level=["to"])
        .sum()
        .reindex(initial_population.index, fill_value=0)
    )

    to_transfer = initial_population - df_out.transfer_out + transfer_in

    # Make sure we get rid of any that are not in care
    if not pd.isna(external_bin_identifier) and external_bin_identifier in to_transfer.index:
        del to_transfer[external_bin_identifier]

    return to_transfer
