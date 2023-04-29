from ssh_pymongo import MongoSession
session = MongoSession(host='202.112.47.121',port=22,user='root', key='/home/ubuntu/.ssh/id_rsa',to_port=27017, to_host='127.0.0.1')
db = session.connection['PROD_DATA']
osv = db['parsed_osv']
have = 0
none = 0
check = 0
#for document in osv.aggregate([{'$sample': {'size': 1000}}]):
for document in osv.find():
    if 'references' in document:
        check += 1
        giturl = []
        for url in document['references']:
            if 'commit' in url['url']:
                giturl.append(url['url'])
        print(giturl)
        if giturl:
            have += 1
    else:
        print("no reference")
        none += 1
print("have %d check %d none %d", have, check, none)