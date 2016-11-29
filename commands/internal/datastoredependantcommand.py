from command import MenuCommand, ExitCode
from session import Session
from typing import Dict, Any


class DataStoreDependantCommand(MenuCommand):

    def __init__(self, command: MenuCommand):
        self.command = command

    def name(self) -> str:
        return self.command.name(self.command)

    def description(self) -> str:
        return self.command.description(self.command)

    def execute(self, session: Session, args: Dict[str, Any]) -> ExitCode:
        lookup = args.get('data')
        if lookup is None:
            session.get_io().error('The common data store has not been initialized yet!')
            return ExitCode.FAILURE
        elif len(lookup) == 0:
            session.get_io().error('The common data store does not have any elements in it!')
            return ExitCode.FAILURE
        else:
            return self.command.execute(self=self.command, session=session, args=args)
