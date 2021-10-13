import os
print("Parent’s process id:",os.getppid())
uid = os.getuid()
print("\nUser ID of the current process:", uid)
uid = 1400
os.setuid(uid)
print("\nUser ID changed")
print("User ID of the current process:", os.getuid())
