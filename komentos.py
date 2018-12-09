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
    query = str(target) + "/posts?fields=id&limit=10000"
    r = graph1.get(query)
    
    
    
    idlist = [x['id'] for x in r['data']]
    idlist.reverse()
    print("Ada "+ str(len(idlist)) +" postingan yang siap dispam")
    print warna.hijau+"""
    Lanjut?
    y = ya
    t = tidack
    """
    char1 = raw_input(warna.oren+"---> "+warna.biru)
    count = 0
    if char1 == 'y':
        print warna.hijau+"Jumlah"
        nos = input(warna.oren+"---> "+warna.biru)
        print warna.hijau+"Text"
        mess = raw_input(warna.oren+"---> "+warna.biru)
        if nos <= len(idlist):
           for indid in (idlist[(len(idlist) - nos):]):
            facebook.publish(cat = "comments", id = indid, message = mess) #Comments on each post
            facebook.publish(cat = "likes", id = indid) #Likes each post
            count += 1
            print(warna.hijau+"Berhasil " + warna.oren+"=> "+warna.biru+"https://www.facebook.com/" + str(indid).split('_')[0] + "/posts/" + str(indid).split('_')[1] + warna.hijau + " ["+str(count)+"]")
        else: 
          print warna.merah+"Error"
    else :
      print warna.merah+"Error"
##########################
banner()
spam()
