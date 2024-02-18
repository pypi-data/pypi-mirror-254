from decimal import Decimal

from scipy.stats import rv_discrete

from analysis.forecasting.forecast_strategies.form_forecast_strategy import (
    FormForecastStrategy,
)
from analysis.forecasting.form_forecast import FormForecast
from analysis.horse import Horse
from analysis.race_conditions import RaceConditions


class RepeatLto(FormForecastStrategy):
    def __call__(self, horse: Horse, _race_conditions: RaceConditions) -> FormForecast:
        lto_rating = horse.performances[-1].form_rating
        probability_distribution = rv_discrete(values=([lto_rating], [1]))
        solidity = Decimal(1.0)
        return FormForecast(probability_distribution, solidity)
