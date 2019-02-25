from program import Program
from programs import register_program


class MakefileProgram(Program):
    long_running = False

    def execute(self):
        self.kernel.fs.make_file(self.args[0])


register_program('mf', MakefileProgram)
register_program('mkfile', MakefileProgram)