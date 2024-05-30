from State import State

class OffState(State):
    def press_power_button(self, device):
        from LockedState import LockedState
        print("Device is turning on and entering Locked State.")
        device.set_state(LockedState())
    
    def press_home_button(self, device):
        print("Device is off. Home button does nothing.")