from typing import Optional, List, Union

from pydantic import BaseModel


class InternalBaseSchema(BaseModel):
    pass


class InternalPaginationBaseSchema(BaseModel):
    page_no: int
    page_size: int
    total_num: int
    page_data: Optional[List[InternalBaseSchema]] = []


class InternalBaseResponse(BaseModel):
    code: str
    message: str
    data: Optional[Union[InternalBaseSchema, InternalPaginationBaseSchema]] = None
