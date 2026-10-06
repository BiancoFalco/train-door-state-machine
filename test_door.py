from door import TrainDoor, DoorState


def test_starts_closed_and_traction_allowed():
    door = TrainDoor()
    assert door.state == DoorState.CLOSED_LOCKED
    assert door.traction_allowed()


def test_no_release_while_moving():
    door = TrainDoor()
    assert door.release(speed_kmh=30, at_platform=True) is False
    assert door.state == DoorState.CLOSED_LOCKED


def test_full_station_stop_cycle():
    door = TrainDoor()
    assert door.release(speed_kmh=0, at_platform=True)
    door.open()
    assert not door.traction_allowed()
    door.close()
    door.closing_finished(obstacle_detected=False)
    assert door.state == DoorState.CLOSED_LOCKED
    assert door.traction_allowed()


def test_obstacle_reopens_door_and_blocks_traction():
    door = TrainDoor()
    door.release(speed_kmh=0, at_platform=True)
    door.open()
    door.close()
    door.closing_finished(obstacle_detected=True)
    assert door.state == DoorState.OPEN
    assert not door.traction_allowed()
