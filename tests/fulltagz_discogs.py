import discogs_client
import os
import time
from cryptography.fernet import Fernet
import sys
import dotenv
from os.path import join, dirname
from dotenv import load_dotenv
dotenv_path = "tests/api.env"
load_dotenv(dotenv_path)
user_token = os.environ.get("DISCOGS_TOKEN")

def discogstokenchecker(user_token):
    dotenv_path = 'tests/api.env'
    load_dotenv(dotenv_path)
    user_token = os.environ.get("DISCOGS_TOKEN")
    print("Please Wait")
    try:
        d = discogs_client.Client('fulltagz/1.0', user_token=user_token)
        results = d.search('Stockholm By Night', type='release')
        print(results.pages)
    except discogs_client.exceptions.HTTPError:
        print("Invaild Token (401)")
        exit(1)
discogstokenchecker(user_token)
