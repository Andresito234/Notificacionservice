from abc import ABC, abstractmethod
from typing import List, Optional
from .entities import Notification

class NotificationRepository(ABC):
    
    @abstractmethod
    def create_notification(self, notification: Notification) -> Notification:
        pass

    @abstractmethod
    def get_notifications_by_user(self, user_id: str) -> List[Notification]:
        pass

    @abstractmethod
    def mark_as_read(self, notification_id: str) -> Optional[Notification]:
        pass