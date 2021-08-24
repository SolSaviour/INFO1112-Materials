import os

cmd = '/bin/bash'

# Method 1
os.execl(cmd, cmd, "-c", "ls")

# Method 2
os.execle(cmd, cmd, "-c", "ls", os.environ)

# Method 3
os.execv(cmd, (cmd, "-c", "ls"))

# Method 4
os.execve(cmd, (cmd, "-c", "ls"), os.environ)