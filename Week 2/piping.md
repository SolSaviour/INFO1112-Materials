# Piping

In the real world, a pipe is often used to transfer liquids such as water. It allows flow from one end to another! In Bash, often what we want to transfer is data, i.e., output from a command, text, content from a file, etc.

We can take this data, put it through our pipe, and connect it to a program or process which will accept this as input.

**Example**

Let's say we have a script, `myscript.sh`:

```bash
#!/bin/bash

read name
echo "Hello $name!"
```

When we run this script, it will prompt the user for input (i.e. wait blankly until the user types something in and hits enter), and then spit out `Hello <whatever the user inputted>`. 

If I was to input my name `Dylan`, the output of this program would be: 
`Hello Dylan!`.

Instead of giving my name to the process directly,

> Note: I called it a process as I assume the *program* has been run and now is a process waiting for input.

I can feed my name into it through a pipe!

**Example**

`$ echo 'Dylan' | ./myscript.sh`

> Note: The $ symbol represents the 'bash prompt', you will see this a lot of websites which show bash code.

The output of this command is the same: `Hello Dylan!`.

*Why does this work?* - the output of `echo 'Dylan'` is sent to our script, `myscript.sh` (notice the ./ beforehand, this represents running, or activating, the script), which then uses "Dylan" as a variable to then print to standard output.

---

It's common to _string_, or _chain_, pipes together to achieve something. For example:

`$ ps aux | tail -n 2 | head -n 1 | awk {'print $2'}`

Let's break it down.

* `ps aux` - a command I use when I want to list out all processes from all users (-a), displaying the user owner (-u), and those which have not been executed from the terminal (-x), i.e. system processes. More info on this command [here](https://www.computernetworkingnotes.com/linux-tutorials/ps-aux-command-and-ps-command-explained.html).
* `tail -n 2 | head -n 1` - tail will get the last two processes and head will only show the first of those 2, therefore it shows the second last process.
* `awk {'print $2'}` - gets the second column of the piped input, which happens to be the Process ID (PID). Some awk tutorials I like are: [tutorials point](https://www.tutorialspoint.com/unix_commands/awk.htm) and [howtogeek](https://www.howtogeek.com/562941/how-to-use-the-awk-command-on-linux/).

> Note: awk requires that you use single quotes instead of double.