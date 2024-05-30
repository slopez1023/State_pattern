from OffState import OffState

class Device:
    def __init__(self):
        self.state = OffState()
    
    def set_state(self, state):
        self.state = state
    
    def press_power_button(self):
        self.state.press_power_button(self)
    
    def press_home_button(self):
        self.state.press_home_button(self)

if __name__ == "__main__":
    device = Device()

    print("Initial State: OffState")
    device.press_power_button()  
    device.press_home_button()   
    device.press_power_button() 
    device.press_power_button() 