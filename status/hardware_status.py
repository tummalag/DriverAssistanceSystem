from enum import Enum, auto

class StatusType(Enum):
    OK = auto()
    ERROR = auto()
    NOT_FOUND = auto()
    UNKNOWN = auto()

class Component(Enum):
    CAMERA = auto()
    HAILO = auto()
    AUDIO = auto()

class HardwareStatus:
    def __init__(self):
        self.status = {
            Component.CAMERA: StatusType.UNKNOWN,
            Component.HAILO: StatusType.UNKNOWN,
            Component.AUDIO: StatusType.UNKNOWN
        }
    
    def update_status(self, component: Component, status: StatusType):
        self.status[component] = status
    
    def all_ok(self) -> bool:
        return all(stat == StatusType.OK for stat in self.status.values())
    
    def print_status(self):
        print("\nHardware Status Report:")
        print("----------------------")
        for component, status in self.status.items():
            print(f"{component.name}: {status.name}")
        print("----------------------")
