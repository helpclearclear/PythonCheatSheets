#When you go through API's, you might come across a ten-digit 'timestamp'. this is called a Unix timestamp. heres a function to convert it to human-readable:

def unixTimeStamp(stamp):
    import requests as R
    return R.get(f'https://showcase.api.linx.twenty57.net/UnixTime/fromunix?timestamp={stamp}').text
