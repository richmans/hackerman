from program import Program
from programs import register_program


class ScanProgram(Program):
    long_running = True

    def execute(self, execution_time=0.1):
        self.add_progress(execution_time)


register_program('scan', ScanProgram)