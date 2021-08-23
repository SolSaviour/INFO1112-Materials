import os

cmd = '/bin/bash'

# Method 1
os.execl(cmd, cmd, "-c", "ls", )

# Method 2
os.execv(cmd, (cmd, "-c", "ls"))

# Method 3
os.execv(cmd, [cmd, "-c", "ls"])

# same thing as os.execv(cmd, (cmd, )) or os.execv(cmd, [cmd, ])
# the exec* family of commands differs in the way they take arguments

