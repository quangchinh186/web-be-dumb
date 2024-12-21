class BaseService():
    NOT_FOUND_ERROR = {'status': '404 NOT FOUND'}
    SUCCESS = {'status': 'SUCCESS'}
    FORBIDDEN_ERROR = {'status': '403 FORBIDDEN'}
    AUTH_REQUIRED = {'status': '401 UNAUTHORIZED'}