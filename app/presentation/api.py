from fastapi import FastAPI, HTTPException
from app.presentation.schemas import NotificationCreate, NotificationResponse
from app.use_cases.create_notification import create_notification
from app.use_cases.get_notifications import get_notifications
from app.use_cases.mark_as_read import mark_as_read

app = FastAPI()

@app.post("/notifications", response_model=NotificationResponse)
async def create_notification_endpoint(notification: NotificationCreate):
    return await create_notification(notification)

@app.get("/notifications/{user_id}", response_model=list[NotificationResponse])
async def get_notifications_endpoint(user_id: int):
    notifications = await get_notifications(user_id)
    if notifications is None:
        raise HTTPException(status_code=404, detail="Notifications not found")
    return notifications

@app.put("/notifications/{id}/read")
async def mark_as_read_endpoint(id: int):
    success = await mark_as_read(id)
    if not success:
        raise HTTPException(status_code=404, detail="Notification not found")
    return {"message": "Notification marked as read"}

@app.get("/health")
async def health_check():
    return {"status": "healthy"}