from sqlalchemy import Column, Integer, String, DateTime, Enum
from sqlalchemy.dialects.postgresql import UUID
import datetime
from app.db.base_class import Base
from app.db.session import engine
from app.models.rule import ProtocolName, ActionName
from uuid import uuid4


class Rule(Base):
    id = Column(UUID(as_uuid=True),
                primary_key=True,
                default=uuid4,)
    src_ip = Column(String, nullable=True)
    src_zone = Column(String, nullable=True)
    dst_ip = Column(String, nullable=True)
    dst_zone = Column(String, nullable=True)
    protocol = Column(Enum(ProtocolName))
    port = Column(Integer, nullable=True)
    action = Column(Enum(ActionName))

    created_at = Column(DateTime, default=datetime.datetime.now)
    updated_at = Column(DateTime, default=datetime.datetime.now)


Base.metadata.create_all(bind=engine)
