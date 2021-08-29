# Scheduling

The kernel stores a great deal of information about processes including process priority 
which is simply: the scheduling priority attached to a process.

Processes with a higher priority (lower numbers) will be executed before those with a lower priority (higher numbers), while processes with the same priority are scheduled one after the next, repeatedly.

## Why is this important?

Read more about that [here](https://medium.com/@chetaniam/a-brief-guide-to-priority-and-nice-values-in-the-linux-ecosystem-fb39e49815e0).

## How it works

There are a total of 140 priorities and two distinct priority ranges implemented in Linux. 

##### Range One

The first one is a nice value, NI, (niceness) which ranges from -20 (highest priority value) to 19 (lowest priority value) and the default is 0. 

##### Range Two

The other is the real-time priority, PRI, which ranges from 1 to 99 by default, then 100 to 139 are meant for user-space.

One important characteristic of Linux is dynamic priority-based scheduling, 
which allows the nice value of processes to be changed (increased or decreased) depending on your needs.

```bash
$ ps -l
$ top
$ htop
```

You'll see there is a PRI (sometimes PR) column as well, this is the process’s actual priority, as seen by the Linux kernel,
while NI is the nice value, which is a user-space concept.

Syntax:
`$ nice -n <nice value> <command>`

> Important - if the "-n <nice value>" is ommited (left out), a value of 10 is assumed.

`$ renice -n <nice value> -p <pid of process>`

## How is PR calculated?

PR = 20 + NI \
   = 20 + (-20 to + 19) \
   = 20 + -20  to 20 + 19 \
   = 0 to 39 (which is same as 100 to 139)

## Additional reading and references

- "Ps Output Fields". (Knowedge Base) From: https://kb.iu.edu/d/afnv 
- "How to set linux processes priority using nice and renice commands" (Tecmint) From: https://www.tecmint.com/set-linux-process-priority-using-nice-and-renice-commands/

