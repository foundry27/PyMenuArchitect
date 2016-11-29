from typing import List
from command import MenuCommand
from commands.internal.dataprintingcommand import DataPrintingCommand
from commands.internal.quitcommand import QuitMenuCommand
from commands.internal.datainitializationcommand import DataInitializationMenuCommand
from commands.internal.appenddatapointcommand import AppendDataCommand
from commands.internal.deletefirstoccurrencecommand import DeleteFirstOccurrenceCommand
from commands.internal.deletealloccourrencescommand import DeleteAllOccurrencesCommand
from commands.internal.findnthlargestcommand import FindNthLargestCommand
from commands.internal.findfirstsumindexcommand import FindFirstSumIndexCommand

_MENU_COMMANDS = [DataInitializationMenuCommand(),
                  DataPrintingCommand(),
                  AppendDataCommand(),
                  DeleteFirstOccurrenceCommand(),
                  DeleteAllOccurrencesCommand(),
                  FindNthLargestCommand(),
                  FindFirstSumIndexCommand(),
                  QuitMenuCommand()]  # type: List[MenuCommand]


def get_commands() -> List[MenuCommand]:
    return _MENU_COMMANDS
