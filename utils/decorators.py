"""
decorators.py - Message formatting decorators for T-Bomb by Rayhan

This module provides classes to format console output with colored icons and status messages.
It uses the colorama library to add ANSI color codes for better visual distinction.

Developed by Rayhan for educational purposes.
"""

from colorama import Fore, Style


class IconicDecorator(object):
    """Decorator class for icon-based message formatting."""
    def __init__(self):
        self.PASS = Style.BRIGHT + Fore.GREEN + "[ ✔ ]" + Style.RESET_ALL
        self.FAIL = Style.BRIGHT + Fore.RED + "[ ✘ ]" + Style.RESET_ALL
        self.WARN = Style.BRIGHT + Fore.YELLOW + "[ ! ]" + Style.RESET_ALL
        self.HEAD = Style.BRIGHT + Fore.CYAN + "[ # ]" + Style.RESET_ALL
        self.CMDL = Style.BRIGHT + Fore.BLUE + "[ → ]" + Style.RESET_ALL
        self.STDS = "     "


class StatusDecorator(object):
    """Decorator class for status-based message formatting."""
    def __init__(self):
        self.PASS = Style.BRIGHT + Fore.GREEN + "[ SUCCESS ]" + Style.RESET_ALL
        self.FAIL = Style.BRIGHT + Fore.RED + "[ FAILURE ]" + Style.RESET_ALL
        self.WARN = Style.BRIGHT + Fore.YELLOW + "[ WARNING ]" + Style.RESET_ALL
        self.HEAD = Style.BRIGHT + Fore.CYAN + "[ SECTION ]" + Style.RESET_ALL
        self.CMDL = Style.BRIGHT + Fore.BLUE + "[ COMMAND ]" + Style.RESET_ALL
        self.STDS = "           "


class MessageDecorator(object):
    """Main decorator class to select between icon or status formatting."""
    def __init__(self, attr):
        ICON = IconicDecorator()
        STAT = StatusDecorator()
        if attr == "icon":
            self.PASS = ICON.PASS
            self.FAIL = ICON.FAIL
            self.WARN = ICON.WARN
            self.HEAD = ICON.HEAD
            self.CMDL = ICON.CMDL
            self.STDS = ICON.STDS
        elif attr == "stat":
            self.PASS = STAT.PASS
            self.FAIL = STAT.FAIL
            self.WARN = STAT.WARN
            self.HEAD = STAT.HEAD
            self.CMDL = STAT.CMDL
            self.STDS = STAT.STDS

    def SuccessMessage(self, RequestMessage):
        """Print a success message with the appropriate decorator."""
        print(self.PASS + " " + Style.RESET_ALL + RequestMessage)

    def FailureMessage(self, RequestMessage):
        """Print a failure message with the appropriate decorator."""
        print(self.FAIL + " " + Style.RESET_ALL + RequestMessage)

    def WarningMessage(self, RequestMessage):
        """Print a warning message with the appropriate decorator."""
        print(self.WARN + " " + Style.RESET_ALL + RequestMessage)

    def SectionMessage(self, RequestMessage):
        """Print a section header message with the appropriate decorator."""
        print(self.HEAD + " " + Fore.CYAN + Style.BRIGHT
              + RequestMessage + Style.RESET_ALL)

    def CommandMessage(self, RequestMessage):
        """Return a command message with the appropriate decorator."""
        return self.CMDL + " " + Style.RESET_ALL + RequestMessage

    def GeneralMessage(self, RequestMessage):
        """Print a general message with the appropriate decorator."""
        print(self.STDS + " " + Style.RESET_ALL + RequestMessage)
