# -*- coding:utf-8 -*-

from datetime import datetime
from typing import Any, Union, List, Optional
from pydantic import BaseModel


class Response(BaseModel):
    code: Optional[int] = 0
    msg: Optional[str] = "success"
    data: Optional[Any] = None


class GenerateBase(BaseModel):
    prompt: str
    mv: str
    title: str
    tags: str
    continue_at: Optional[str] = None
    continue_clip_id: Optional[str] = None




