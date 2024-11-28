from .base import PowerPlant

class GasFiredPlant(PowerPlant):
    def unit_cost(self, fuels):
        fuel_cost = fuels["gas(euro/MWh)"] / self.efficiency
        co2_cost = 0.3 * fuels["co2(euro/ton)"]
        return fuel_cost + co2_cost

class TurboJetPlant(PowerPlant):
    def unit_cost(self, fuels):
        fuel_cost = fuels["kerosine(euro/MWh)"] / self.efficiency
        return fuel_cost

class WindTurbinePlant(PowerPlant):
    def unit_cost(self, fuels):
        return 0
