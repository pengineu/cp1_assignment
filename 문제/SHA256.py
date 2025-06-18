import hashlib

def hash(string, code):
    return hashlib.sha256(string.encode()).hexdigest() == code

print(hash("apple", "3a7bd3e2360a3d29eea436fcfb7e44c735d117c42d1c1835420b6b9942dd4f1b"))