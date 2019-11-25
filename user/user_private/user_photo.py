import base64, re, string, random, os
from user.db import db_user


def pictures(photo, username):
    imges = re.findall(r"base64,(.*)", photo)
    imgdata = base64.b64decode(imges[0])
    src = '/home/date/library/img1/'
    result = db_user.sql_query_photo(username)
    if result and result != "1.jpg":
        ran_str = result
        src = src + ran_str
    else:
        while 1:
            ran_str = ''.join(random.sample(string.ascii_letters + string.digits, 20))
            src = src + ran_str + '.jpg'
            if os.path.exists(src):
                continue
            break
    print(src)
    file = open(src, 'wb')
    file.write(imgdata)
    file.close()
    return ran_str
