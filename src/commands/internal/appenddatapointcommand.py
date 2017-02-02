from typing import Dict, Any

from command import MenuCommand, ExitCode
from commands.internal.datastoredependantcommand import DataStoreDependantCommand
from session import Session

from src.utils import get_integer_from_user


def get_data_to_append(session: Session) -> int:
    return get_integer_from_user(session, 'What data point should be appended: ')


class AppendDataCommand(MenuCommand):

    def __new__(cls, *args, **kwargs) -> MenuCommand:
        return DataStoreDependantCommand(cls)

    def name(self) -> str:
        return 'Append Data'

    def description(self) -> str:
        return 'Appends a point of data to the common data store'

    def execute(self, session: Session, args: Dict[str, Any]) -> ExitCode:
        new_data = get_data_to_append(session)

        args['data'].append(new_data)

        return ExitCode.SUCCESS
