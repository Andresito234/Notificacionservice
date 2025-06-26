class Notification:
    def __init__(self, id: int, user_id: int, message: str, read_status: bool, created_at: str):
        self.id = id
        self.user_id = user_id
        self.message = message
        self.read_status = read_status
        self.created_at = created_at

    def mark_as_read(self):
        self.read_status = True

    def __repr__(self):
        return f"<Notification(id={self.id}, user_id={self.user_id}, message='{self.message}', read_status={self.read_status}, created_at='{self.created_at}')>"