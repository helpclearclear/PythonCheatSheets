#When you go through API's, you might come across a ten-digit 'timestamp'. this is called a Unix timestamp. heres a function to convert it to human-readable:

def unixTimeStamp(stamp):
    import requests as R
    return R.get(f'https://showcase.api.linx.twenty57.net/UnixTime/fromunix?timestamp={stamp}').text

#When you want to retrieve an mp4 file via url, use this function. Make sure the string value of 'saveToFileName' is the name/path of a local file ending in '.mp4':

def retrieveMP4ByURL(url, saveToFileName):
    import urllib.request as perform
    return perform.urlretrieve(url, saveToFileName)
