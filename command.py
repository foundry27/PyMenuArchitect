from enum import Enum
from abc import ABCMeta, abstractmethod
from session import Session
from typing import Dict, Any


class ExitCode(Enum):
    SUCCESS = 0
    FAILURE = 1
    TERMINATED = 2


class MenuCommand(metaclass=ABCMeta):

    @abstractmethod
    def name(self) -> str:
        pass

    @abstractmethod
    def description(self) -> str:
        pass

    @abstractmethod
    def execute(self, session: Session, args: Dict[str, Any]) -> ExitCode:
        pass
