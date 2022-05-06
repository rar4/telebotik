class CustomError(Exception):
    def __init__(self, message=None, name = None):
        self.message = message
        self.name = name

    def __str__(self):
        if self.message == None or self.name == None:
            return 'custom error has been raised'
        else:
            return f'{self.name} has been raised. {self.message}'

error = CustomError('simple message', 'NonReasonError')

raise error

