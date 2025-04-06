from sqlalchemy import String, Column, Integer, ForeignKey
from database import Base


class URLS(Base):
    __tablename__="urls"
    id = Column(Integer, primary_key=True, index=True)
    org_url = Column(String)
    shortcode = Column(String, unique=True)
