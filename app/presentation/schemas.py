from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime

class NotificationBase(BaseModel):
    user_id: int
    message: str

class NotificationCreate(NotificationBase):
    pass

class Notification(NotificationBase):
    id: int
    read_status: bool
    created_at: datetime

    class Config:
        orm_mode = True

class NotificationList(BaseModel):
    notifications: List[Notification]