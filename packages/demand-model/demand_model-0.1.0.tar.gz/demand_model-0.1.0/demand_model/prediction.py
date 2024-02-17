from datetime import date, timedelta
from typing import Any, Optional, Union, Iterable

import pandas as pd

from demand_model.transition import transition_population, combine_rates
from demand_model.population_stats import PopulationStats

try:
    import tqdm
except ImportError:
    tqdm = None


class ModelPredictor:
    def __init__(
        self,
        population: pd.Series,
        transition_rates: Optional[pd.Series] = None,
        transition_numbers: Optional[pd.Series] = None,
        start_date: date = date.today(),
        external_bin_identifier: Optional[Any] = None,
    ):
        self.__initial_population = population
        self.__transition_rates = transition_rates
        self.__transition_numbers = transition_numbers
        self.__start_date = start_date
        self.__external_bin_identifier = external_bin_identifier

    @property
    def transition_rates(self):
        return self.__transition_rates.copy()

    @property
    def transition_numbers(self):
        return self.__transition_numbers.copy()

    @property
    def initial_population(self):
        return self.__initial_population

    @property
    def date(self):
        return self.__start_date

    @property
    def external_bin_identifier(self):
        return self.__external_bin_identifier

    def next(self, step_days: int = 1):
        next_population = transition_population(
            self.initial_population,
            self.__transition_rates,
            self.__transition_numbers,
            days=step_days,
            external_bin_identifier=self.external_bin_identifier,
        )

        next_date = self.date + timedelta(days=step_days)
        next_population.name = next_date

        return ModelPredictor(
            next_population,
            self.__transition_rates,
            self.__transition_numbers,
            next_date,
            self.external_bin_identifier,
        )

    def predict(self, steps: int = 1, step_days: int = 1, progress=False):
        predictor = self

        if progress and tqdm:
            iterator = tqdm.trange(steps)
            set_description = iterator.set_description
        else:
            iterator = range(steps)
            set_description = lambda x: None

        predictions = []
        for i in iterator:
            predictor = predictor.next(step_days=step_days)

            pop = predictor.initial_population
            pop.name = self.__start_date + timedelta(days=(i + 1) * step_days)
            predictions.append(pop)

            set_description(f"{pop.name:%Y-%m}")

        return pd.concat(predictions, axis=1).T


def build_prediction_model(
    df: pd.DataFrame,
    daily_entrants: pd.Series,
    reference_start: date,
    reference_end: date,
    prediction_start: Optional[date] = None,
    rate_adjustment: Union[pd.Series, Iterable[pd.Series]] = None,
    number_adjustment: Union[pd.Series, Iterable[pd.Series]] = None,
    external_bin_identifier: Optional[date] = None,
) -> ModelPredictor:
    stats = PopulationStats(df=df, external_bin_identifier=external_bin_identifier)

    transition_rates = stats.raw_transition_rates(reference_start, reference_end).copy()
    transition_rates.index.names = ["from", "to"]
    daily_entrants.index.names = ["from", "to"]

    if number_adjustment is not None:
        if isinstance(number_adjustment, pd.Series):
            number_adjustment = [number_adjustment]
        for adjustment in number_adjustment:
            adjustment = adjustment.copy()
            adjustment.index.names = ["from", "to"]
            daily_entrants = combine_rates(daily_entrants, adjustment)

    if rate_adjustment is not None:
        if isinstance(rate_adjustment, pd.Series):
            rate_adjustment = [rate_adjustment]
        for adjustment in rate_adjustment:
            adjustment = adjustment.copy()
            adjustment.index.names = ["from", "to"]
            transition_rates = combine_rates(transition_rates, adjustment)

    # If we haven't provided a prediction start date, use the reference end
    if prediction_start is None:
        prediction_start = reference_end

    return ModelPredictor(
        population=stats.stock_at(prediction_start),
        transition_rates=transition_rates,
        transition_numbers=daily_entrants,
        start_date=prediction_start,
        external_bin_identifier=external_bin_identifier,
    )
