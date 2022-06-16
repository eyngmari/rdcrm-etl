from sqlalchemy import Column
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.types import (
    Integer, String, Boolean, DateTime, Float
)


Base = declarative_base()


class Deal(Base):
    __tablename__ = "deals"

    id = Column(String(24), primary_key=True, unique=True, nullable=False)
    name = Column(String(255), nullable=True)
    contacts_email = Column(String(255), nullable=True)
    user_id = Column(String(24), nullable=True)
    user_name = Column(String(255), nullable=True)
    created_at = Column(DateTime)
    updated_at = Column(DateTime)
    deal_stage_id = Column(String(24), nullable=True)
    deal_stage_name = Column(String(255), nullable=True)
    contacts_phones = Column(String(255), nullable=True)
    deal_source_id = Column(String(24), nullable=True)
    deal_source_name = Column(String(255), nullable=True)
    deal_products_base_price = Column(Float())
    deal_products_id = Column(String(24), nullable=True)
    deal_products_name = Column(String(255), nullable=True)
    win = Column(Boolean(), nullable=True)
    rating = Column(Integer(), nullable=True)
    closed_at = Column(DateTime, nullable=True)

# from database import engine
# Base.metadata.create_all(engine)
