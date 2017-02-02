import time

from src.session import Session


class MalformedInputException(Exception):
    def __init__(self, message: str):
        self.message = message


class InputAttemptTimeoutException(Exception):
    def __init__(self, message: str, max_attempts_given: int):
        self.message = message
        self.max_attempts_given = max_attempts_given


def get_integer_from_user(session: Session, message: str, max_attempts: int = 0, retry_delay: int = 1) -> int:
    attempt_count = 0
    while attempt_count <= max_attempts:
        session.get_io().output(message, end='')
        user_input = session.get_io().input()

        try:
            return int(user_input)
        except ValueError:
            session.get_io().error('Your input must be an integer, instead got "{}"'.format(user_input))
            time.sleep(retry_delay)
            session.clear()
            if max_attempts > 0:
                attempt_count += 1
                if attempt_count > max_attempts:
                    raise InputAttemptTimeoutException('Exceeded maximum number of input attempts', max_attempts)


