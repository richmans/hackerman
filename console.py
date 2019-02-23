from threading import Thread
import sys
import select
import colorful
from command import Command


class Console(Thread):
    def __init__(self, kernel):
        self.shutting_down = False
        self.kernel = kernel
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
        print(msg.format(c=colorful), end=end)
        sys.stdout.flush()

    def error(self, msg):
        self.print("{c.red}" + msg + "{c.close_fg_color}")

    def prompt(self):
        self.print("$ ", False)

    def get_command(self):
        i, o, e = select.select([sys.stdin], [], [], 1)
        if i:
            return Command(sys.stdin.readline(), self, self)

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