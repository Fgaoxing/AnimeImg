import requests as requ
import threading, time, sys
from pathlib import Path

def get_url(url):
    try:
        return requ.get(url, allow_redirects=False).headers.get('Location')
    except:
        return None


url = sys.argv[1]
urlList = []

def down(img):
    try:
        imgReq = requ.get(url, stream=True)
        with open(str(time.time_ns()) + Path(img).suffix, 'wb') as f:
            for chunk in imgReq.iter_content(chunk_size=1024):
                if chunk:
                    f.write(chunk)
                    f.flush()
            f.close()
            print(img, "下载完成")        
    except:
        return None

while True:
    img = get_url(url)
    if img != None and img not in urlList:
        print(f"发现：{img}已发现{len(urlList)}个")
        urlList.append(img)
        threading.Thread(target=down, args=(img,)).start()
    time.sleep(0.3)