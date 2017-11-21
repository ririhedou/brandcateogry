#!/usr/bin/env python
# -*- coding: utf-8 -*-
# this is python 2.7


__author__ = "ketian"
__time__ = "Jun 2017"

from bs4 import BeautifulSoup
import tldextract


def parse_html_pages(html):

    #<div class="td DescriptionCell">
    div_class = "td DescriptionCell"

    html_text = open(html,'r')
    soup = BeautifulSoup(html_text, "html.parser")
    mydivs = soup.findAll("div", { "class" : div_class })

    domains = []
    for each_div in mydivs:
        #print (each_div)
        href_Tags = each_div.find_all("a")
        a = href_Tags[0]
        domain_name = extract_domain_name(a.text)
        domains.append(domain_name.lower())
    return domains

def extract_domain_name(text):
    ex = tldextract.extract(text)
    #ExtractResult(subdomain='forums.news', domain='cnn', suffix='com')
    if ex.subdomain:
        tmp = ex.subdomain + '.' + ex.domain + '.' + ex.suffix
    else:
        tmp = ex.domain + '.' + ex.suffix
    return tmp


def iterate_all_htmls(files=None):

    all_domains = list()
    import glob
    htmls = glob.glob('./*.html')
    for html in htmls:
        t1 = parse_html_pages(html)
        print ("\n------------" +html.split('_')[-1])
        #for i in t1:
        #    print (i)
        all_domains.extend(t1)

    all_domains.extend(phishingtank_brand_extract())
    all_domains = sorted(list(set(all_domains)))

    for i in all_domains:
        print (i)
    return


def phishingtank_brand_extract():

    fname = "phishingTankBrand.domain"
    phishingDomains = list()

    f = open(fname, 'r')
    for line in f.readlines():
        line = line.strip()
        link = line.split('#')[-1]
        if not link.startswith('http'):
            continue
        domain_name = extract_domain_name(link)
        phishingDomains.append(domain_name)

    phishingDomains = list(set(phishingDomains))
    return phishingDomains

if __name__ == "__main__":
    test = "Alexa - Top Sites by Category_ Adult.html"
    test2 = "Alexa - Top Sites by Category_ Kids and Teens.html"
    iterate_all_htmls()