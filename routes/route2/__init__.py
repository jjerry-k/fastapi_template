import traceback
from fastapi import APIRouter, HTTPException, Depends, File, Form, status
from typing import Annotated, List

from func import *

router = APIRouter(
    prefix="/route2",
    tags=["Route2"], 
    dependencies=[Depends(check_credential)]
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