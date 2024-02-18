# Copyright 2023 Wirepas Ltd licensed under Apache License, Version 2.0
#
# See file LICENSE for full license details.
#
from typing import Any
from .error_code_enum import ErrorCodeEnum


class Response:
    """ Response object containing the meter response informations.

    * error_code: Error code of the response to know whether the response is valid.
    * xml: String representation in xml of the message.
    * payload: Payload in bytes of the meter response.
    * value: Value parsed from the response.

    Note: If the data content of the response is an enumerate or a result code, \
          it can not be parsed as data content, and the value should be set to None.
    """
    def __init__(self, error_code: ErrorCodeEnum, xml: str, payload: bytes, value: Any = None):
        self.error_code = error_code
        self.xml = xml
        self.payload = payload
        self.value = value
