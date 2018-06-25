#!/bin/bash

mecab -d /usr/local/lib/mecab/dic/mecab-ipadic-neologd scraped/2017-12.txt | grep "名詞" | cut -f 1 | sort | uniq -c | sort -r -n > result/2017-12.txt
mecab -d /usr/local/lib/mecab/dic/mecab-ipadic-neologd scraped/2018-01.txt | grep "名詞" | cut -f 1 | sort | uniq -c | sort -r -n > result/2018-01.txt
mecab -d /usr/local/lib/mecab/dic/mecab-ipadic-neologd scraped/2018-02.txt | grep "名詞" | cut -f 1 | sort | uniq -c | sort -r -n > result/2018-02.txt
mecab -d /usr/local/lib/mecab/dic/mecab-ipadic-neologd scraped/2018-03.txt | grep "名詞" | cut -f 1 | sort | uniq -c | sort -r -n > result/2018-03.txt
mecab -d /usr/local/lib/mecab/dic/mecab-ipadic-neologd scraped/2018-04.txt | grep "名詞" | cut -f 1 | sort | uniq -c | sort -r -n > result/2018-04.txt
mecab -d /usr/local/lib/mecab/dic/mecab-ipadic-neologd scraped/2018-05.txt | grep "名詞" | cut -f 1 | sort | uniq -c | sort -r -n > result/2018-05.txt
mecab -d /usr/local/lib/mecab/dic/mecab-ipadic-neologd scraped/2018-06.txt | grep "名詞" | cut -f 1 | sort | uniq -c | sort -r -n > result/2018-06.txt
mecab -d /usr/local/lib/mecab/dic/mecab-ipadic-neologd scraped/total.txt | grep "名詞" | cut -f 1 | sort | uniq -c | sort -r -n > result/total.txt