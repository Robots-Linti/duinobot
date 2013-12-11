import duinobot
import test_helper
import unittest

class TestMovement(unittest.TestCase):
    def setUp(self):
        self.board = test_helper.MockBoard("/dev/ttyUSB0")

    def test_motor0_in_range(self):
        self.board.board.expect("send_sysex", 1, [0, 42])
        self.board.motor0(0, 42)
        self.board.board.expect("send_sysex", 1, [100, 42])
        self.board.motor0(100, 42)

    def test_motor1_in_range(self):
        self.board.board.expect("send_sysex", 2, [0, 42])
        self.board.motor1(0, 42)
        self.board.board.expect("send_sysex", 2, [100, 42])
        self.board.motor1(100, 42)
    
    def test_motor0_out_range(self):
        self.board.board.expect_nothing()
        self.board.motor0(-1, 42)
        self.board.motor0(-1, 42)

    def test_motor1_out_range(self):
        self.board.board.expect_nothing()
        self.board.motor1(-1, 42)
        self.board.motor1(-1, 42)

    def test_motors_in_range_positive(self):
        self.board.board.expect("send_sysex", 4, [0, 0, 0, 0, 42])
        self.board.motors(0, 0, robotid = 42)
        self.board.board.expect("send_sysex", 4, [100, 100, 1, 1, 42])
        self.board.motors(100, 100, robotid = 42)

    def test_motors_in_range_negative(self):
        self.board.board.expect("send_sysex", 4, [1, 1, 0, 0, 42])
        self.board.motors(-1, -1, robotid = 42)
        self.board.board.expect("send_sysex", 4, [100, 100, 0, 0, 42])
        self.board.motors(-100, -100, robotid = 42)

    def test_motors_out_range(self):
        self.board.board.expect_nothing()
        self.board.motors(-101, 0, robotid = 42)
        self.board.motors(0, -101, robotid = 42)
        self.board.motors(101, 0, robotid = 42)
        self.board.motors(0, 101, robotid = 42)

    def test_motors_with_time(self):
        self.board.board.expect("send_sysex", 4, [100, 100, 1, 1, 42])
        self.board.board.expect("pass_time", 5)
        self.board.board.expect("send_sysex", 4, [0, 0, 0, 0, 42])
        self.board.motors(100, 100, 5, 42)

if __name__ == "__main__":
    unittest.main()
