# coding: utf-8

"""
    FINBOURNE Luminesce Web API

    FINBOURNE Technology  # noqa: E501

    Contact: info@finbourne.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""


from __future__ import annotations
import pprint
import re  # noqa: F401
import json


from typing import Any, Dict, Optional
from pydantic import BaseModel, Field, StrictStr
from luminesce.models.link import Link

class BackgroundQueryResponse(BaseModel):
    """
    Response for Background Query Start requests  # noqa: E501
    """
    execution_id: Optional[StrictStr] = Field(None, alias="executionId", description="ExecutionId of the started-query")
    progress: Optional[Link] = None
    cancel: Optional[Link] = None
    fetch_json: Optional[Link] = Field(None, alias="fetchJson")
    fetch_json_proper: Optional[Link] = Field(None, alias="fetchJsonProper")
    fetch_xml: Optional[Link] = Field(None, alias="fetchXml")
    fetch_parquet: Optional[Link] = Field(None, alias="fetchParquet")
    fetch_csv: Optional[Link] = Field(None, alias="fetchCsv")
    fetch_pipe: Optional[Link] = Field(None, alias="fetchPipe")
    fetch_excel: Optional[Link] = Field(None, alias="fetchExcel")
    fetch_sqlite: Optional[Link] = Field(None, alias="fetchSqlite")
    histogram: Optional[Link] = None
    __properties = ["executionId", "progress", "cancel", "fetchJson", "fetchJsonProper", "fetchXml", "fetchParquet", "fetchCsv", "fetchPipe", "fetchExcel", "fetchSqlite", "histogram"]

    class Config:
        """Pydantic configuration"""
        allow_population_by_field_name = True
        validate_assignment = True

    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.dict(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> BackgroundQueryResponse:
        """Create an instance of BackgroundQueryResponse from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of progress
        if self.progress:
            _dict['progress'] = self.progress.to_dict()
        # override the default output from pydantic by calling `to_dict()` of cancel
        if self.cancel:
            _dict['cancel'] = self.cancel.to_dict()
        # override the default output from pydantic by calling `to_dict()` of fetch_json
        if self.fetch_json:
            _dict['fetchJson'] = self.fetch_json.to_dict()
        # override the default output from pydantic by calling `to_dict()` of fetch_json_proper
        if self.fetch_json_proper:
            _dict['fetchJsonProper'] = self.fetch_json_proper.to_dict()
        # override the default output from pydantic by calling `to_dict()` of fetch_xml
        if self.fetch_xml:
            _dict['fetchXml'] = self.fetch_xml.to_dict()
        # override the default output from pydantic by calling `to_dict()` of fetch_parquet
        if self.fetch_parquet:
            _dict['fetchParquet'] = self.fetch_parquet.to_dict()
        # override the default output from pydantic by calling `to_dict()` of fetch_csv
        if self.fetch_csv:
            _dict['fetchCsv'] = self.fetch_csv.to_dict()
        # override the default output from pydantic by calling `to_dict()` of fetch_pipe
        if self.fetch_pipe:
            _dict['fetchPipe'] = self.fetch_pipe.to_dict()
        # override the default output from pydantic by calling `to_dict()` of fetch_excel
        if self.fetch_excel:
            _dict['fetchExcel'] = self.fetch_excel.to_dict()
        # override the default output from pydantic by calling `to_dict()` of fetch_sqlite
        if self.fetch_sqlite:
            _dict['fetchSqlite'] = self.fetch_sqlite.to_dict()
        # override the default output from pydantic by calling `to_dict()` of histogram
        if self.histogram:
            _dict['histogram'] = self.histogram.to_dict()
        # set to None if execution_id (nullable) is None
        # and __fields_set__ contains the field
        if self.execution_id is None and "execution_id" in self.__fields_set__:
            _dict['executionId'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> BackgroundQueryResponse:
        """Create an instance of BackgroundQueryResponse from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return BackgroundQueryResponse.parse_obj(obj)

        _obj = BackgroundQueryResponse.parse_obj({
            "execution_id": obj.get("executionId"),
            "progress": Link.from_dict(obj.get("progress")) if obj.get("progress") is not None else None,
            "cancel": Link.from_dict(obj.get("cancel")) if obj.get("cancel") is not None else None,
            "fetch_json": Link.from_dict(obj.get("fetchJson")) if obj.get("fetchJson") is not None else None,
            "fetch_json_proper": Link.from_dict(obj.get("fetchJsonProper")) if obj.get("fetchJsonProper") is not None else None,
            "fetch_xml": Link.from_dict(obj.get("fetchXml")) if obj.get("fetchXml") is not None else None,
            "fetch_parquet": Link.from_dict(obj.get("fetchParquet")) if obj.get("fetchParquet") is not None else None,
            "fetch_csv": Link.from_dict(obj.get("fetchCsv")) if obj.get("fetchCsv") is not None else None,
            "fetch_pipe": Link.from_dict(obj.get("fetchPipe")) if obj.get("fetchPipe") is not None else None,
            "fetch_excel": Link.from_dict(obj.get("fetchExcel")) if obj.get("fetchExcel") is not None else None,
            "fetch_sqlite": Link.from_dict(obj.get("fetchSqlite")) if obj.get("fetchSqlite") is not None else None,
            "histogram": Link.from_dict(obj.get("histogram")) if obj.get("histogram") is not None else None
        })
        return _obj
