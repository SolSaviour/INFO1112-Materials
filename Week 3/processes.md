# Processes

**Process** - a program with its code and data stored in the memory along with some metadata that shows who the owner is (UID), what open files it has (file descriptors).

## Background Processes

When we want to run a process *in the background*, we use a "&" symbol.

**Example:**

```bash
$ sleep 300 &
[1] 22 # 22 here is the process ID
$ jobs
[1]+  Running                 sleep 300 & 
$ fg 1 # 1 here is referring to the [1] in the above line
sleep 300

```

And from another terminal, we can know the process ID is 22, so we can send this process a signal!

We send signals using the bash command `kill`. The word "kill" is a little misleading, it only means here, "send a signal to...".

To find out what kind of signals we can send to our processes, we can use, `kill -l`.

The signals you'll use the most are:

| Signal | Description | Code | Example |
| -- | -- | -- | -- |
| SIGINT | Signal Interrupt | 2 | `kill -2 22` |
| SIGKILL | Terminate process | 9 | `kill -9 22` |
| SIGSTOP | Stop the process | 19 | `kill -19 22` |
| SIGCONT | Continue the process | 18 | `kill -18 22` |

> See signals.sh for example usage of these commands!

## System Calls

**DEMO** - https://youtu.be/WrMtdHrpAm0

## Process Codes

###  Run programs/zombie.py, what did you observe in the process table?

Status code Z (or Z+) for zombie process.

### What could we do to deal with this process?

`$ kill -9 <pid of the parent>`

From your output we see a "defunct", which means the process has either 
completed its task or has been corrupted or killed, but its child processes 
are still running or these parent process is monitoring its child process.


| PROCESS STATE CODES | Description |
| -- | -- |
| D | uninterruptible sleep (usually IO) |
| R | running or runnable (on run queue) |
| S | interruptible sleep (waiting for an event to complete) |
| T | stopped, either by a job control signal or because it is being traced. |
| W | paging (not valid since the 2.6.xx kernel) |
| X | dead (should never be seen) |
| Z | defunct ("zombie") process, terminated but not reaped by its parent. |

For [BSD formats](https://www.howtogeek.com/190773/htg-explains-whats-the-difference-between-linux-and-bsd/) and when the stat keyword is used, additional characters may be displayed:

| Character | Description |
| -- | -- |
| < | high-priority (not nice to other users) |
| N | low-priority (nice to other users) |
| L | has pages locked into memory (for real-time and custom IO) |
| s | is a session leader |
| l | is multi-threaded (using CLONE_THREAD, like NPTL pthreads do) |
| + | is in the foreground process group. |
