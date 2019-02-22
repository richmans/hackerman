from console import Console


class Hackerman:
    def main(self):
        self.console = Console()
        self.console.start()
        try:
            self.console.join()
        except KeyboardInterrupt:
            self.console.shutdown()
            self.console.join(1.0)


if __name__ == "__main__":
    Hackerman().main()