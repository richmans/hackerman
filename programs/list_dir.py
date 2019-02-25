from program import Program
from programs import register_program


class ListDirProgram(Program):
    long_running = False

    def execute(self):
        path = '/'
        if len(self.args) > 0:
            path = self.args[0]
        for it in self.kernel.fs.list_dir(path):
            self.stdout.print(it)


register_program('ls', ListDirProgram)
register_program('list', ListDirProgram)