from collections import deque
from itertools import filterfalse
from typing import Dict, Any

from command import MenuCommand, ExitCode
from commands.internal.datastoredependantcommand import DataStoreDependantCommand
from session import Session

from src.utils import get_integer_from_user


def get_data_to_remove(session: Session) -> int:
    return get_integer_from_user(session, 'What data point should be removed: ')


class DeleteAllOccurrencesCommand(MenuCommand):

    def __new__(cls, *args, **kwargs) -> MenuCommand:
        return DataStoreDependantCommand(cls)

    def name(self) -> str:
        return 'Delete All Occurrences'

    def description(self) -> str:
        return 'Deletes all occurrences of a point of data from the common data store'

    def execute(self, session: Session, args: Dict[str, Any]) -> ExitCode:
        data_to_remove = get_data_to_remove(session)

        data = args['data']
        args['data'] = deque(filterfalse(lambda x: x == data_to_remove, data))

        session.get_io().output('Removed {} data points'.format(len(data) - len(args['data'])))

        return ExitCode.SUCCESS
