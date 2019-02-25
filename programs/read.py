from program import Program
from programs import register_program


class ReadfileProgram(Program):
    long_running = False

    def execute(self):
        if len(self.args) < 1:
            self.stdout.error("Please provide file path")
            return
        filnam = self.args[0]
        fil = self.kernel.fs.open(filnam)
        if not fil:
            self.stdout.error("Can not open file: " + filnam)
            return
        self.stdout.print(fil.read())


register_program('rf', ReadfileProgram)
register_program('read', ReadfileProgram)