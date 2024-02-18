from __future__ import annotations

import time
import uuid
from abc import ABC, abstractmethod
from typing import List, Type
from typing import TYPE_CHECKING

from looqbox.config.logger import Logger
from looqbox.flows.steps.step import Step
from looqbox.global_calling import GlobalCalling
from looqbox.objects.message.message import Message
from looqbox.objects.message.message_keys import MessageKeys


if TYPE_CHECKING:
    from looqbox.objects.flow.script_info import ScriptInfo

global_variables = GlobalCalling().looq


class BaseFlow(ABC):
    steps: List[Type[Step]]

    def __init__(self, script_info: "ScriptInfo"):
        self._init_session_id()
        self.logger = Logger.get_logger(self.__class__.__name__)
        self.message = Message()
        self.message.offer(
            (MessageKeys.SCRIPT_INFO, script_info),
        )

    @abstractmethod
    def define_steps(self):
        ...

    def run(self):
        self.define_steps()
        init_time: float = time.time()
        for step in self.steps:
            start_time: float = time.time()
            step(self.message).execute()
            end_time: float = time.time()
            time_in_ms: float = (end_time - start_time) * 1000
            self.logger.info(f"Step {step.__name__} executed in {time_in_ms:.2f} ms")
        end_time: float = time.time()
        time_in_ms: float = (end_time - init_time) * 1000
        self.logger.info(f"Flow executed in {time_in_ms:.2f} ms")

    @staticmethod
    def _init_session_id():
        global_variables.session_id = uuid.uuid4()
        global_variables.query_list[global_variables.session_id] = []
