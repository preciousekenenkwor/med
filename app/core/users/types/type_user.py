
from dataclasses import dataclass, field
from datetime import datetime
from enum import Enum
from typing import NotRequired, Optional, TypedDict


@dataclass
class UserD:
    id: str

    first_name: str
    last_name: str
    username: str
    email: str
    password: str
    
    remember_token: str
    deleted_at: datetime
    created_at: datetime 
    updated_at: datetime 
    
   
    
    allow_login: bool
    user_type:str
    gender:str


class UserT(TypedDict, ):
    id: str

    first_name: str
    last_name: str
    username: str
    email: str
    password: str


    signup_type: str # Either 'email' or 'phone' GOOGLE or FACEBOOK
    remember_token: str
    deleted_at: datetime
    created_at: datetime 
    updated_at: datetime 
    
   
 
    allow_login: bool
    user_type:str
    gender:str
class CreateUserT(TypedDict ):


    first_name: str
    last_name: str
    email: str
    password: str


@dataclass    
class CreateUserD:


    first_name: str
    last_name: str
    email: str
    password: str


    
class UpdateUserT(TypedDict ):
    first_name: str
    last_name: str
    username: NotRequired[str]

    language: NotRequired[str]
    remember_token: NotRequired[str]

    gender:NotRequired[str]

    
class GenderE(Enum):
    MALE = "male"
    FEMALE = "female"
    OTHER = "other"

class UserTypeE(Enum):
    PATIENT = "PATIENT",
    ADMIN="ADMIN",
    DOCTOR="DOCTOR"
