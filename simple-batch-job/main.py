import random
import time
import sys

print("Batch Job started")
# 1 out of 10 jobs should fail by random

if random.random() < 0.1:
    raise Exception("Batch Job exited with error")

time.sleep(5)
print("Batch Job completed successfully")
