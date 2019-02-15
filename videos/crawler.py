import requests
import json
import time
import os

def getSignature(credentials):
        url = credentials["signatureUrl"]
        queryString = credentials["signatureQueryString"]
        response = requests.request("GET", url, params=queryString)
        return response.text

def getHLS(credentials, hlsQuery):
        url = credentials["hlsUrl"]
        queryString = credentials[hlsQuery]
        headers = {"Authorization": credentials["userName"] + ":" + getSignature(credentials)}
        response = requests.request("GET", url, headers=headers, params=queryString)
        jsonObj = json.loads(response.text)
        return jsonObj["SessionId"]

def openStream(credentials, hlsQuery):
        date = time.strftime('%Y_%m_%d_%H_%M_%S', time.localtime(time.time()))
        url = credentials["streamingUrl"] + getHLS(credentials, hlsQuery) + ".m3u8"
        headers = {"Authorization": credentials["userName"] + ":" + getSignature(credentials)}
        response = requests.request("GET", url, headers=headers)
        print(url)
        os.system('ffmpeg -i "' + url + '" -t 00:01:00 result/videos/' + hlsQuery + '.mp4')

credentials = json.load(open("resource/botgo.txt"))

for key in credentials:
    if not key.startswith("hlsLaoQiao"):
        continue

    if key.startswith("hlsUrl"):
        continue

    print(key)
    time.sleep(30)
    openStream(credentials, key)
