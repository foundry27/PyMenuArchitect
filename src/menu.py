from abc import ABCMeta, abstractmethod
from typing import List, Union

from src.command import MenuCommand


class Menu(metaclass=ABCMeta):

    @abstractmethod
    def __iter__(self) -> MenuCommand:
        pass

    @abstractmethod
    def __len__(self) -> int:
        pass

    @abstractmethod
    def __getitem__(self, item) -> MenuCommand:
        pass


class SimpleMenu(Menu):

    def __init__(self, menucommands: List[MenuCommand]):
        self.menucommands = menucommands

    def __len__(self) -> int:
        return len(self.menucommands)

    def __iter__(self):
        for c in self.menucommands:
            yield c

    def __getitem__(self, item: Union[str, int]) -> MenuCommand:
        if isinstance(item, int):
            return self.menucommands[item - 1]
