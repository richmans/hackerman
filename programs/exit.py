from program import Program
from programs import register_program


class ExitProgram(Program):
    long_running = False

    def execute(self):
        self.stdout.print("{c.red}Shutting down...{c.close_fg_color}")
        self.kernel.shutdown()
        self.done()


register_program('exit', ExitProgram)