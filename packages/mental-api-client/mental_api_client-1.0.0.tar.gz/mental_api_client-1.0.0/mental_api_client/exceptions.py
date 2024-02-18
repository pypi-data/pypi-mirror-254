import json


class APIException(Exception):
    def __init__(self, *args, **kwargs):
        super().__init__(*args)
        self.details = kwargs.get('details', None)
        self.code = kwargs.get('code', None)
        self.status_code = kwargs.get('status_code', None)

    @classmethod
    def from_resp(cls, resp):
        body = resp.text

        detail = None
        code = None
        msg = None
        try:
            data = json.loads(body)
            if data:
                detail = data['detail']
                code = data['code']
                msg = f'{detail} {code}'
        except ValueError:
            pass

        return cls(msg, detail=detail, code=code, status_code=resp.status_code)
