from console import Console
from kernel import Kernel


class Hackerman:
    def __init__(self):
        self.kernel = Kernel()
        self.console = Console(self.kernel)

    def main(self):
        self.kernel.start()
        self.console.start()
        try:
            self.kernel.join()
        except KeyboardInterrupt:
            self.kernel.shutdown()
            self.kernel.join(1.0)


if __name__ == "__main__":
    Hackerman().main()