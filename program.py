class Program:
    long_running = False

    def __init__(self, kernel, progname, args, stdin, stdout):
        self.kernel = kernel
        self.stdout = stdout
        self.progname = progname
        self.stdin = stdin
        self.args = args
        self.progress = 0
        self.state = 'running'

    def add_progress(self, amount):
        self.progress = min(self.progress+amount, 100)
        if self.progress == 100:
            self.done()

    def done(self):
        self.state = 'finished'

    def run(self, exec_time=0.1):
        if self.long_running:
            self.execute(exec_time)
        else:
            self.execute()
            self.done()