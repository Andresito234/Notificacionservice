from sqlalchemy.orm import Session
from app.domain.entities import Notification
from app.domain.repositories import NotificationRepository

class SQLAlchemyNotificationRepository(NotificationRepository):
    def __init__(self, db: Session):
        self.db = db

    def create_notification(self, notification: Notification) -> Notification:
        self.db.add(notification)
        self.db.commit()
        self.db.refresh(notification)
        return notification

    def get_notifications_by_user(self, user_id: int) -> list[Notification]:
        return self.db.query(Notification).filter(Notification.user_id == user_id).all()

    def mark_as_read(self, notification_id: int) -> Notification:
        notification = self.db.query(Notification).filter(Notification.id == notification_id).first()
        if notification:
            notification.read_status = True
            self.db.commit()
            self.db.refresh(notification)
        return notification