# coding: utf-8

"""
    FINBOURNE Luminesce Web API

    FINBOURNE Technology  # noqa: E501

    Contact: info@finbourne.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""


import json
import pprint
import re  # noqa: F401
from aenum import Enum, no_arg





class SourceType(str, Enum):
    """
    The file type of a source
    """

    """
    allowed enum values
    """
    UNKNOWN = 'Unknown'
    CSV = 'Csv'
    EXCEL = 'Excel'
    SQLITE = 'SqLite'
    XML = 'Xml'
    PARQUET = 'Parquet'
    RAWTEXT = 'RawText'

    @classmethod
    def from_json(cls, json_str: str) -> SourceType:
        """Create an instance of SourceType from a JSON string"""
        return SourceType(json.loads(json_str))
