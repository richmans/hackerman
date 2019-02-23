from threading import Thread
from time import sleep
from command import Command
import programs
import random

class Kernel(Thread):
    def __init__(self):
        self.shutting_down = False
        self.proclist = []
        super().__init__()
        self.time_slice = 0.1
        self.daemon = True

    def shutdown(self):
        self.shutting_down = True

    def handle_command(self, command:Command):
        if command.program == '':
            return
        program = programs.get(command.program)
        if not program:
            command.stdout.error("Unknown program: {}".format(command.program))
            return
        process = program(self, command.program, command.args, command.stdin, command.stdout)
        if process.long_running:
            self.proclist.append(process)
            command.stdin.print("{c.yellow}Kernel: Program has been started in the background{c.close_fg_color}")
        else:
            process.execute()

    def scheduler(self, run_time):
        ready_procs = [p for p in self.proclist if p.state == 'running']
        if len(ready_procs) == 0:
            return
        proc = random.choice(ready_procs)
        proc.execute(run_time)

    def clean_proclist(self):
        self.proclist = [p for p in self.proclist if p.state =='running']

    def run(self):
        while not self.shutting_down:
           self.scheduler(self.time_slice)
           self.clean_proclist()
           sleep(0.1)