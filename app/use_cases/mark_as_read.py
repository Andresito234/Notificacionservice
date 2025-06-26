from app.domain.repositories import NotificationRepository
from app.domain.entities import Notification
from pydantic import BaseModel
from fastapi import HTTPException

class MarkAsReadRequest(BaseModel):
    user_id: int

async def mark_as_read(notification_id: int, request: MarkAsReadRequest, repository: NotificationRepository):
    notification = await repository.get_notification_by_id(notification_id)
    
    if not notification:
        raise HTTPException(status_code=404, detail="Notification not found")
    
    if notification.user_id != request.user_id:
        raise HTTPException(status_code=403, detail="Not authorized to mark this notification as read")
    
    notification.read_status = True
    await repository.update_notification(notification)