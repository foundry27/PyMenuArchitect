import os
from typing import Any, Callable, Optional, Iterable
from abc import ABCMeta, abstractmethod
from collections import deque


class IODescriptor(metaclass=ABCMeta):

    @abstractmethod
    def input(self) -> str:
        pass

    @abstractmethod
    def output(self, o: Any, end: str = "\n") -> None:
        pass

    def error(self, o: Any, end: str = "\n") -> None:
        self.output(o)


class Session(metaclass=ABCMeta):

    @abstractmethod
    def get_io(self) -> IODescriptor:
        pass

    @abstractmethod
    def lines(self) -> Iterable[str]:
        pass

    @abstractmethod
    def clear(self) -> None:
        pass


class SessionWithIO(Session, IODescriptor):
    Consumer = Callable[[Any, str], None]

    Supplier = Callable[[], str]

    def __init__(self,
                 inputsupplier: Supplier,
                 outputconsumer: Consumer,
                 errorconsumer: Optional[Consumer] = None):
        self.inputsupplier = inputsupplier
        self.outputconsumer = outputconsumer
        self.errorconsumer = errorconsumer if isinstance(errorconsumer, Callable) else outputconsumer
        self.received_lines = deque()

    def input(self) -> str:
        return self.inputsupplier()

    def output(self, o: Any, end: str = "\n") -> None:
        self.received_lines.append(str(o))
        self.outputconsumer(o, end)

    def error(self, o: Any, end: str = "\n") -> None:
        self.received_lines.append(str(o))
        self.errorconsumer(o, end)

    def clear(self) -> None:
        self.received_lines.clear()
        os.system('cls' if os.name == 'nt' else 'clear')

    def lines(self) -> Iterable[str]:
        return self.received_lines

    def get_io(self) -> IODescriptor:
        return self
