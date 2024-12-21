from .BaseModel import Base
from sqlalchemy import String
from sqlalchemy.orm import mapped_column, Mapped, relationship

from typing import Optional

class AppUser(Base):
    __tablename__ = 'app_users'

    #column
    user_id: Mapped[int] = mapped_column(primary_key=True)
    email: Mapped[str] = mapped_column(String(100), nullable=False)
    pwd: Mapped[str] = mapped_column(String(100), nullable=False)
    name: Mapped[str] = mapped_column(String(25))
    phone_number: Mapped[Optional[str]] = mapped_column(String(20))
    image_url: Mapped[Optional[str]] = mapped_column(String(100), default='https://t3.ftcdn.net/jpg/05/70/71/06/360_F_570710660_Jana1ujcJyQTiT2rIzvfmyXzXamVcby8.jpg')

    def __repr__(self):
        return f"{self.name}___{self.image_url}"
    
    def as_dict(self):
        user = super().as_dict()
        # remove sensitive data
        del user['pwd']
        del user['user_id']
        return user


