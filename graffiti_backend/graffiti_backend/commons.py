from enum import Enum

class HTTPMethod(Enum):
    POST = 'POST'
    PUT = 'PUT'
    GET = 'GET'
    DELETE = 'DELETE'

class GraffitiBackendMethod(Enum):
    CREATE = 'create'
    UPDATE = 'update'
    READ = 'read'
    DELETE = 'delete'

class GraffitiOption(Enum):
    INFO = 'info'
    OVERVIEW = 'overview'
    DETAIL = 'detail'
    MODIFY = 'modify'
    #LISTING = 'listing'
    SEARCH = 'search'
    #LIKE = 'like'
    #DISLIKE = 'dislike'
    #ADD = 'add'
    #CONFIRM = 'confirm'
    #IGNORE = 'ignore'
    #UNFRIEND = 'unfriend'
