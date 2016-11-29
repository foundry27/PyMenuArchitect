from command import MenuCommand, ExitCode
from session import Session
from typing import Dict, Any
from commands.internal.datastoredependantcommand import DataStoreDependantCommand
from utils import get_integer_from_user


def get_data_to_remove(session: Session) -> int:
    return get_integer_from_user(session, 'What data point should be removed: ')


class DeleteFirstOccurrenceCommand(MenuCommand):

    def __new__(cls, *args, **kwargs) -> MenuCommand:
        return DataStoreDependantCommand(cls)

    def name(self) -> str:
        return 'Delete First Occurrence'

    def description(self) -> str:
        return 'Deletes the first occurrence of a point of data from the common data store'

    def execute(self, session: Session, args: Dict[str, Any]) -> ExitCode:
        data_to_remove = get_data_to_remove(session)

        try:
            args['data'].remove(data_to_remove)
            session.get_io().output('Removed the first instance of data point "{}"'.format(data_to_remove))
        except ValueError:
            session.get_io().error('Data point "{}" is not present in the data store!'.format(data_to_remove))

        return ExitCode.SUCCESS
