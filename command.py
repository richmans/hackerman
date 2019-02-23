import shlex


class Command:
    def __init__(self, cmd, stdin, stdout):
        self.stdin = stdin
        self.stdout = stdout
        self.cmd = cmd
        self.parts = shlex.split(cmd)
        self.program = ''
        self.args = []
        if len(self.parts) > 0:
            self.program = self.parts[0]
            self.args = self.parts[1:]