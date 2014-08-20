import duinobot
import test_helper
import unittest


class TestServo(unittest.TestCase):
    def setUp(self):
        self.board = test_helper.MockBoard("/dev/ttyUSB0")
        self.robot = duinobot.Robot(self.board, 1)

    def test_config_servo(self):
        #  0x70 // pin, minPulse_LO, minPulse_HI, maxPulse_LO, maxPulse_HI,
        #          robot_id
        self.board.board.expect("send_sysex", 0x70,
                                [9, 0, 3, 32, 4,
                                 self.robot.robotid],
                                )
        # 384 = 2**7 + 2**8
        # 544 = 2**5 + 2**9
        self.robot.configServo(9, 384, 544)

    def test_move_servo(self):
        self.board.board.expect("send_sysex", 0x0A,
                                [9, 1, 2,
                                 self.robot.robotid])
        self.robot.moveServo(9, 130)


if __name__ == "__main__":
    unittest.main()
