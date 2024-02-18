import base64
import json
from io import BytesIO
from PIL import Image
from datetime import datetime
import time
from random import randrange
import requests

def base64ToImage(base64_string,type = 'RGB'):
    image_bytes = base64.b64decode(base64_string)
    image_buffer = BytesIO(image_bytes)
    image = Image.open(image_buffer)
    if 'RGB' == type:
        return image.convert('RGB')
    else:
        return image

def imageToBase64(image):
    return base64.b64encode(image)
def readURLImage(url):
    response = requests.get(url)
    # Check if the request was successful
    if response.status_code == 200:
        # Read the image from the response content
        #print(response.content)
        image = Image.open(BytesIO(response.content))
        # Now you can work with the image object
        # For example, you can display it:
        base64_data = base64.b64encode(response.content)
        #print(base64_data)
        #image.show()
        return image,base64_data
    else:
        #print("Failed to fetch the image")
        return None,None
##
# flag success/fail
# data when flag == success
# error when flag == fail
# #
def jsonMsg(status,data,error):
    result = {}
    result["status"] = status
    if "success" == status:
        result["data"] = data
    else:
        result["error"] = error
    return json.dumps(result)

def gen_rnd_filename(fmt):
    if fmt == "time1":
        return int(round(time() * 1000))
    elif fmt == "time2":
        return "%s%s" % (
            int(round(time() * 1000)),
            str(randrange(1000, 10000)),
        )
    elif fmt == "time3":
        return "%s%s" % (
            datetime.now().strftime("%Y%m%d%H%M%S"),
            str(randrange(1000, 10000)),
        )
    elif fmt == "time4":
        return "%s" % (
            datetime.now().strftime("%Y%m%d%H%M%S"),
        )
def recursive_decoder(obj):
    # Customize this function according to your needs
    if isinstance(obj, dict):
        for key, value in obj.items():
            obj[key] = recursive_decoder(value)  # Recursively decode nested objects
        return obj
    elif isinstance(obj, list):
        return [recursive_decoder(item) for item in obj]  # Recursively decode nested objects in lists
    else:
        return obj