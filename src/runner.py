import itertools
import time
from typing import Dict, Any

from command import MenuCommand, ExitCode
from menu import Menu
from session import IODescriptor, Session

from src.utils import MalformedInputException


class IllegalCommandIndexException(Exception):
    def __init__(self, index: int):
        self.index = index


def show_menu_options(io: IODescriptor, menu: Menu) -> None:
    labels = ['"' + x.name() + '"' + ': ' + x.description() for x in menu]
    numbered_labels = itertools.zip_longest(itertools.takewhile(lambda x: x <= len(labels), itertools.count(1)), labels)
    concatenated_labels = '\n'.join(itertools.starmap(lambda num, label: str(num) + '. ' + label, numbered_labels))
    io.output('Available Commands: ' + ('\n' + concatenated_labels if len(concatenated_labels) > 0 else 'None.'))


def retrieve_user_command_choice(io: IODescriptor, menu: Menu) -> MenuCommand:
    io.output('Select an option: ', end='')
    user_input = io.input()

    try:
        parsed_command_index = int(user_input)
    except ValueError:
        raise MalformedInputException('Your input must be a positive integer, instead got "{}"'.format(user_input))

    validate_user_command_choice_bounds(parsed_command_index, menu)
    return menu[parsed_command_index]


def validate_user_command_choice_bounds(index: int, menu: Menu) -> None:
    if index <= 0:
        raise MalformedInputException('Your input must be greater than zero, instead got {}'.format(str(index)))
    elif index > len(menu):
        raise MalformedInputException('Cannot access command at index {}: there {} only {} {} in this menu'
                                      .format(str(index), 'is' if len(menu) == 1 else 'are',
                                              str(len(menu)), 'command' if len(menu) == 1 else 'commands'))


def handle_illegal_command_index_exception(exception: IllegalCommandIndexException, io: IODescriptor, menu: Menu) -> None:
    io.error('Illegal command index "{}": must be between 1 and {}.'.format(exception.index, len(menu)))
    time.sleep(1)


def handle_malformed_input_exception(exception: MalformedInputException, io: IODescriptor) -> None:
    io.error(exception.message)
    time.sleep(1)


def handle_valid_command(command: MenuCommand, session: Session, args: Dict[str, Any]) -> None:
    session.clear()
    exit_code = command.execute(session, args)  # type: ExitCode
    session.get_io().output('Command "{}" completed with exit code {}'.format(command.name(), exit_code.name))
    time.sleep(1)


def run_console(session: Session, menu: Menu, **kwargs: Dict[str, Any]) -> None:
    session.clear()
    if len(menu) == 0:
        session.get_io().output("No commands present in menu. Exiting...")
        return

    while True:
        show_menu_options(session.get_io(), menu)
        try:
            command_lookup = retrieve_user_command_choice(session.get_io(), menu)  # type: MenuCommand
            handle_valid_command(command_lookup, session, kwargs)
        except IllegalCommandIndexException as illegal_input_ex:
            handle_illegal_command_index_exception(illegal_input_ex, session.get_io(), menu)
        except MalformedInputException as malformed_input_ex:
            handle_malformed_input_exception(malformed_input_ex, session.get_io())

        session.clear()
