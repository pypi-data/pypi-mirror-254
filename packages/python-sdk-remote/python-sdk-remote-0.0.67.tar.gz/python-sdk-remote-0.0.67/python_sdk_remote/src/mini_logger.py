import sys
from datetime import datetime


class MiniLogger:
    # TODO Can we so one generic function call by all
    # TODO Shall we user the Python logging package?

    @staticmethod
    def start(message: str = "", object: dict = None):
        """
        Print a log message with the current time.

        Parameters:
            message (str): The message to be printed.
        """
        if object is None:
            print(f"{datetime.now()} - START - {message}")
        else:
            print(f"{datetime.now()} - START - {message} - {object}")

    @staticmethod
    def end(message: str = "", object: dict = None):
        """
        Print a log message with the current time.

        Parameters:
            message (str): The message to be printed.
        """
        if object is None:
            print(f"{datetime.now()} - END - {message}")
        else:
            print(f"{datetime.now()} - END - {message} - {object}")

    @staticmethod
    def info(message: str = "", object: dict = None):
        """
        Print a log message with the current time.

        Parameters:
            message (str): The message to be printed.
            object (dict): The object to be printed.
        """
        if object is None:
            print(f"{datetime.now()} - INFO - {message}")
        else:
            print(f"{datetime.now()} - INFO {message} - {object}")

    @staticmethod
    def warning(message: str = "", object: dict = None):
        """
        Print a log message with the current time.

        Parameters:
            message (str): The message to be printed.
            object (dict): The object to be printed.
        """
        if object is None:
            print(f"{datetime.now()} - WARNING - {message}")
        else:
            print(f"{datetime.now()} - WARNING {message} - {object}")

    @staticmethod
    def error(message: str = "", object: dict = None):
        """
        Print a log error message with the current time.

        Parameters:
            message (str): The message to be printed.
            object (dict): The object to be printed.
        """
        if object is None:
            print(f"{datetime.now()} - ERROR - {message}", file=sys.stderr)
        else:
            print(
                f"{datetime.now()} - ERROR - {message} - {object}", file=sys.stderr)

    @staticmethod
    def exception(message: str = "", object: Exception | dict = None):
        """
        Print a log error message with the current time.

        Parameters:
            message (str): The message to be printed.
            object (dict / Exception): The object / Exception to be printed.
        """
        if object is None:
            print(f"{datetime.now()} - EXCEPTION - {message}", file=sys.stderr)
        else:
            print(
                f"{datetime.now()} - EXCEPTION- {message} - {object}", file=sys.stderr)
