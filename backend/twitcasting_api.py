import json
import urllib.request
import base64
import datetime
import pprint

base_url = "https://apiv2.twitcasting.tv"

def getAccessToken():
    with open("./auth.json", "r") as f: 
        auth_json = json.load(f)
    auth_str = auth_json["client_id"]+":"+auth_json["client_secret"]
    auth_b64encoded = base64.b64encode(auth_str.encode("utf-8"))
    access_token = "Basic "+auth_b64encoded.decode("ascii")
    return access_token


def getUserInfo(user_id):
    access_token = getAccessToken()
    request_url = "/users/"+user_id+"/movies"
    request_obj = urllib.request.Request(base_url+request_url,
        headers={"X-api-Version":"2.0", "Authorization":access_token}
    )
    with urllib.request.urlopen(request_obj) as response_obj:
        response_body = json.load(response_obj)
    for movie in response_body["movies"]:
        created_datetime = datetime.datetime.fromtimestamp(float(movie["created"]))
        movie["created"] = created_datetime.strftime("%Y/%m/%d %H:%M")
        duration_second = int(movie["duration"])
        movie["duration"] = "{:02}:{:02}".format(duration_second//60, duration_second%60)

    # pprint.pprint(response_body)
    return response_body


