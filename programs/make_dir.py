from program import Program
from programs import register_program


class MakedirProgram(Program):
    long_running = False

    def execute(self):
        self.kernel.fs.make_dir(self.args[0])


register_program('md', MakedirProgram)
register_program('mkdir', MakedirProgram)