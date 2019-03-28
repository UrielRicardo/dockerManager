#!/usr/bin/python3
import docker
import string
from random import *

min_char = 8
max_char = 12
allchar = string.ascii_letters +  string.digits
password = "".join(choice(allchar) for x in range(randint(min_char, max_char)))



client = docker.from_env()


def createUser(password):
   user = input("Username: ")
   print("This is your password : ",password)

   for container in client.containers.list():
           container = client.containers.get(container.id)

           container.exec_run('useradd -s /bin/bash -m \"%s\"' % (user),tty=True)
           container.exec_run("sh -c 'echo \"%s:%s\" | chpasswd'" % (user,password),tty=True)


def deleteUser():
   user = input("Username to delete: ")
   for container in client.containers.list():
           container = client.containers.get(container.id)
           container.exec_run('userdel -r \"%s\"' % (user),tty=True)


question = input("Create user: [c] or Delete user: [d]: ")

if question == "c":
    createUser(password)
elif question == "d":
    deleteUser()
else:
    raise SystemExit
