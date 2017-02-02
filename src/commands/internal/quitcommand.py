from sys import exit
from typing import Dict, Any

from command import MenuCommand, ExitCode

from src.session import Session


class QuitMenuCommand(MenuCommand):

    def name(self) -> str:
        return 'Quit'

    def description(self) -> str:
        return 'Exits the program'

    def execute(self, session: Session, args: Dict[str, Any]) -> ExitCode:
        session.get_io().output('Exiting program...')
        exit()
        return ExitCode.SUCCESS
