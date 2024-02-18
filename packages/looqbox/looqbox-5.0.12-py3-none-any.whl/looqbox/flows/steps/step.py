from abc import ABC, abstractmethod

from looqbox.objects.message.message import Message


class Step(ABC):
    def __init__(self, message: Message):
        self.message = message

    @abstractmethod
    def execute(self):
        ...
