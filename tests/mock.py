"""
Module containing mocked classes for Unit Testing
Does nothing interesting on its own.
"""


class Bot:
    """
    Mock bot object
    """
    def say(self,message, *args, **kwargs)->None:
        """
        Dummy method
        :param args:
        :param kwargs:
        :return:
        """
        print("[Bot] {}".format(message))

    def reply(self, *args, **kwargs)->None:
        """
        Dummy method
        :param args:
        :param kwargs:
        :return:
        """
        pass


class Trigger:
    def __init__(self, host, owner=False, op=False, admin=False):
        self.owner = owner
        self.op = op
        self.admin = admin
        self.host = host
