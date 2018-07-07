import requests
import os
import errno
from bs4 import BeautifulSoup
import subprocess as sub

# 取得して期待カレンダーの年月を配列に設定
# TODO コマンドの引数で渡すかなんかで、もっといい感じにイミュータブルな方法を考えたい
target_months = ['2017-12', '2018-01', '2018-02',
                 '2018-03', '2018-04', '2018-05', '2018-06']

# 処理開始前に要らないファイルがあったら消す
def silentremove(filename):
    try:
        os.remove(filename)
    except OSError as e:  # this would be "except OSError, e:" before Python 2.6
        if e.errno != errno.ENOENT:  # errno.ENOENT = no such file or directory
            raise  # re-raise exception if a different error occurred

# 設定した年月のカレンダーを取ってくる
for target_month in target_months:
    target_url = 'https://wp.infra-workshop.tech/events/' + target_month + '/'
    save_file = 'scraped/' + target_month + '.txt'

    if os.path.exists(save_file):
        silentremove(save_file)

    r = requests.get(target_url)
    soup = BeautifulSoup(r.text, 'lxml')

    for a in soup.find_all('a', attrs={'class': 'url'}):
        text = a.get_text()
        with open(save_file, "a", encoding="utf-8") as f:
            f.write(text+'\n')
    print('got ' + target_month)

# 取得してきたファイルを全部ぐちゃっとくっつけてtotal.txtに保存
mergeFiles = sub.getoutput('cat scraped/201*.txt > scraped/total.txt')

print('done!')
