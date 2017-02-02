from typing import Dict, Any

from command import MenuCommand, ExitCode
from commands.internal.datastoredependantcommand import DataStoreDependantCommand
from session import Session

from src.utils import get_integer_from_user


def get_data_to_try_to_sum(session: Session) -> int:
    return get_integer_from_user(session, 'What number should we try to find data points summing to: ')


class FindFirstSumIndexCommand(MenuCommand):

    def __new__(cls, *args, **kwargs) -> MenuCommand:
        return DataStoreDependantCommand(cls)

    def name(self) -> str:
        return 'Find First Sum Index'

    def description(self) -> str:
        return 'Find the index of the first data point such that all subsequent data adds to a given number'

    def execute(self, session: Session, args: Dict[str, Any]) -> ExitCode:
        data_to_find = get_data_to_try_to_sum(session)

        point_dict = {}
        curr_sum = 0
        curr_index = 0
        for point in reversed(args['data']):
            curr_sum += point
            indices = point_dict.setdefault(curr_sum, list())
            indices.append(curr_index)
            curr_index += 1

        session.get_io().output(len(args['data']) - min(point_dict.get(data_to_find)) - 1)

        return ExitCode.SUCCESS
