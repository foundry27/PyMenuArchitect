import random
import time
from collections import deque
from typing import Dict, Any, Optional

from command import MenuCommand, ExitCode
from session import Session
from utils import get_integer_from_user


def retrieve_data_point_count(session: Session) -> int:
    while True:
        data_point_count = get_integer_from_user(session, 'How many data points do you want to create: ')
        if data_point_count <= 0:
            session.get_io().output('Your input must be greater than zero, instead got {}'.format(str(data_point_count)))
            time.sleep(1)
            session.clear()
            continue
        return data_point_count


def retrieve_min_data_value(session: Session) -> int:
    return get_integer_from_user(session, 'What should the minimum data value be: ')


def retrieve_max_data_value(session: Session) -> int:
    return get_integer_from_user(session, 'What should the maximum data value be: ')


def ensure_data_not_overwritten(session: Session, data_lookup: Optional[Any]) -> bool:
    if data_lookup is None:
        return True

    while True:
        session.get_io().output('Data has already been loaded for this session. Do you want to replace it? (y/n): ', end='')
        user_input = session.get_io().input().lower()
        if user_input == 'y':
            return True
        elif user_input == 'n':
            return False
        else:
            session.get_io().error('Your response must be either "y" or "n", instead got "{}"'.format(user_input))
            time.sleep(1)
            session.clear()


class DataInitializationMenuCommand(MenuCommand):

    def name(self) -> str:
        return 'Initialize'

    def description(self) -> str:
        return 'Initializes the data in the common data store'

    def execute(self, session: Session, args: Dict[str, Any]) -> ExitCode:
        if not ensure_data_not_overwritten(session, args.get('data')):
            session.get_io().output("Not modifying existing data store. Continuing...")
            return ExitCode.SUCCESS

        data_point_count = retrieve_data_point_count(session)
        min_data_value = retrieve_min_data_value(session)
        max_data_value = retrieve_max_data_value(session)
        args['data'] = deque((random.randint(min(min_data_value, max_data_value), max(min_data_value, max_data_value)) for _ in range(data_point_count)))

        session.get_io().output('{} data points initialized with values between {} and {}'
                                .format(data_point_count, min_data_value, max_data_value))
        return ExitCode.SUCCESS
