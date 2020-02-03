from enum import Enum

class UserType(Enum):
    PERSONAL_USER = 'personal_user'
    COMMERCIAL_USER = 'commerical_user'
    SUPER_USER = 'super_user'

class UserSearchIdentifier(Enum):
    USER_ID = 'id'
    USER_EMAIL = 'email'
    USERNAME = 'username'
