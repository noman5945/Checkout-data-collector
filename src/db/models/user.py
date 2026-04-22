from sqlalchemy import Column,String,Enum,text,DateTime
from sqlalchemy.dialects.postgresql import UUID
from core.database import Base
import enum
from datetime import datetime

# ENUMS
class UserStatus(str, enum.Enum):
    activated = "activated"
    deactivated = "deactivated"


class UserType(str, enum.Enum):
    admin = "admin"
    user = "agent"


class User(Base):
    __tablename__="users"

    user_id = Column(
        UUID(as_uuid=True),
        primary_key=True,
        server_default=text("gen_random_uuid()")
    )

    user_email = Column(
        String,
        unique=True,
        nullable=False
    )

    user_password = Column(
        String,
        nullable=False
    )

    user_active_status = Column(
        Enum(UserStatus),
        nullable=False,
        default=UserStatus.activated
    )

    user_type = Column(
        Enum(UserType),
        nullable=False
    )

    created_at = Column(DateTime, default=datetime.utcnow)