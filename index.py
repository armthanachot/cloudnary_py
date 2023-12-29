import cloudinary_conf as conf
from cloudinary.uploader import upload
import requests


def download_image(fileUrl):
    resp = requests.get(fileUrl)
    #write file 
    with open("downloaded_image3.jpg", "wb") as f:
        f.write(resp.content)

def upload_file(filename):
    return upload(filename)

if __name__ == "__main__":
    # Upload a file
    response = upload_file("./img/kelly-sikkema-2z9cV4DsDlE-unsplash.jpg")

    print(response)

    #download_image()
    download_image("https://res.cloudinary.com/mediaserver123/image/upload/v1703778214/gawyv8rmof5md6dbkgwv.jpg")