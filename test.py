import sys # to add parameters when running script
import json # for config files
import time
import schedule # for pipeline scheduling
import pandas as pd 
import requests as req
from os import environ, remove
from pathlib import Path
from ftplib import FTP_TLS

# get ftp details
def get_ftp() -> FTP_TLS: # -> for type hint for the expected return type
    FTP_HOST = environ["FTP_HOST"]
    FTP_USER = environ["FTP_USER"]
    FTP_PASSWORD = environ["FTP_PASSWORD"]

    print(f"test: {FTP_HOST}") # f-string for embedded expressions

    ftp = FTP_TLS(FTP_HOST, FTP_USER, FTP_PASSWORD)
    ftp.prot_p() # establish secure data connection
    return ftp

# upload source to ftp
def upload_to_ftp(ftp: FTP_TLS, source: Path):
    with open(source, "rb") as s: # read binary to preserve data format
        ftp.storbinary(f"STOR {source.name}", s)

# delete source
def delete_source(source: Path):
    remove(source)

# data pipeline
def pipeline():
    ftp = get_ftp()
    upload_to_ftp(ftp, Path("employer-information.csv"))
    df = pd.read_csv("employer-information.csv", encoding="utf-16", sep='\t')
    print(df.head())
    delete_source(Path("employer-information.csv"))

# main script
if __name__=="__main__":

    pipeline()

    

    
