class Response():
    error: bool
    error_text: str
    response: str
    status: int
    outbound: str

    def __init__(self, error=False, error_text='', response='', status=0, outbound='') -> None:
        self.error = error
        self.error_text = error_text
        self.response = response
        self.status = status
        self.outbound = outbound
