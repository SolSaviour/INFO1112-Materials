import os, sys, time

pid = os.fork()
if pid > 0: #main thread
    wval = os.wait()
    time.sleep(300)
elif pid == 0: #child thread
    sys.exit(0)
else:
    print("Fork error")