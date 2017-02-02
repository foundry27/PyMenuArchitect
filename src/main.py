import sys

from menu import SimpleMenu
from runner import run_console

from src.session import SessionWithIO

if __name__ == "__main__":
    from src.commands.commands import get_commands

    session = SessionWithIO(
        lambda: input(),
        lambda x, end: print(x, end=end),
        lambda x, end: print(x, end=end, file=sys.stderr)
    )

    menu = SimpleMenu(get_commands())

    run_console(session, menu)
