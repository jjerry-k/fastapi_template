import json
from pydantic import BaseModel, Field, AliasChoices, model_validator
from typing import Any

class MultipleRequest(BaseModel):
    in1: list[str] # Require field
    in2: list[bool] # Require field
    
    @model_validator(mode='before')
    @classmethod
    def validate_to_json(cls, value: Any) -> Any:
        if isinstance(value, str):
            return cls(**json.loads(value))
        return value
    
class ComplexRequest(BaseModel):
    in1: str  # Require field
    in2: bool # Require field
    in3: bool | None = True # Default value
    in4: bool | None = False # Default value
    
    @model_validator(mode='before')
    @classmethod
    def validate_to_json(cls, value: Any) -> Any:
        if isinstance(value, str):
            return cls(**json.loads(value))
        return value
    
class Foo1(BaseModel):
    key: str
    value: float

class Foo2(BaseModel):
    num: int = Field(..., validation_alias=AliasChoices("Number", "num"))
    content: str = Field(..., validation_alias=AliasChoices("Message", "content"))
    
class Foo3(BaseModel):
    tmp1: int
    tmp2: float
    tmp3: str
    tmp4: bool
    tmp5: list[Foo1] | None = []
    tmp6: Foo2
    
class ComplexResponse(BaseModel):
    out1: bool
    out2: list[Foo3] | None = []
    out3: dict | None = None
    out4: list
    