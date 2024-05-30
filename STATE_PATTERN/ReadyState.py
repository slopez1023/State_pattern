from State import State

class ReadyState(State):
    def press_power_button(self, device):
        from LockedState import LockedState

        print("Device is locking.")
        device.set_state(LockedState())
    
    def press_home_button(self, device):
        print("Device is already in Ready State.")