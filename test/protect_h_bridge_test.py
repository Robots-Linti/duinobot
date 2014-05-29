import duinobot
import test_helper
import unittest
from datetime import datetime, timedelta
import time


class TestProtectHBridge(unittest.TestCase):
    def setUp(self):
        self.board = test_helper.MockBoard("/dev/ttyUSB0")
        self.robot = duinobot.Robot(self.board, 42)

    def tearDown(self):
        self.board.board.expectations = []

    def test_multiple_forwards_in_one_second(self):
        """ Having 1000ms the Robot should perform 10 movements or less
        (1 movement every 100ms at most)"""
        self.board.board.expect("send_sysex", 4, [100, 100, 1, 1, 42])
        self.board.board.expectations *= 10  # 10 movements
        now = datetime.now()
        while datetime.now() - now < timedelta(0, 1, 0):
            self.robot.forward(100)

    def test_mixed_forward_turnLeft_with_short_pauses(self):
        """Having N movements with a pause bigger than 100ms the Robot
        should perform all movements"""
        n = 20
        for i in range(n):
            self.board.board.expect("send_sysex", 4, [100, 100, 1, 1, 42])
            self.board.board.expect("send_sysex", 4, [0, 0, 0, 0, 42])
            self.board.board.expect("send_sysex", 4, [50, 50, 1, 0, 42])
            self.board.board.expect("send_sysex", 4, [0, 0, 0, 0, 42])
            self.robot.forward(100)
            time.sleep(0.101)
            self.robot.stop()
            self.robot.turnLeft(50)
            time.sleep(0.101)
            self.robot.stop()
        self.assertTrue(self.board.board.expectations_satisfied())

if __name__ == "__main__":
    unittest.main()
