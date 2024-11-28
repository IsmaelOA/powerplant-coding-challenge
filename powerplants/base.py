from abc import ABC, abstractmethod

class PowerPlant(ABC):
    def __init__(self, name, pmin, pmax, efficiency):
        self.name = name
        self.pmin = pmin
        self.pmax = pmax
        self.efficiency = efficiency

    @abstractmethod
    def unit_cost(self, fuels):
        """
        Abstract method to calculate the unit cost (€/MWh) for the plant.
        """
        pass
