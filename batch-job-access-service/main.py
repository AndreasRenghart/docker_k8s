import random
import time
import sys
import os
import requests

print("Batch Job started")
# 1 out of 10 jobs should fail by random

print("##############################")

print("Env Variables:")
for key, value in os.environ.items():
    print(key + ": " + value)

print("##############################")

# Access kubernetes service: node-service
# Service is accesses by http://[service-name].[namespace] or simply http://[service-name] if default namespace
print("Access kubnetes service by DNS")
r = requests.get('http://node-service.default')
print(f"Status: {r.status_code}")
print("Response: " + r.text)

if random.random() < 0.1:
    raise Exception("Batch Job exited with error")

time.sleep(5)
print("Batch Job completed successfully")
