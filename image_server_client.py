import base64
from tkinter import filedialog

import requests

server = "http://vcm-21170.vm.duke.edu"


# Select Image to Upload

def select_image():
    filename = filedialog.askopenfilename(initialdir="Images")
    return filename


# Convert to base64 string
def convert_image_file_to_base64_string(filename):
    with open(filename, "rb") as image_file:
        b64_bytes = base64.b64encode(image_file.read())
    b64_string = str(b64_bytes, encoding='utf-8')
    return b64_string


# Upload base64 string
def make_JSON_for_image_upload(b64_string):
    image_json = {"image": b64_string, "net_id": "rdh46", "id_no": 2}
    return image_json


def send_image(server, image_json):
    r = requests.post(server + "/add_image", json=image_json)
    print(r.status_code)
    print(r.text)


# Download Watermarked Image
def get_watermark(server):
    r = requests.get(server + "/get_image/rdh46/2")
    print(r.status_code)
    return r.text

def save_image_file(downloaded_image_base64, file_output):
    image_bytes = base64.b64decode(downloaded_image_base64)
    with open(file_output, "wb") as out_file:
        out_file.write(image_bytes)
    return



def main():
    filename = select_image()
    if filename == "":
        return
    b64string = convert_image_file_to_base64_string(filename)
    image_json = make_JSON_for_image_upload(b64string)
    send_image(server, image_json)
    downloaded_image_base64 = get_watermark(server)
    save_image_file(downloaded_image_base64, "watermark_download.JPG")


if __name__ == "__main__":
    main()
