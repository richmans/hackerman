# Hackerman
This is one of those brainfarts we had: what if we made a board-game about hackers? 
The game would combine a tech-ish computer environment with a real-life game board,
cards and all that jazz.

For this game to work, we would need a virtual computing environment that simplifies
all the details of a real computer, while still having the main conceptual things like
networks, filesystems and commands. This is a first attempt at building that.

The name hackerman is a placeholder. The actual game may be named differently.

Here's an example of a session:

```
$ pl
No running programs
$ scan
Kernel: Program has been started in the background
$ pl
scan   0%
$ pl
scan   2%
$ pl
scan   3%
$ pl
scan   5%
$ exit
Shutting down...
$ 
```

Anti-Rude-Comment-Disclaimer: I am aware that the thing that I call 'Kernel' is not
something you would normally call a kernel, and that many things in this program do
not accurately resemble a real OS. That is actually the point of this project ;-)