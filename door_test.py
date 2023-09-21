import pytest
from door import Door, DoorLock


class TestDoor:

    @pytest.fixture
    def a_door(self):
        return Door(DoorLock(), 'green')


    def test_initial(self,a_door):
        assert a_door.color == 'green'

    def test_get_set_color(self, a_door):
        a_door.color = 'red'
        assert a_door.color == 'red'


    def test_door_open(self, a_door):
        a_door.open_the_door()
        assert a_door.door_is_open
    def test_door_close(self, a_door):
        a_door.close_the_door()
        assert a_door.door_is_open == False

    def test_door_locking(self, a_door):
        a_door.lock_the_door()
        assert a_door.door_ist_locked

    def test_door_unlock(self, a_door):
        a_door.unlock_the_door()
        assert a_door.door_ist_locked == False

