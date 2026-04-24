from sqlalchemy import Column,String,Enum,text,DateTime,ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from core.database import Base

class Agent(Base):
    __tablename__="agent"
    
    agent_id=Column(
        UUID(as_uuid=True),
        primary_key=True,
        server_default=text("gen_random_uuid()")
    )

    user_id=Column(
        UUID(as_uuid=True),
        ForeignKey("users.user_id"),
        nullable=False
    )

    agent_full_name=Column(
        String(50),
        nullable=False
    )

    contact_no=Column(
        String(12),
        nullable=False
    )

    work_location=Column(
        String(50),
        nullable=False
    )

    profile_picture=Column(
        String(50),
        nullable=False
    )

    created_at = Column(
        DateTime,
        server_default=text("now()"),
        nullable=False
    )


