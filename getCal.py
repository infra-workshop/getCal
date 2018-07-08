import requests
import re
import os
import errno
from bs4 import BeautifulSoup
import subprocess as sub
from time import sleep

target_months = ['2017-12', '2018-01', '2018-02',
                 '2018-03', '2018-04', '2018-05', '2018-06']


def silentremove(filename):
    try:
        os.remove(filename)
    except OSError as e:  # this would be "except OSError, e:" before Python 2.6
        if e.errno != errno.ENOENT:  # errno.ENOENT = no such file or directory
            raise  # re-raise exception if a different error occurred


for target_month in target_months:
    target_url_base = 'https://wp.infra-workshop.tech/events/'
    target_url = target_url_base + target_month + '/'
    save_file = 'scraped/' + target_month + '.txt'

    sleep(1)  # add wait time

    if os.path.exists(save_file):
        silentremove(save_file)

    r = requests.get(target_url)
    soup = BeautifulSoup(r.text, 'lxml')
    text_prev = ""  # for duplicated line check

    for td in soup.select('table tbody tr td '):  # get date from calender
        target_date = td.get("data-day")
        if target_date[:-3] == target_month:  # skip if prev or next month
            if len(td.select("div.tribe-events-viewmore"))==0:
                for div in td.select("div"):
                    if len(div.select("a.url")) != 0:  # exclude blank list
                        for a in div.find_all("a", attrs={"class": "url"}):  # similar to original
                            text = a.get_text()
                            # temporary work. To exclude duplicated line
                            # i.e. event from 2300 to 2500 (event is added to 2 days)
                            if text_prev != text:
                                with open(save_file, "a", encoding="utf-8") as f:
                                    f.write(text+'\n')
                            text_prev = text
            else:
                # if the day has more than 3 events, only first 3 events are shown in calender.
                # to fix it, search "day event page" instead of calender
                target_url_day = target_url_base + target_date + '/'

                sleep(1)  # add wait time

                r_day = requests.get(target_url_day)
                soup_day = BeautifulSoup(r_day.text, 'lxml')

                for title in soup_day.find_all("a", attrs={"class": "url"}):  # get date from calender
                    text = re.sub("\s", "", title.get_text())  # trim all blanks
                    with open(save_file, "a", encoding="utf-8") as f:
                        f.write(text + '\n')



    print('got ' + target_month)

mergeFiles = sub.getoutput('cat scraped/201*.txt > scraped/total.txt')

print('done!')
