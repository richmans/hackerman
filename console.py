from threading import Thread
import sys
import select
import colorful
from command import Command


class Console(Thread):
    def __init__(self, kernel, stdin, stdout):
        self.shutting_down = False
        self.kernel = kernel
        self.stdout = stdout
        self.stdin = stdin
        super().__init__()
        self.daemon = True

    def banner(self):
        self.print("""{c.green}         _   _            _                                   
        | | | |          | |                                  
        | |_| | __ _  ___| | _____ _ __ _ __ ___   __ _ _ __  
        |  _  |/ _` |/ __| |/ / _ \ '__| '_ ` _ \ / _` | '_ \ 
        | | | | (_| | (__|   <  __/ |  | | | | | | (_| | | | |
        \_| |_/\__,_|\___|_|\_\___|_|  |_| |_| |_|\__,_|_| |_|
        {c.close_fg_color}""")

    def print(self, msg, newline=True):
        if newline:
            end = '\n'
        else:
            end = ''
        self.stdout.write(msg.format(c=colorful) + end)
        self.stdout.flush()

    def error(self, msg):
        self.print("{c.red}" + msg + "{c.close_fg_color}")

    def prompt(self):
        self.print("$ ", False)

    def get_command(self):
        cmd = self.stdin.readline()
        if cmd:
            return Command(cmd, self, self)
        else:
            return None

    def handle_command(self, command):
        self.kernel.handle_command(command)

    def shutdown(self):
        self.shutting_down = True

    def run(self):
        self.banner()
        self.prompt()
        while not self.shutting_down:
            command = self.get_command()
            if command is not None:
                self.handle_command(command)
                self.prompt()