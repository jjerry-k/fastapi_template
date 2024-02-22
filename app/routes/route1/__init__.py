import traceback
from fastapi import APIRouter, HTTPException, Depends, UploadFile, File, Form, status
from typing import Annotated, List
from pydantic import Json

from model import MultipleRequest, ComplexRequest, ComplexResponse
from func import *

router = APIRouter(
    prefix="/route1",
    tags=["Route1"]
)

@router.post("/func")
async def func1():
    try:
        return {"content":"func1"}
    except:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, 
                            detail=str(traceback.format_exc()))
        
@router.post("/image")
async def func2(
                file: Annotated[bytes, File()]
                ):
    try:
        if not file:
            return {"message": "No file sent"}
        else:
            return {"file_size": len(file)}
    except:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, 
                            detail=str(traceback.format_exc()))
        
@router.post("/text")
async def func3(
            text: Annotated[str, Form()]
                ):
    try:
        return {"text": text}
    except:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, 
                            detail=str(traceback.format_exc()))

@router.post("/multi")
async def func4(
                file: Annotated[List[UploadFile], File()],
                requests: Annotated[MultipleRequest, Form]):
    try:
        print(requests)
        return {"text": "text"}
    except:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, 
                            detail=str(traceback.format_exc()))
        
@router.post("/complex", response_model=ComplexResponse)
async def func4(
                file: Annotated[bytes, File()],
                request: ComplexRequest
                ):
    try:
        response = {
            "out1": request.in2,
            "out2": [{"tmp1": len(file), 
                      "tmp2": 2.3,
                      "tmp3": request.in1, 
                      "tmp4": True,
                      "tmp5": [{"key": "test", "value": 2.3}, {"key": "test", "value": 2.3}],
                      "tmp6": {"Number": 23, "Message": "test"}}],
            "out3": {"temp":"temp"},
            "out4": ["asd", "asdasd"]
        }
        return response
    except:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, 
                            detail=str(traceback.format_exc()))