import sys # to add parameters when running script
import json # for config files
import time
import schedule # for pipeline scheduling
import pandas as pd 
import requests as req
from os import environ, remove
from pathlib import Path
from ftplib import FTP_TLS

def get_ftp() -> FTP_TLS: # -> for type hint for the expected return type
    FTP_HOST = environ["FTP_HOST"]
    FTP_USER = environ["FTP_USER"]
    FTP_PASSWORD = environ["FTP_PASSWORD"]

    print(f"test: {FTP_HOST}") # f-string for embedded expressions

    ftp = FTP_TLS(FTP_HOST, FTP_USER, FTP_PASSWORD)
    ftp.prot_p() # establish secure data connection
    return ftp

if __name__=="__main__":
    print(get_ftp())