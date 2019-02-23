from program import Program
from programs import register_program


class ProclistProgram(Program):
    long_running = False

    def execute(self):
        if len(self.kernel.proclist) == 0:
            self.stdout.print("No running programs")
            return
        for p in self.kernel.proclist:
            self.stdout.print("{} {:3d}%".format(p.progname, int(p.progress)))


register_program('pl', ProclistProgram)
register_program('proclist', ProclistProgram)