from sqlalchemy import String
from sqlalchemy.orm import mapped_column, Mapped

from config.database import Base


class Brand(Base):
    __tablename__ = "brand"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(100))
