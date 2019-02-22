from threading import Thread
import sys
import select
import colorful


class Console(Thread):
    def __init__(self):
        self.shutting_down = False
        super().__init__()

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

    def prompt(self):
        self.print("$ ", False)

    def get_command(self):
        i, o, e = select.select([sys.stdin], [], [], 1)
        if i:
            return sys.stdin.readline().strip()

    def handle_command(self, command):
        if command == 'exit':
            self.shutdown()

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