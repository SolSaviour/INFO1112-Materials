import os, sys, time

cmd = "/bin/python3"

pid = os.fork()
if pid == 0:
    print(f"=> parent.py: CHILD with PID = {os.getpid()}\n")
    os.execv(cmd, (cmd, "child.py"))
    sys.exit(99) #Who can tell me why this line doesn't run?
elif pid > 0:
    print(f"=> parent.py: PARENT with PID = {os.getpid()}")
    wval = os.wait()
    print(f"=> parent.py: PARENT says, \"child.py has finished with exit code {wval[1]>>8}\"")
else:
    print("Forking error")