"""
TODO
"""


class RESTObject(object):

    operation = "get"
    endpoint: str = None
    params: dict = {}
    headers: dict = {}
    payload: str = ""

    def __init__(self, **kwargs) -> None:
        self.__dict__.update(kwargs)
