from State import State

class LockedState(State):
    def press_power_button(self, device):
        from OffState import OffState

        print("Device is turning off.")
        device.set_state(OffState())
    
    def press_home_button(self, device):
        from ReadyState import ReadyState

        print("Device is unlocking and entering Ready State.")
        device.set_state(ReadyState())