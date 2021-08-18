# Processes

> see zombie.sh

##  What did you observe in the process table?

Status code Z (or Z+) for zombie process.

## What could we do to deal with this process?

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

For BSD formats and when the stat keyword is used, additional characters may be displayed:

| Character | Description |
| -- | -- |
| < | high-priority (not nice to other users)
| N | low-priority (nice to other users)
| L | has pages locked into memory (for real-time and custom IO)
| s | is a session leader
| l | is multi-threaded (using CLONE_THREAD, like NPTL pthreads do)
| + | is in the foreground process group.
