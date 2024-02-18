from decimal import Decimal

from horsetalk import RaceDesignation

from .form_prediction_factor import FormPredictionFactor


class HandicapDebutBonus(FormPredictionFactor):
    def _calc(self) -> Decimal:
        return Decimal(
            5
            if self.horse.is_handicap_debutant
            and self.race_conditions.race_designation == RaceDesignation.HANDICAP
            else 0
        )
