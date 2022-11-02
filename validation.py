class ValidationError(BaseException):
    pass


def check(cond: bool, msg: str) -> None:
    if not cond:
        raise ValidationError(f'{msg}')
    