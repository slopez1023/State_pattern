from abc import ABC, abstractmethod

class State(ABC):
    @abstractmethod
    def press_power_button(self, device):
        pass

    @abstractmethod
    def press_home_button(self, device):
        pass
