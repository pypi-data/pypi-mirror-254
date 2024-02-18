class Logger:

    def __init__(self, filename):
        self.terminal = sys.stdout
        self.filename = filename
        self.log = open(filename, "w")

    def write(self, message):
        self.terminal.write(message)
        self.log.write(message)

    def flush(self):
        self.terminal.flush()
        self.log.flush()

    def isatty(self):
        return False

    def read(self):
        sys.stdout.flush()
        with open(self.filename, "r") as f:
            return f.read()
