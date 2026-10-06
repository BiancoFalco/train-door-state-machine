from enum import Enum, auto

# Below this speed the train counts as standing still
STANDSTILL_KMH = 0.5


class DoorState(Enum):
    CLOSED_LOCKED = auto()  # safe state: train may drive
    RELEASED = auto()       # passengers may open the doors
    OPEN = auto()
    CLOSING = auto()


class TrainDoor:
    def __init__(self):
        self.state = DoorState.CLOSED_LOCKED

    def release(self, speed_kmh: float, at_platform: bool) -> bool:
        """Release doors only at standstill and at a platform."""
        if (self.state == DoorState.CLOSED_LOCKED
                and speed_kmh < STANDSTILL_KMH
                and at_platform):
            self.state = DoorState.RELEASED
            return True
        return False

    def open(self):
        if self.state == DoorState.RELEASED:
            self.state = DoorState.OPEN

    def close(self):
        if self.state == DoorState.OPEN:
            self.state = DoorState.CLOSING

    def closing_finished(self, obstacle_detected: bool):
        if self.state != DoorState.CLOSING:
            return
        if obstacle_detected:
            self.state = DoorState.OPEN  # reopen to protect the passenger
        else:
            self.state = DoorState.CLOSED_LOCKED #closed_locked

    def traction_allowed(self) -> bool:
        """The train may only drive when the doors are closed and locked."""
        return self.state == DoorState.CLOSED_LOCKED
