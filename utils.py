import re
import requests
import sys
from bs4 import BeautifulSoup
import pandas
import os

session = requests.Session()

# https://olr.gdc-uk.org/SearchRegister/SearchResult?RegistrationNumber={registeration_num}
def get_url(registeration_num ):
    url = f"https://olr.gdc-uk.org/SearchRegister/SearchResult?RegistrationNumber={registeration_num}"
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


def extract_page(registeration_num):
    url = get_url(registeration_num)
    r = load_page(url)

    try:
        soup = BeautifulSoup(r.content, features="html.parser")
        my_df = pandas.DataFrame()
        contents = soup.find_all("div", class_="card-header")
        contents_body = soup.find_all("div", class_="col-md-4 font-weight-bold")
        contents_result = soup.find_all("div", class_="col-md-6 col-sm-10")
        if contents == []:
            pass
        for name in contents[0].get_text().split("\n"):
            if name.strip() != "":
                Name = name.strip()
                break
        Registration_number = (contents_result[0].get_text().strip())
        First_registered_on = (contents_result[1].get_text().strip())
        dftemp = pandas.DataFrame({'Name': [Name], 'Registration_number': [Registration_number], 'First_registered_on': [First_registered_on]})
        # not use _append anymore
        my_df = pandas.concat([my_df,dftemp])
    except Exception as e:
        print("Something wrong: ", e)
    else:
        return my_df

def extract_all_page():
    dftemps = pandas.DataFrame()
    for i in range(79800,79900):
        dftemp = extract_page(i)
        dftemps = dftemps._append(dftemp,sort = False)
    return dftemps
def get_file_name():
    filename = f"Output.csv"
    if os.name == "nt":
        # window
        filepath = os.getcwd() + "\\output\\" + filename
    else:
        # other
        filepath = os.getcwd() + "/output/" + filename
    return filename, filepath

extract_page(79801)