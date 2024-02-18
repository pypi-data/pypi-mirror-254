class Response():
    error: bool
    error_text: str
    response: str
    status: int

    def __init__(self, error=False, error_text='', response='', status=0) -> None:
        self.error = error
        self.error_text = error_text
        self.response = response
        self.status = status
