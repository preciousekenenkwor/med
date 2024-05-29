
from datetime import datetime
from typing import TYPE_CHECKING

from sqlalchemy import (ARRAY, DATETIME, INTEGER, Boolean, DateTime, Enum,
                        Float, ForeignKey, Integer, String)
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.config.database.db import Base, TimeStamp
from app.core.users.types.type_user import GenderE, UserTypeE
from app.utils.uuid_generator import id_gen

if TYPE_CHECKING:
    from app.core.auth.models.model_token import TokenModel
    from app.core.notification.models.model_notification import \
        NotificationModel


# This class likely represents a user model with inheritance from Base and TimeStamp classes.
class UserModel(Base, TimeStamp):
    __tablename__ = "USER"
    id:Mapped[str] = mapped_column(
        String(255), primary_key=True, default=id_gen() , unique=True
    )
    first_name:Mapped[str]
    last_name:Mapped[str]
    password:Mapped[str] =mapped_column(String(255), nullable=False)
    email:Mapped[str]= mapped_column(String(255), unique=True, nullable=False)
    phone:Mapped[str] = mapped_column(String(255), unique=True, nullable=True)
    is_email_verified:Mapped[bool] = mapped_column(Boolean, default=False)
    
    deleted_at:Mapped[datetime] = mapped_column(DateTime, nullable=True)
    gender:Mapped[str]=mapped_column(Enum(GenderE), nullable=True)
    user_type:Mapped[str] = mapped_column(Enum(UserTypeE), default=UserTypeE.PATIENT)
    allow_login:Mapped[bool] = mapped_column(Boolean, default=True)
  


    #relationship
   
    user__token:Mapped["TokenModel"] = relationship(back_populates="token__user")
    # user__notification:Mapped["NotificationModel"] = relationship(back_populates="notification__user")


