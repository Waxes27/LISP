class BigError(Exception):
    lineNumber = None

    def __init__(self, *args):
        if args:
            self.message = args[0]
            if len(args) > 1 and args[1].isdigit() and int(args[1]) >= 1:
                lineNumber = int(args[1])
        else:
            self.message = None

    def __str__(self) -> str:
        if self.message:
            return f"BIG ERROR: {self.message}"
        else:
            return f"BIG ERROR: An error that cannot be understood has been encountered"


class SyntaxError(Exception):
    def __init__(self, *args):
        if args:
            self.message = args[0]
