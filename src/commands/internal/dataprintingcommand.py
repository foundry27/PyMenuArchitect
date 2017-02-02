import time
from typing import Dict, Any

from command import MenuCommand, ExitCode
from commands.internal.datastoredependantcommand import DataStoreDependantCommand
from session import Session

from src.utils import get_integer_from_user


def get_data_points_per_line(session: Session) -> int:
    while True:
        data_points_per_line = get_integer_from_user(session, 'How many data points per line should be outputted: ')
        if data_points_per_line <= 0:
            session.get_io().output('Your input must be greater than zero, instead got {}'.format(str(data_points_per_line)))
            time.sleep(1)
            session.clear()
            continue
        return data_points_per_line


class DataPrintingCommand(MenuCommand):

    def __new__(cls, *args, **kwargs) -> MenuCommand:
        return DataStoreDependantCommand(cls)

    def name(self) -> str:
        return 'Print'

    def description(self) -> str:
        return 'Prints out the common data store in its current state'

    def execute(self, session: Session, args: Dict[str, Any]) -> ExitCode:
        data_points_per_line = get_data_points_per_line(session)

        num = 0
        for point in args['data']:
            num += 1
            end = ' '
            if num == data_points_per_line:
                num = 0
                end = '\n'
            session.get_io().output(point, end=end)
        if num > 0:
            session.get_io().output('', end='\n')

        session.get_io().output('Press any key to return to the menu', end='')
        session.get_io().input()

        return ExitCode.SUCCESS
