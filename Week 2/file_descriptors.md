# File Descriptors

This can be a confusing topic, so don't get too hung up on it if you don't understand right away! 

| File Descriptor | Represents |
| -- | -- |
| 0 | Standard Input |
| 1 | Standard Output | 
| 2 | Standard Error |

File descriptors (FDs) are non-negative integers that act as "handles" to files. They help us to interact more easily with these files.

A good example is, say you want to send all the error messages from a command to a file AS WELL AS the output of the command itself. 

`$ find / -name "*.conf" > results.txt 2>&1`

In this example we:
* firstly redirect standard output (FD **1**) to the file descriptor of results.txt. 
* Next, standard error (file descriptor 2) is redirected to file descriptor 1 (which WAS standard output, but is now pointing at file descriptor for the file: results.txt). 

That is the long way to write it, nowadays you can shorten it like such:

`$ find / -name "*.conf" &> results.txt`

[This](https://linuxconfig.org/bash-redirect-both-standard-output-and-standard-error-to-same-file) explains the above in a little more detail.

In case you were wondering...

* \> is equivalent to 1> 

**why?** \> is output redirection, 1 is the file descriptor for standard output. 

It's like saying: "Send standard output to..."

* < is equivalent to 0< 

**why?** < is input redirection, 0 is the file descriptor for standard input. 

It's like saying: "Receive input from..."