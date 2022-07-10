import os
try:
    from requests import get
except ImportError:
    os.system('pip install requests')
    from requests import get
session = input('Enter SessionID : ')
link = input("Enter Link Story : ")
def storyViews():
    splt = link.split('/')
    idStory = splt[5]
    idStory = idStory.split('?')[0]
    Headers = {
        "X-IG-Capabilities": "3yo=",
        "Cookie": f"sessionid={session}",
        "Connection": "keep-alive",
        "Accept": "*/*",
        "User-Agent": "Instagram 10.4.0 (iPhone7,2; iOS 12_5_1; en_SA@calendar=gregorian; ar-SA; scale=2.00; gamut=normal; 750x1334) AppleWebKit/420+",
        "Accept-Language": "ar-SA;q=1",
        "Accept-Encoding": "gzip, deflate",
        "X-IG-Connection-Type": "WiFi",
    }
    req = get(f"https://i.instagram.com/api/v1/media/{idStory}/list_reel_media_viewer/",headers=Headers)
    total = req.json()['updated_media']['viewer_count']
    i = 0
    while i < 21:
        try:

            print(req.json()['users'][i]['username'])
            with open("views story by zyll.txt", "a") as x:
                x.write(f"{req.json()['users'][i]['username']}\n")
            i+=1
        except:
            break
    max = 20
    ii = 0
    req2 = get(f"https://i.instagram.com/api/v1/media/{idStory}/list_reel_media_viewer/?max_id={str(max)}",headers=Headers)
    while int(total) > max:
        try:

            print(req2.json()['users'][ii]['username'])
            with open("views story by zyll.txt", "a") as x:
                x.write(f"{req2.json()['users'][ii]['username']}\n")
            ii+=1
            max +=1
            if ii == 50:
                ii = 0
                req2 = get(f"https://i.instagram.com/api/v1/media/{idStory}/list_reel_media_viewer/?max_id={str(max)}",
                           headers=Headers)
                continue
        except:
            break
    print(f"Finished : {total}")
storyViews()











