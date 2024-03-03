from cheshire_cat_api.api_client import ApiClient
from cheshire_cat_api.configuration import Configuration
from cheshire_cat_api.api.rabbit_hole_api import RabbitHoleApi

from pprint import pprint
from os import walk
import sys

# get a list of all files in a directory passed as command line argument
path = sys.argv[1]
filenames = next(walk(path), (None, None, []))[2]  # [] if no file

conf = Configuration(host="http://localhost:1865")

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
