from sqlalchemy import String, ForeignKey
from sqlalchemy.orm import mapped_column, Mapped

from config.database import Base


class CarModel(Base):
    __tablename__ = "model"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(100))
    brand_id: Mapped[int] = mapped_column(ForeignKey("brand.id"))
