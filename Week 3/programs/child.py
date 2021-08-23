import time, sys, os

print("="*50)

print(f"\n=> child.py: new process with PID = {os.getpid()}")

# If running another_fork_example.py, this line will demonstrate the use of environment variables.
try:
    print(f"Env variables do work! QUERY_STRING = {os.environ['QUERY_STRING']}")
except KeyError:
    pass

print("\nI am the NEW process. I REPLACED parent.py child thread when \"execv()\" was called.")

print("Sleeping for 10 seconds...\n\n" + "="*50 + "\n")

time.sleep(1)
sys.exit(30)