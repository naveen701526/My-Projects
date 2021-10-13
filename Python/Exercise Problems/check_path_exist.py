import os
print("Test a path exists or not:")
path = r'g:\\testpath\\a.txt'
print(os.path.exists(path))
path = r'g:\\testpath\\p.txt'
print(os.path.exists(path))
print("\nFile name of the path:")
print(os.path.basename(path))
print("\nDir name of the path:")
print(os.path.dirname(path))
