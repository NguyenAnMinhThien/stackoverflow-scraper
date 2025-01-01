import re
import requests
import sys
from bs4 import BeautifulSoup
import pandas
import os

session = requests.Session()


def get_url(tag, page_num):
    tags = tag.split(" ")
    tags = [x.strip() for x in tags]
    if tags.__len__() > 1:
        search_tag = str.join("%2b", tags)
    else:
        search_tag = tags[0]
    url = f"https://stackoverflow.com/questions/tagged/{search_tag}?tab=votes&page={page_num}&pagesize=50"
    return url


def load_page(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36',
        'Accept-Language': 'en-US, en;q=0.5'}
    try:
        r = session.get(url=url, headers=headers)
        if r.status_code == 200:
            return r
    except Exception as e:
        print("Something wrong.", e)


def extract_page(tag, page_num):
    url = get_url(tag, page_num)
    r = load_page(url)

    try:
        soup = BeautifulSoup(r.content, features="html.parser")
        my_df = pandas.DataFrame(columns=['Votes', 'Title', 'Summary'])
        contents = soup.find_all("div", class_="s-post-summary js-post-summary")
        if contents == []:
            sys.exit(
                f"Please check again your tag name. The tag '{tag}' is not exist.\nCheck the following URL:\nhttps://stackoverflow.com/tags")
        for content in contents:
            vote = (content.find("span", class_="s-post-summary--stats-item-number").get_text().strip())
            title = (content.find("h3", class_="s-post-summary--content-title").get_text().strip())
            summary = (content.find("div", class_="s-post-summary--content-excerpt").get_text().strip())
            if vote == "" or title == "" or summary == "":
                sys.exit(f"The page html has change element structure.")
            dftemp = pandas.DataFrame({'Votes': [vote], 'Title': [title], 'Summary': [summary]})
            my_df = my_df._append(dftemp, ignore_index=True)
    except Exception as e:
        print("Something wrong: ", e)
    else:
        return my_df


def extract_all_page(tag, page_nums):
    my_df = pandas.DataFrame()
    for page in range(1, int(page_nums) + 1):
        df = extract_page(tag=tag, page_num=page)
        my_df = my_df._append(df, ignore_index=True)
    return my_df


def get_file_name(tag, page_num):
    tags = tag.split(" ")
    tags = [x.strip() for x in tags]
    if tags.__len__() > 1:
        search_tag = str.join("-", tags)
    else:
        search_tag = tags[0]
    filename = f"{search_tag}-{page_num}p.csv"
    if os.name == "nt":
        # window
        filepath = os.getcwd() + "\\output\\" + filename
    else:
        # other
        filepath = os.getcwd() + "/output/" + filename
    return filename, filepath
