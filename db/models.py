from sqlalchemy import Float, Integer, String
from sqlalchemy.orm import Mapped, declarative_base, mapped_column

Base = declarative_base()


class FreelancerEarnings(Base):
    """
    Модель БД для загрузки данных с .csv файла
    """

    __tablename__ = "freelancer_earnings_table"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    freelancer_id: Mapped[int] = mapped_column(Integer, nullable=False)
    job_category: Mapped[str] = mapped_column(String, nullable=False)
    platform: Mapped[str] = mapped_column(String, nullable=False)
    experience_level: Mapped[str] = mapped_column(String, nullable=False)
    client_region: Mapped[str] = mapped_column(String, nullable=False)
    payment_method: Mapped[str] = mapped_column(String, nullable=False)
    job_completed: Mapped[int] = mapped_column(Integer, nullable=False)
    earnings_usd: Mapped[int] = mapped_column(Integer, nullable=False)
    hourly_rate: Mapped[float] = mapped_column(Float, nullable=False)
    job_success_rate: Mapped[float] = mapped_column(Float, nullable=False)
    client_rating: Mapped[float] = mapped_column(Float, nullable=False)
    job_duration_days: Mapped[int] = mapped_column(Integer, nullable=False)
    project_type: Mapped[str] = mapped_column(String, nullable=False)
    rehire_rate: Mapped[float] = mapped_column(Float, nullable=False)
    marketing_spend: Mapped[int] = mapped_column(Integer, nullable=False)
