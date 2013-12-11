import duinobot
import test_helper
import unittest
from datetime import datetime, timedelta
import time
class TestProtectHBridge(unittest.TestCase):
    def setUp(self):
        self.board = test_helper.MockBoard("/dev/ttyUSB0")
        orig = self.board.board.pass_time
        def pass_time(self, t):
            orig(t)
            time.sleep(t)
        self.board.board.pass_time = pass_time
        self.robot = duinobot.Robot(self.board, 42)
    def test_one_second(self):
        # Having 1000ms the Robot should perform 10 movements (1 movement every 100ms) or less
        self.board.board.expect("send_sysex", 4, [100, 100, 1, 1, 42])
        self.board.board.expectations *= 10 # 10 movements
        now = datetime.now()
        #while datetime.now() - now < timedelta(0, 1, 0):
        #    self.robot.forward(100)
        self.robot.forward(100)
        self.assertEqual(len(self.board.board.expectations), 0)

if __name__ == "__main__":
    unittest.main()
