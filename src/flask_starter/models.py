from flask_starter.extensions import db


class User(db.Model):  # type: ignore[name-defined]
    __tablename__ = "user"
    id = db.Column(db.String(), primary_key=True)
    name = db.Column(db.String(), nullable=False)

    def __init__(self, id: str, name: str) -> None:
        self.id = id
        self.name = name

    def serialize(self) -> dict:
        return {"id": self.id, "name": self.name}


"""

from datetime import datetime
from sqlalchemy import DateTime, Index

class Post(db.Model):  # type: ignore[name-defined]
    __tablename__ = "post"
    id = db.Column(db.String(), primary_key=True)
    user_id = db.Column(db.String(), db.ForeignKey("user.id"), nullable=False)
    created = db.Column(DateTime(timezone=True), nullable=False)
    title = db.Column(db.String(), nullable=False)
    body = db.Column(db.String(), nullable=False)

    def __init__(
        self,
        id: int,
        user_id: str,
        created: datetime,
        title: str,
        body: str,
    ) -> None:
        self.id = id
        self.author_id = user_id
        self.created = created
        self.title = title
        self.body = body

    __table_args__ = (
        Index(
            "ix_author_id",
            "author_id",
        ),
        Index(
            "ix_media_metadata_last_modified",
            "last_modified",
        ),
    )

    def serialize(self) -> dict:
        return {"id": self.id, "name": self.name}
"""
