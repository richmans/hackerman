from program import Program
from programs import register_program


class WritefileProgram(Program):
    long_running = False

    def execute(self):
        if len(self.args) < 2:
            self.stdout.error("Please provide file path and contents")
            return
        data = self.args[1]
        filnam = self.args[0]
        fil = self.kernel.fs.open(filnam)
        if not fil:
            self.stdout.error("Can not open file: " + filnam)
            return
        fil.write(data)


register_program('wf', WritefileProgram)
register_program('write', WritefileProgram)