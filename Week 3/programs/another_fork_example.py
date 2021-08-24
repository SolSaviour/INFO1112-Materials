#!/bin/python
import os, sys

def fork_and_run():
    os.environ["QUERY_STRING"] = input("What is your name? ")
    cmd = '/bin/python3'
    pid = os.fork()
    if pid == 0: # child is 0, always 0. How to remember? When a child is born, they are age 0!!! Just like their PID.
        os.execle(cmd, cmd, "child.py", os.environ)
        sys.exit(99)
    elif pid == -1:
        print("FORK FAILED")
        sys.exit(1)
    else:
        print("Parent: I'm the parent process")
        print("Parent: I'm waiting for the child to finish sleeping")
        wval = os.wait()
        ret_value = wval[1]>>8
        print(f"Parent: Waiting over! Child process ID was: {wval[0]} and exit status was: {ret_value}")

if __name__ == "__main__":
    fork_and_run()