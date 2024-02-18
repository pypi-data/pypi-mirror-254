from analysis.forecasting.form_forecast import FormForecast
from analysis.horse import Horse
from analysis.race_conditions import RaceConditions


class FormForecastStrategy:
    def __call__(self, horse: Horse, race_conditions: RaceConditions) -> FormForecast:
        raise NotImplementedError
