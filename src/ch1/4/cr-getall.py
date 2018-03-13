'''
Created on 2018/03/08

@author: miyazawataishi
'''

# pythonのマニュアルを再帰的にDL
from bs4 import BeautifulSoup
from urllib.request import urlretrieve
from urllib.parse import urlparse, urljoin
from os import makedirs
import os.path, time, re

proc_files = {}


def enum_links(html, base):
    soup = BeautifulSoup(html, "html.parser")
    links = soup.select("link[rel='stylesheet']")  # css
    links += soup.select("a[href]")  # link
    result = []
    # href属性を取り出し、リンクを絶対パスに変換
    for a in links:
        href = a.attrs['href']
        url = urljoin(base, href)
        result.append(url)
    return result


# ファイルをDLし保存
def download_file(url):
    o = urlparse(url)
    savepath = "./" + o.netloc + o.path
    if (re.search(r"/$", savepath)):  # ディレクトリならindex.html
        savepath += "index.html"
    savedir = os.path.dirname(savepath)
    # すでにDL済み？
    if os.path.exists(savepath): return savepath
    # DL先のディレクトリを作成
    if not os.path.exists(savedir):
        print("mkdir=", savedir)
        makedirs(savedir)
    # ファイルをDL
    try:
        print("download=", url)
        urlretrieve(url, savepath)
        time.sleep(1)  # 礼儀として1秒スリープ
    except:
        print("DL失敗：", url)
        return None


# HTMLを解析してDLする関数
def analize_html(url, root_url):
    savepath = download_file(url)
    if savepath is None: return
    if savepath in proc_files: return  # 解析済みなら処理しない
    proc_files[savepath] = True
    print("analize_html=", url)
    # リンクを抽出
    html = open(savepath, "r", encoding="utf-8").read()
    links = enum_links(html, url)
    for link_url in links:
        # リンクがルート以外のパスをさしていたら無視
        if link_url.find(root_url) != 0:
            if not re.search(r".css$", link_url): continue
        # HTML?
        if re.search(r"(html|htm)$", link_url):
            # 再帰的に解析
            analize_html(link_url, root_url)
            continue
        # それ以外のファイル
        download_file(link_url)


if __name__ == "__main__":
    # URLを丸ごとDL
    url = "http://docs.python.jp/3.5/library/"
    analize_html(url, url)
