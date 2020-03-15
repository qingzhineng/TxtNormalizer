import urllib3
import urllib3.contrib.pyopenssl
import certifi
import os

def sslDownloadSingle(url):
    header = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.25111 Safari/537.36"
    }
    http = urllib3.PoolManager(cert_reqs='CERT_REQUIRED', ca_certs=certifi.where())
    response = http.request('GET', url, None, header)
    
    splitPath = url.split('/')
    fileName = splitPath.pop()
    with open(fileName, 'wb+') as f:
        print(u'正在保存的一张图片为:%s', fileName)
        f.write(response.data)
        


if __name__ == "__main__":
    dir = "D:\\download"
    os.chdir(dir)
    urllib3.contrib.pyopenssl.inject_into_urllib3()
    for line in open("D:\\todo.txt"):
        print(line);
        sslDownloadSingle(line.strip())

