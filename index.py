import cloudinary_conf as conf
from cloudinary.uploader import upload
from cloudinary.utils import cloudinary_url, download_zip_url
from cloudinary.api import delete_resources_by_tag, resources_by_tag
import requests


def download_image():
    resp = requests.get("https://res.cloudinary.com/mediaserver123/image/upload/v1703778214/gawyv8rmof5md6dbkgwv.jpg")
    #write file 
    with open("downloaded_image2.jpg", "wb") as f:
        f.write(resp.content)

if __name__ == "__main__":
    # Upload a file
    # response = upload("kelly-sikkema-2z9cV4DsDlE-unsplash.jpg")

    # Print the response
    # print(response)

    #download_image()
    download_image()