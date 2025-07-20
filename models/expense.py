from sqlalchemy import Column, Integer, String, Float, Date
from db.database import Base

class Expense(Base):
    __tablename__ = "expenses"

    id = Column(Integer, primary_key=True, index=True)
    date = Column(Date)
    category = Column(String)
    amount = Column(Float)
    description = Column(String, nullable=True)