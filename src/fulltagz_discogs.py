import discogs_client
import os
from cryptography.fernet import Fernet
from dotenv import load_dotenv
#dotenv_path = "api.env"
#load_dotenv(dotenv_path)
#user_token = os.environ.get("DISCOGS_TOKEN")

def discogstokenchecker(user_token):
    if user_token != "":
        to_write = "DISCOGS_TOKEN = ", user_token

        try:
            with open("api.env", "w") as api_file:
                api_file.writelines(to_write)
                api_file.close()
            print("Establishing connection from the given API...")
            d = discogs_client.Client('fulltagz/1.0', user_token=user_token)
            results = d.search('Stockholm By Night', type='release')
            print(results.pages)
        except discogs_client.exceptions.HTTPError:
            print("Invaild Token (401)")
            exit(1)
    else:

        dotenv_path = 'api.env'
        load_dotenv(dotenv_path)
        user_token = os.environ.get("DISCOGS_TOKEN")
        print("Please Wait")
        try:
            print("Establishing connection from the enviroment file...")
            d = discogs_client.Client('fulltagz/1.0', user_token=user_token)
            results = d.search('Stockholm By Night', type='release')
            print(results.pages)
        except discogs_client.exceptions.HTTPError:
            print("Invaild Token (401)")
            exit(1)
