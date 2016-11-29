import heapq
from typing import Dict, Any

from command import MenuCommand, ExitCode
from commands.internal.datastoredependantcommand import DataStoreDependantCommand
from session import Session
from utils import get_integer_from_user


def get_number_off_largest(session: Session) -> int:
    while True:
        num_off_largest = get_integer_from_user(session, 'For finding the nth largest element, n is: ')
        if num_off_largest <= 0:
            session.get_io().output('Your input must be greater than zero, instead got {}'.format(str(num_off_largest)))
            session.clear()
            continue
        return num_off_largest


class FindNthLargestCommand(MenuCommand):
    def __new__(cls, *args, **kwargs) -> MenuCommand:
        return DataStoreDependantCommand(cls)

    def name(self) -> str:
        return 'Find Nth Largest'

    def description(self) -> str:
        return 'Finds the nth largest data point in the common data store'

    def execute(self, session: Session, args: Dict[str, Any]) -> ExitCode:
        num_off_largest = get_number_off_largest(session)

        num_suffix = ('st' if num_off_largest == 1 else
                      ('nd' if num_off_largest == 2 else
                       ('rd' if num_off_largest == 3 else 'th')))

        data = args['data']
        if num_off_largest > len(data):
            session.get_io().error(
                'Unable to find the {}{} largest data point: There are only {} data points in the common data store!'
                    .format(num_off_largest, num_suffix, len(data)))

        nth_largest = heapq.nlargest(num_off_largest, data)[num_off_largest - 1]

        session.get_io().output('The {}{} largest data point is: {}'
                                .format(num_off_largest, num_suffix, nth_largest))

        return ExitCode.SUCCESS
