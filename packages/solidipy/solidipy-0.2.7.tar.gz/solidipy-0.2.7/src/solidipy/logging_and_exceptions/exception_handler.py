# /utilities/exception/exception_handler.py

""" Exception handler class definition. """

from logging import Logger
from typing import NoReturn, Union

from solidipy.logging_and_exceptions.exception_values import GENERIC_ERROR_DICT, MASTER_EXCEPTION_DICT
from solidipy.logging_and_exceptions.logger import BaseLogger, solidipy_logger as sl


class ExceptionHandler:
	""" Base class for handling exceptions. """

	def __init__(
		self, new_logger: Union[Logger, BaseLogger, None] = None
	):
		"""
		Initializer for the ExceptionHandler class.

		:param new_logger: Instance of a logger class.
		"""
		self.logger = new_logger

	def get_exception_log(self, exception) -> dict:
		"""
		Method for assembling and logging exception information.

		:param exception: Exception object that was raised.
		:return: Formatted dictionary log of exception that occurred.
		"""
		exception_dict: dict = self.__get_exception_dict(exception)

		if self.logger is not None:
			self.__log_exception(exception.__class__.__name__, exception_dict)
		return exception_dict

	@classmethod
	def __get_exception_dict(cls, exception) -> dict:
		"""
		Method for retrieving the exception dictionary for a given exception.

		:param exception: Exception that occurred.
		:return: The requested dictionary of mapped exception values or a
			generic error dictionary if the key is not found.
		"""
		queried_dict: dict = MASTER_EXCEPTION_DICT.get(
			exception.__class__.__name__, GENERIC_ERROR_DICT
		)
		if len(exception.args) > 0 and len(exception.args[0]):
			queried_dict["Message"] = exception.args[0]
		else:
			queried_dict.pop("Message", None)

		return queried_dict

	def __log_exception(self, exception_name: str, exception_dict: dict) -> NoReturn:
		"""
		Method that formats a log and then logs it.
		:param exception_name: The name of the exception that occurred.
		:param exception_dict: Exception dictionary to be logged.
		"""

		log: str = (
			f"A {exception_name} occurred:\n{exception_dict}\n"
		)
		max_length = max(len(line) for line in log.split('\n'))
		divider: str = "=" * max_length
		log = f"\n{divider}\n\n{log}\n{divider}\n"
		self.logger.log_exception(log)  # noqa


solidipy_exception_handler: ExceptionHandler = ExceptionHandler(sl)
"""
Universal exception handling object for operations across the package.
Not intended for use outside of the package.
"""
