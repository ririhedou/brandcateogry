"""
scan the phishing Tank for suspicious URLs
"""
__author__ = 'ketian'
__version__ = '0.01a'
__email__ = 'ririhedou@gmail.com'

import tldextract
import collections


def read_complete_domain_list(fname):

    f = open(fname, 'r')

    subdomains = list()

    domain_dict = collections.defaultdict(list)

    for line in f.readlines():
        text = line.strip()

        ex = tldextract.extract(text)
        # ExtractResult(subdomain='forums.news', domain='cnn', suffix='com')
        if ex.subdomain:
            tmp = ex.subdomain + '.' + ex.domain + '.' + ex.suffix
            if tmp not in subdomains:
                subdomains.append(tmp)

        domain = ex.domain + '.' + ex.suffix
        domain_dict[ex.domain].append(domain)

    # print (subdomains)
    # print (domain_dict)

    pure_domains = []
    for i in domain_dict:
        pure_domains.append(domain_dict[i][0])

    pure_domains = sorted(pure_domains)
    print ("h", pure_domains)


fname = 'the_complete_list.domain'
read_complete_domain_list(fname)

subdomains = ['abcnews.go.com', 'abr.business.gov.au', 'answers.yahoo.com', 'auto.qq.com', 'auto.sina.com.cn', 'auto.sohu.com', 'baike.baidu.com', 'blog.csdn.net', 'blog.e-gold.com', 'blog.sina.com.cn', 'blog.sohu.com', 'citeseerx.ist.psu.edu', 'cn.bing.com', 'developer.android.com', 'dict.leo.org', 'dictionary.cambridge.org', 'docs.google.com', 'doctor.webmd.com', 'ec.europa.eu', 'economictimes.indiatimes.com', 'emedicine.medscape.com', 'en.wikipedia.org', 'en.wiktionary.org', 'fafsa.ed.gov', 'fallout.wikia.com', 'fantasy.nfl.com', 'finance.yahoo.com', 'football.fantasysports.yahoo.com', 'forms.netsuite.com', 'forum.gsmhosting.com', 'hao.360.cn', 'ibank.gtbank.com', 'login.live.com', 'mail.google.com', 'mail.qq.com', 'mail.yahoo.com', 'map.baidu.com', 'mlb.mlb.com', 'money.cnn.com', 'ncbi.nlm.nih.gov', 'news.baidu.com', 'news.google.com', 'news.qq.com', 'news.sina.com.cn', 'news.sohu.com', 'news.yahoo.com', 'niams.nih.gov', 'nichd.nih.gov', 'niddk.nih.gov', 'nimh.nih.gov', 'nlm.nih.gov', 'online.citi.com', 'onlinelibrary.wiley.com', 'outlook.live.com', 'pan.baidu.com', 'personal.natwest.com', 'personal.rbs.co.uk', 'play.google.com', 'plus.google.com', 'post.japanpost.jp', 'profootballtalk.nbcsports.com', 'runescape.wikia.com', 'scratch.mit.edu', 'search.yahoo.com', 'sports.qq.com', 'sports.sina.com.cn', 'sports.sohu.com', 'sports.yahoo.com', 'store.steampowered.com', 'support.microsoft.com', 'tech.sina.com.cn', 'timesofindia.indiatimes.com', 'translate.google.com', 'travel.state.gov', 'usa.visa.com', 'v.qq.com', 'wenku.baidu.com', 'www.tax.service.gov.uk', 'yule.sohu.com', 'zh.wikipedia.org']
