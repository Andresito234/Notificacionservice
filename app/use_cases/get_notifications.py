from app.domain.repositories import NotificationRepository
from app.domain.entities import Notification
from typing import List

class GetNotifications:
    def __init__(self, repository: NotificationRepository):
        self.repository = repository

    def execute(self, user_id: int) -> List[Notification]:
        return self.repository.get_notifications_by_user(user_id)