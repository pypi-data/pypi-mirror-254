# /utilities/validation.py

""" Module for validation helpers. """

from importlib.util import find_spec

PYDANTIC_AVAILABLE: bool = find_spec("pydantic") is not None
FLASK_AVAILABLE: bool = find_spec("flask") is not None

if PYDANTIC_AVAILABLE:
	from typing import Any, Callable, Optional, TypeVar, Union

	from pydantic import BaseModel, ValidationError, model_validator
	from pydantic_core import PydanticCustomError

	wrapped_func = TypeVar("wrapped_func", bound=Callable[..., Any])
	""" TypeVar used for a wrapped function. """


	class CustomValidationError(Exception):
		"""
		Custom error class used to handle Pydantic validation errors that are
		outside the scope of the library's functionality.
		"""

		def __init__(
				self,
				error_type: str,
				msg: str,
				loc: Optional[tuple] = None,
				user_input: Optional[Any] = None,
				error_code: Optional[int] = None,
		):
			"""
			CustomValidationError initialization method.

			:param error_type: The type of error that occurred.
			:param msg: The message associated with the error.
			:param loc: The field of distress.
			:param user_input: The user input that caused the error.
			"""

			self.error: dict = {
				"type": error_type,
				"msg": msg,
			}

			if loc is not None:
				self.error["loc"] = loc

			if user_input is not None:
				self.error["input"] = user_input

			if error_code is not None:
				self.error["response_code"] = error_code

		def errors(self):
			"""
			Method that mirrors the Pydantic.ValidationError.errors() method.
			:return: A list containing the error dictionary.
			"""

			return [self.error]


	class ValidationErrorHandler:
		"""
		Houses methods to parse Pydantic validation errors into formatted dictionaries.
		"""
		validation_error_types = Union[ValidationError, PydanticCustomError, CustomValidationError]
		""" Type hint for all valid Pydantic validation error types. """

		def __init__(self, validation_exception: validation_error_types):
			"""
			Initialization method.

			:param validation_exception: Dictionary representation of a Pydantic validation error.
			"""

			self.error: dict = self.__parse_error(validation_exception)

		def __parse_error(self, validation_exception: validation_error_types) -> dict:
			"""
			Pydantic validation error handler function. Deconstructs Pydantic
			Validation errors into error dictionaries.

			:param validation_exception: A Pydantic validation error.
			:return: A dictionary containing the error type and error message.
			"""

			# Get the list of errors
			error_list: list = validation_exception.errors()
			# Extract the first error from the list of errors.
			validation_error: dict = error_list[0]
			# Extract the error type.
			error_type: str = validation_error.get("type")
			# Extract the error field of distress, user input, & error message
			# from the error or None if the location is not present in the validation error.
			field_of_distress: Optional[str] = self.__unpack_location(validation_error.get("loc"))
			# If a field is missing, there will be no user input, so substitute a
			# None value to show that no value was provided for the field of distress.
			user_input: str = validation_error.get("input", "") if error_type != "missing" else None

			response_code: int = validation_error.get("response_code")

			error_response_dict: dict = {
				"Type": error_type.replace("_", " "),
				"Message": validation_error.get("msg", ""),
				"User Input": user_input
			}

			if field_of_distress:
				error_response_dict["Field of Distress"] = field_of_distress

			if response_code is not None:
				error_response_dict["Response Code"] = response_code
			return error_response_dict

		@classmethod
		def __unpack_location(cls, location: Optional[tuple]) -> Optional[str]:
			"""
			Unpacks the location tuple into a string.  Reading from left to right,
			it will unpack the tuple into a string that looks like:
			('type', 0, 'name') -> type[0][name]

			:param location: Tuple containing the location of the error.
			:return: String containing the location of the error or None if the location isn't specified.
			"""

			# If the location tuple is empty, the error occurred on behalf of an erroneously empty payload.
			if location is None:
				return location

			unpacked_location: str = ""
			for attribute in location:
				unpacked_location = (
					attribute if not unpacked_location else unpacked_location + f"[{attribute}]"
				)

			return unpacked_location

	if FLASK_AVAILABLE:

		class NoRequestBody(BaseModel):
			""" Pydantic request model for a request with no body. """

			@model_validator(mode="before")
			def validate_empty_request_body(cls, request_payload: dict) -> dict:
				"""
				Pydantic model validator to ensure that the request body is empty.

				:param request_payload:
				:return:
				"""

				if bool(request_payload):
					raise CustomValidationError(
						"Unexpected request data",
						"Empty JSON payload expected.",
						("Request body",),
					)

				return request_payload
