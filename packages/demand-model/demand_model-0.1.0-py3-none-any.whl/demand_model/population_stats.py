from datetime import date
from functools import lru_cache
from typing import Any, Optional
import pandas as pd


class PopulationStats:
    def __init__(self, df: pd.DataFrame, external_bin_identifier: Optional[Any] = None):
        """
        Initialize the PopulationStats object with:
        - df: the dataframe containing the population data. Each row is the activity of a population member that relates the following columns:
            - start_bin: the bin the member belongs to
            - end_bin: the bin the member belongs to at the end of the period (the one the member transitions to)
            - start_date: the date a member joins the "start_bin"
            - end_date: the date a member leaves the "start_bin" and joins the "end_bin"
        - external_bin_identifier: the identifier of the bin representing the daily entrants - if left empty, the daily entrants will not be possible to calculate.
        """
        assert "start_bin" in df.columns
        assert "end_bin" in df.columns
        assert "start_date" in df.columns
        assert "end_date" in df.columns

        self.__df = df
        self.__external_bin_identifier = external_bin_identifier

    @property
    def df(self):
        return self.__df

    @property
    def external_bin_identifier(self):
        return self.__external_bin_identifier

    @property
    def stock(self):
        """
        Calculates the daily transitions for each bin by
        finding all the transitions, summing to get total populations for each
        day and then resampling to get the daily populations.
        """

        df = self.df.copy()
        endings = df.groupby(["end_date", "start_bin"]).size()
        endings.name = "nof_endings"

        beginnings = df.groupby(["start_date", "start_bin"]).size()
        beginnings.name = "nof_beginnings"

        endings.index.names = ["date", "start_bin"]
        beginnings.index.names = ["date", "start_bin"]

        pops = pd.merge(
            left=beginnings,
            right=endings,
            left_index=True,
            right_index=True,
            how="outer",
        )

        pops = pops.fillna(0).sort_values("date")

        pops = (pops["nof_beginnings"] - pops["nof_endings"]).groupby(["start_bin"]).cumsum()

        pops = pops.unstack(level=1)

        # Resample to daily counts and forward-fill in missing days
        pops = pops.resample("D").first().fillna(method="ffill").fillna(0)

        return pops

    @lru_cache(maxsize=5)
    def stock_at(self, start_date):
        """
        truncates the stock dataframe to the date closest to the provided start_date.
        """
        start_date = pd.to_datetime(start_date)

        index = self.stock.index.get_indexer([start_date], method="nearest")

        stock = self.stock.iloc[index[0]].T
        stock.name = start_date
        return stock

    @property
    def transitions(self):
        """
        Calculates the daily transitions for each bin.
        """
        transitions = self.df.copy()

        transitions = transitions.groupby(["start_bin", "end_bin", "end_date"]).size()
        transitions = (
            transitions.unstack(level=["start_bin", "end_bin"])
            .fillna(0)
            .asfreq("D", fill_value=0)
        )

        return transitions

    @lru_cache(maxsize=5)
    def raw_transition_rates(self, start_date: date, end_date: date):
        """
        Calculates the transition rates for each bin.
        """

        # Ensure we can calculate the transition rates by aligning the dataframes
        stock = self.stock.truncate(before=start_date, after=end_date)
        stock.columns.name = "start_bin"
        transitions = self.transitions.truncate(before=start_date, after=end_date)

        # Calculate the transition rates
        stock, transitions = stock.align(transitions)
        transition_rates = transitions / stock.shift(1).fillna(method="bfill")
        transition_rates = transition_rates.fillna(0)

        # Use the mean rates
        transition_rates = transition_rates.mean(axis=0)
        transition_rates.name = "transition_rate"

        return transition_rates


    def to_excel(self, output_file: str, start_date: date, end_date: date):
        with pd.ExcelWriter(output_file) as writer:
            self.stock_at(end_date).to_excel(writer, sheet_name="population")
            self.raw_transition_rates(start_date, end_date).to_excel(
                writer, sheet_name="transition_rates"
            )
            self.daily_entrants(start_date, end_date).to_excel(
                writer, sheet_name="daily_entrants"
            )
