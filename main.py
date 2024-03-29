import sys
from os import walk
from pprint import pprint

from cheshire_cat_api.api.rabbit_hole_api import RabbitHoleApi
from cheshire_cat_api.api_client import ApiClient
from cheshire_cat_api.configuration import Configuration

# get a list of all files in a directory passed as command line argument
path = sys.argv[1]
filenames = next(walk(path), (None, None, []))[2]  # [] if no file

try:
    url = sys.argv[2]
except Exception as e:
    url = "http://localhost:1865"

conf = Configuration(host=url)

file = open("error.txt", "w")

# Enter a context with an instance of the API client
with ApiClient(conf) as api_client:
    # Create an instance of the API class
    api_instance = RabbitHoleApi(api_client)

    for fileName in filenames:

        try:
            # Upload File
            api_response = api_instance.upload_file(path + "\\" + fileName)
            print("The response of RabbitHoleApi->upload_file:\n")
            pprint(api_response)
        except Exception as e:
            print("Exception when calling RabbitHoleApi->upload_file: %s\n" % e)
            file.write(e)
