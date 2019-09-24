# from sqlalchemy import Boolean, Column, Integer, String, DateTime
# import datetime
# from app.db.base_class import Base
# from app.db.session import engine

# class Device(Base):
#     id = Column(Integer, primary_key=True, index=True)
#     fqdn = Column(String, index=True)
#     name = Column(String, unique=True, index=True)
#     serial = Column(String)
#     management_ip = Column(String)
#     created_at = Column(DateTime, default=datetime.datetime.now)
#     updated_at = Column(DateTime, default=datetime.datetime.now)

# Base.metadata.create_all(bind=engine)