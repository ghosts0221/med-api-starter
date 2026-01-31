from sqlalchemy import String, Integer
from sqlalchemy.orm import Mapped, mapped_column

from app.db.database import Base


class Patient(Base):
    __tablename__ = "patients"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    patient_code: Mapped[str] = mapped_column(String(50), unique=True, index=True)
    age: Mapped[int] = mapped_column(Integer)
    sex: Mapped[str] = mapped_column(String(10))  # e.g., "M", "F", "Other"
