import os

print("JENKINS CREDENTIALS")

username = os.getenv('username')
password = os.getenv('password')

print(username)
print(password)