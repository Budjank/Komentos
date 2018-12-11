import json, fb, requests
from facepy import GraphAPI

class warna:
    ungu = '\033[95m'
    biru = '\033[94m'
    hijau = '\033[92m'
    oren = '\033[93m'
    merah = '\033[91m'

def banner():
    print warna.merah+"""
    ##########################################"""+warna.oren+"""
    #####   Spamtos Komentos Pesbuktos   #####"""+warna.hijau+"""
    ##########################################
    """
def spam():
    print warna.hijau+"Input Token"
    token = raw_input(warna.oren+"---> "+warna.biru)
    facebook = fb.graph.api(token)
    graph1 = GraphAPI(token)
    
    print warna.hijau+"ID Target"
    target = input(warna.oren+"---> "+warna.biru)
    print warna.hijau+"Limit"
    limit =raw_input(warna.oren+"---> "+warna.biru)
    query = str(target) + "/posts?fields=id&limit=%s"%(limit)
    r = graph1.get(query)
    
    asu = requests.get('https://graph.facebook.com/v3.0/%s?fields=feed.limit(%s)&access_token=%s'%(target,limit,token))
    gblk = json.loads(asu.text)
    for lmao in gblk['feed']['data']:
        print warna.hijau+"[*] Post Id : "+lmao['id']+""

    idlist = [x['id'] for x in r['data']]
    idlist.reverse()
    print(warna.biru+"")
    print(warna.merah+"Ada "+ str(len(idlist)) +" postingan yang siap dispam")
    print warna.hijau+"""
    Lanjut?
    y = ya
    t = tidack
    """
    char1 = raw_input(warna.oren+"---> "+warna.biru)
    count = 0
    if char1 == 'y' or char1 == 'ya':
        print warna.hijau+"Jumlah"
        nos = input(warna.oren+"---> "+warna.biru)
        print warna.hijau+"Text"
        mess = raw_input(warna.oren+"---> "+warna.biru)
        print warna.hijau+"""
        Random Post ID or Target Post ID
        r = random
        t = target
        """
        rt = raw_input(warna.oren+"---> "+warna.biru)
        if rt == "r":
            if nos <= len(idlist):
                for indid in (idlist[(len(idlist) - nos):]):
                    facebook.publish(cat = "comments", id = indid, message = mess)
                    facebook.publish(cat = "likes", id = indid)
                    count += 1
                    print warna.hijau+"Berhasil"
            else:
                print warna.merah+"Error"
        elif rt == "t":
            print warna.hijau+"Post ID"
            pid = raw_input(warna.oren+"---> "+warna.biru)
            if nos <= len(idlist):
                count = nos
                for lol in range(count):
                    params = {'access_token' : token, 'message' : mess}
                    voss = 'https://graph.facebook.com/{0}/comments'.format(pid)
                    cot = requests.post(voss, data = params)
                    id = pid.split('_')[0]
                   # count += 1
                #for lol in range(count)::
                    try:
                        print warna.hijau+"Berhasil" 
                    except KeyError:
                        print warna.merah+"Error"
        else:
            print warna.merah+"Error"
    elif char1 == 't' or char1 == 'tidack' or char1 == 'tidak':
        print warna.biru+"Bye..."
    else:
        print warna.merah+"Error"
##########################
banner()
spam()
