def check_number(number):
    if len(number) == 0:
        err = MultiplyException('Empty input')
        raise err
    for i in range(len(number)):
        if number[i] not in '0123456789' and number[0] != '-':
            err = MultiplyException('Invalid Input :')
            err.arg = number
            err.type = type(number)
            raise err
    return int(number)


class MultiplyException(Exception):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.type = object
        self.arg = ""

    pass
