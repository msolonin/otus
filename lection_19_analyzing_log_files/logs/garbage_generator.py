import time
import sys

count = 0
while True:
    count += 1
    print("time: {}, count {}".format(time.time(), count))
    # Put data in stdout
    sys.stdout.flush()
    time.sleep(0.5)
