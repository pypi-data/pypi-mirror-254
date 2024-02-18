# /utilities/string_utilities.py

""" Module for utility functions related to string operations. """

import base64
import binascii
import json
import random
import string
from os import environ, urandom
from re import Match, Pattern, compile
from string import ascii_uppercase, digits

from solidipy.logging_and_exceptions.exception_values import EXCEPTION_TUPLE
from solidipy.logging_and_exceptions.logger import solidipy_logger


def get_os_variable(os_environ_key: str) -> str:
	"""
	Utility function for returning an OS environment variable if it exists.

	:param os_environ_key: The OS variable key.
	:return: The value of the OS variable or an empty string if the key doesn't exist.
	"""

	if not isinstance(os_environ_key, str):
		raise ValueError("Input must be a string.")

	os_environ_value: str = environ.get(os_environ_key, "")

	if os_environ_value == "":
		solidipy_logger.log_exception(f"Could not get `{os_environ_key}` from os.")

	return os_environ_value


def is_regex_pattern_match(regex_pattern: str, value: str) -> bool:
	"""
	Utility function for conducting a regex match against a string value.

	:param regex_pattern: The regular expression pattern used to conduct the evaluation.
	:param value: The string value to be evaluated.
	:return: Result of the regular expression evaluation on the string value.
	"""

	if not (len(regex_pattern) >= 1 and len(value) > 0):
		raise ValueError("Both inputs must be non-empty strings.")

	regex: Pattern = compile(regex_pattern)
	match: Match = regex.match(value)
	return match is not None


def reformat_string(original_value: str, pattern: str, replacement: str) -> str:
	"""
	Utility function for reformatting a string.

	:param original_value: The value to be reformatted.
	:param pattern: The pattern to match and replace.
	:param replacement: The pattern to replace the original with.
	:return: Reformatted string based upon the parameter inputs.
	"""

	if not (isinstance(original_value, str) and isinstance(pattern, str) and isinstance(replacement, str)):
		raise ValueError("All inputs must be non-empty strings.")

	compiled_pattern: Pattern = compile(pattern)
	return compiled_pattern.sub(replacement, original_value)


def get_random_uuid(num_chars: int) -> str:
	"""
	Utility function for returning a UUID of a specified length.
	UUID format is upper case letters and numbers only.

	:param num_chars: Length of the random UUID.
	:return: A UUID of the specified length.
	"""

	if not isinstance(num_chars, int) or num_chars <= 0:
		raise ValueError("Input must be integer greater than 0.")

	random_uuid: str = ''.join(
		random.choices(ascii_uppercase + digits, k=num_chars)
	)
	return random_uuid


def generate_hex_bytes_as_string(num_bytes: int) -> str:
	"""
	Utility function for generating bytes in hexadecimal format and returning them as a string.

	:param num_bytes: The number of bytes that the hexadecimal value is supposed to be.
	:return: String representation of the newly generated hexadecimal byte value.
	"""

	if not isinstance(num_bytes, int) or num_bytes <= 0:
		raise ValueError("Input must be integer greater than 0.")

	random_bytes: bytes = urandom(num_bytes)
	hex_value: str = binascii.hexlify(random_bytes).decode()
	return hex_value


def base64_decode_string(b64_encoding: str) -> str:
	"""
	Utility function for decoding a base64 encoded string.

	:param b64_encoding: Base64 encoded string value to be decoded and converted back to a string.
	:return: Base64 decoded key on success or an empty string on failure.
	"""

	if not isinstance(b64_encoding, str) or not b64_encoding:
		raise ValueError("Input must be a non-empty string.")

	decoded_string: str = ""

	try:
		decoded_bytes: bytes = base64.b64decode(b64_encoding)
		decoded_string = decoded_bytes.decode().strip()

	except EXCEPTION_TUPLE as exc:
		solidipy_logger.log_exception(f"Could not base64 decode string:\n{b64_encoding}\n\n{exc}")

	return decoded_string


def get_base64_string_from_dict(dict_to_encode: dict) -> str:
	"""
	Utility function for returning a dictionary as a base64 encoded string.

	:param dict_to_encode: Input dictionary that will be converted to a string and baser64 encoded.
	:return: Base64 encoded string value.
	"""

	if not isinstance(dict_to_encode, dict):
		raise ValueError("Input must be a dictionary.")

	encoded_string: str = ""

	try:
		string_to_encode: str = json.dumps(dict_to_encode)
		encoded_bytes: bytes = base64.b64encode(string_to_encode.encode())
		encoded_string = encoded_bytes.decode()

	except EXCEPTION_TUPLE as exception:
		solidipy_logger.log_exception(
			f"Could not base64 encode supplied dictionary:\n{exception}"
		)

	return encoded_string


def get_hex_encoded_str(value: str) -> str:
	"""
	Utility function for hexadecimal encoding a string.

	:param value: String to encode.
	:return: Encoded string if legitimate encoding or an empty string if an error occurred.
	"""

	if not isinstance(value, str):
		raise ValueError("Input must be a string.")

	encoded_str: str = ""

	try:
		encoded_bytes: bytes = binascii.hexlify(value.encode())
		encoded_str = encoded_bytes.decode()

	except EXCEPTION_TUPLE as exception:
		solidipy_logger.log_exception(
			f"Could not hex encode string: `{value}`\n\n{exception}"
		)

	return encoded_str


def generate_alphanumeric_str(size: int) -> str:
	"""
	Utility function for generating a random alphanumeric string of a specified size.

	:param size: The number of characters to generate.
	:return: Random alphanumeric string.
	"""

	if not isinstance(size, int) or size <= 0:
		raise ValueError("Input must be an integer with a value greater than 0.")

	generated_string: str = ''.join(
		random.choices(
			(
					string.ascii_uppercase +
					string.ascii_lowercase +
					string.digits
			),
			k=size
		)
	)

	return generated_string
