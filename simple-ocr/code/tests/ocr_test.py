# coding: utf-8

import requests

def upload_images_analysis_letters():
    url = 'http://localhost:5000/analysis-image-letters'
    files = {'image_file': open('test02.png', 'rb')}

    r = requests.post(url, files=files)
    
    print r.status_code
    print r.text

if __name__ == "__main__":
    upload_images_analysis_letters()
