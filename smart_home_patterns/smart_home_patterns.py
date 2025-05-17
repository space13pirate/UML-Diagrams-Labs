# -----------------------------
# 1. Singleton: SmartHomeHub
# -----------------------------
class SmartHomeHub:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.devices = []
            print("[Singleton] Creating SmartHomeHub instance")
        return cls._instance

    def register_device(self, device):
        self.devices.append(device)

    def broadcast(self, message):
        print(f"[Singleton] Broadcasting: {message}")
        for device in self.devices:
            device.receive(message)


# ----------------------------------
# 2. Factory Method: Device Factory
# ----------------------------------
class SmartDevice:
    def receive(self, message):
        raise NotImplementedError()

class SmartLight(SmartDevice):
    def receive(self, message):
        print(f"[SmartLight] received: {message}")

class SmartThermostat(SmartDevice):
    def receive(self, message):
        print(f"[SmartThermostat] received: {message}")

class SmartCamera(SmartDevice):
    def receive(self, message):
        print(f"[SmartCamera] received: {message}")

class SmartDoorLock(SmartDevice):
    def receive(self, message):
        print(f"[SmartDoorLock] received: {message}")

class DeviceFactory:
    def create_device(self, device_type):
        print(f"[FactoryMethod] Creating device of type: {device_type}")
        if device_type == "light":
            return SmartLight()
        elif device_type == "thermostat":
            return SmartThermostat()
        elif device_type == "camera":
            return SmartCamera()
        elif device_type == "doorlock":
            return SmartDoorLock()
        else:
            raise ValueError("Unknown device type")


# -------------------------------
# 3. Facade: HomeController
# -------------------------------
class HomeController:
    def __init__(self):
        self.hub = SmartHomeHub()

    def leave_home(self):
        print("[Facade] Activating leave_home mode...")
        self.hub.broadcast("lock_doors")
        self.hub.broadcast("turn_off_lights")
        self.hub.broadcast("activate_cameras")

    def arrive_home(self):
        print("[Facade] Activating arrive_home mode...")
        self.hub.broadcast("unlock_doors")
        self.hub.broadcast("turn_on_lights")
        self.hub.broadcast("deactivate_cameras")


# -----------------------------
# 4. Observer: MotionSensor
# -----------------------------
class Observer:
    def update(self):
        raise NotImplementedError()

class MotionSensor:
    def __init__(self):
        self._observers = []

    def attach(self, observer):
        print(f"[Observer] Attaching {observer.__class__.__name__}")
        self._observers.append(observer)

    def detect_motion(self):
        print("[Observer] Motion detected!")
        for observer in self._observers:
            observer.update()

class AlarmSystem(Observer):
    def update(self):
        print("[AlarmSystem] Intrusion detected!")

class AutoLight(Observer):
    def update(self):
        print("[AutoLight] Turning on light due to motion")


# ---------------------------
# 5. State: SmartLight State
# ---------------------------
class LightState:
    def toggle(self, context):
        raise NotImplementedError()

class LightOn(LightState):
    def toggle(self, context):
        print("[State] Switching light OFF")
        context.state = LightOff()

class LightOff(LightState):
    def toggle(self, context):
        print("[State] Switching light ON")
        context.state = LightOn()

class LightContext:
    def __init__(self):
        self.state = LightOff()
        print("[State] Initial light state: OFF")

    def press_button(self):
        print("[State] Button pressed")
        self.state.toggle(self)


# ---------------------------
# Demo: Main
# ---------------------------
if __name__ == "__main__":
    print("\n--- Smart Home Demo ---\n")

    # Singleton and Factory
    print("\n[DEMO] Singleton + Factory Method")
    hub = SmartHomeHub()
    factory = DeviceFactory()
    light = factory.create_device("light")
    thermostat = factory.create_device("thermostat")
    hub.register_device(light)
    hub.register_device(thermostat)

    # Facade
    print("\n[DEMO] Facade Pattern")
    controller = HomeController()
    controller.leave_home()
    controller.arrive_home()

    # Observer
    print("\n[DEMO] Observer Pattern")
    sensor = MotionSensor()
    alarm = AlarmSystem()
    auto_light = AutoLight()
    sensor.attach(alarm)
    sensor.attach(auto_light)
    sensor.detect_motion()

    # State
    print("\n[DEMO] State Pattern")
    smart_light = LightContext()
    smart_light.press_button()
    smart_light.press_button()
