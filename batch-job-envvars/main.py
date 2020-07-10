import os

print("Batch Job started")

print("##############################")

print("Env Variables:")
for key, value in os.environ.items():
    print(key + ": " + value)

print("##############################")

print("Batch Job completed successfully")
