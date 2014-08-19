#-*- encoding: utf-8 -*-
import duinobot
from datetime import datetime, timedelta


class ExpectationException(Exception):
    def __init__(self, msg):
        self.msg = msg

    def __str__(self):
        return self.msg


class NothingExpected(ExpectationException):
    pass


class OtherMessageExpected(ExpectationException):
    pass


class OtherParamsExpected(ExpectationException):
    def _format(self, method, *args, **kwargs):
        msg = ["<{0}(".format(method)]
        msg.extend(args)
        for name in kwargs:
            msg.append(name + " = " + kwargs[name] + ",")
        msg.append(")>")
        msg = map(lambda x: str(x), msg)
        print(msg)
        print("".join(msg))
        return "".join(msg)

    def __init__(self, expected, method, *args, **kwargs):
        self.msg = self._format(
            expected["message"],
            *expected["*args"],
            **expected["**kwargs"]
        )
        self.msg += " expected but got "
        self.msg += self._format(method, *args, **kwargs)


class MockLowLevelBoard(object):
    def __init__(self, device):
        self.live_robots = []
        self.expectations = []

    def expect(self, message, *args, **kwargs):
        self.expectations.append({
            "message": message,
            "*args": args,
            "**kwargs": kwargs
        })

    def expect_nothing(self):
        self.expectations = []

    def expectations_satisfied(self):
        return len(self.expectations) == 0

    def got(self, method, *args, **kwargs):
        if not self.expectations:
            raise NothingExpected(" ".join((
                "Expecting nothing but got",
                method
            )))
        expected = self.expectations.pop(0)
        if expected["message"] != method:
            raise OtherMessageExpected(" ".join((
                "Expecting",
                expected["message"],
                "but got",
                method
            )))
        if expected["*args"] != args or expected["**kwargs"] != kwargs:
            raise OtherParamsExpected(expected, method, *args, **kwargs)

    def send_sysex(self, *args):
        self.got("send_sysex", *args)

    def pass_time(self, time):
        self.got("pass_time", time)

    def exit(self):
        pass


class MockBoard(duinobot.Board):

    def __init__(self, *args, **kwargs):
        self.board = MockLowLevelBoard(*args, **kwargs)
        self._last_motors_invocation = dict()
