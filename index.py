import cloudinary_conf as conf
from cloudinary.uploader import upload
import requests
import os
import time

def download_image(fileUrl):
    resp = requests.get(fileUrl)
    #check dir
    if os.path.isdir("downloaded_image") == False:
        os.mkdir("downloaded_image")
    timeStampStr = time.strftime("%Y%m%d-%H%M%S")
    fileExt = os.path.splitext(fileUrl)[1]
    collectPath = "./downloaded_image/" + timeStampStr + fileExt
    
    #write file 
    with open(collectPath, "wb") as f:
        f.write(resp.content)
    
    #sleep 3 seconds
    time.sleep(3)
    #check file and delete 
    if os.path.isfile(collectPath) == True:
        os.remove(collectPath)

def upload_file(filename):
    return upload(filename)

if __name__ == "__main__":
    # Upload a file
    response = upload_file("./img/kelly-sikkema-2z9cV4DsDlE-unsplash.jpg")

    print(response)

    #download_image()
    download_image("https://res.cloudinary.com/mediaserver123/image/upload/v1703778214/gawyv8rmof5md6dbkgwv.jpg")