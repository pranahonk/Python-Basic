# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import os
import shutil

from datetime import datetime
# from datetime import time
# from datetime import date
from datetime import timedelta
from os import path


# trying os built in function features
def print_os_name():
    print(os.name)


# trying files reand modification\
def read_and_write():
    f = open("textfile.txt", "w+")

    for i in range(10):
        f.write("this is line %d\r\n" % (i + 1))

    f.close()


class MyClass:
    def method1(self):
        print("my class method1")

    def method2(self, some_string):
        print("my Method 2" + some_string)


class AnotherClass(MyClass):
    def method3(self):
        MyClass.method1(self)
        print("this is method 3")

    def method4(self, some_string):
        MyClass.method2(self, some_string)


def try_oop_python():
    c = AnotherClass()
    c.method1()
    c.method3()
    c.method4("test")


def check_file_exist():
    if path.exists("textfile.txt"):
        # get the path to the file in the current directory
        src = path.realpath("textfile.txt")

        # let's make a backup copy by appending "bak" to the name
        dst = src + ".bak"

        # now use the shell to make a copy of the file
        shutil.copy(src, dst)

        # copy over the permissions, modification times, and other info
        shutil.copystat(src, dst)


def read_file():
    f = open("textfile.txt", "r")
    if f.mode == 'r':
        fl = f.readlines()
        for x in fl:
            print(x)


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.
    try_oop_python()
    print(timedelta(days=365, hours=5, minutes=1))
    now = datetime.now()
    print("today is: " + str(now))
    print("One year from now it will be:" + str(now + timedelta(days=365)))
    print("3 Weeks and 2 days from now it will be:" + str(now + timedelta(weeks=3, days=2)))
    check_file_exist()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
