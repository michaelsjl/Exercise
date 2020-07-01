# coding: utf-8

import requests

def upload_images_analysis_letters():
    url = 'http://localhost:5000/simple-ocr/v1/image-letters'
    
    images = ['a-few-letters.png',
            'a-lot-letters.png',
            'mix-letters.png',
            'no-letters.png',
            'not-picture.txt']

    for image in images:
        files = {'image_file': open(image, 'rb')}

        r = requests.post(url, files=files)
    
        print("======"+str(image)+"=====")
        print("status_code: "+str(r.status_code))
        print(r.text)
        print("=========================")


if __name__ == "__main__":
    upload_images_analysis_letters()
