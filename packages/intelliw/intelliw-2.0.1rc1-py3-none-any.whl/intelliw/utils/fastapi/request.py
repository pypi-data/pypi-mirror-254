class IntelliwDict(dict):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.get_dict = None


class Request:
    """
    intelliw server request
    """

    def __init__(self) -> None:
        self.header = None
        self.json = ""
        self.query = {}
        self.form = IntelliwDict()
        self.files = {}
        self.body = ""
        self.batch_params = {}
        self.context = None
