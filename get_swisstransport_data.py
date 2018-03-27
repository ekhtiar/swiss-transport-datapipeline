import requests, argparse
from bs4 import BeautifulSoup
from datetime import datetime, timedelta

# Input parameters
parser = argparse.ArgumentParser()
parser.add_argument("-date", "--date", help="date of the file to download")
parser.add_argument("-write_path", "--write_path",
                    help="full path (incl. file name) of where the download file will be stored")
args = parser.parse_args()
download_date = args.date
write_path = args.write_path

# load the html of the page where data for everyday is listed
html = requests.get('https://opentransportdata.swiss/de/dataset/istdaten')
# parse html using beautiful soup
soup = BeautifulSoup(html.content, 'html.parser', from_encoding="utf-8")

# loop over all the heading class to find get to the right link for the given date
for data in soup.findAll(class_="heading"):
    if download_date in data.text:
        href = 'https://opentransportdata.swiss' + data.get('href')
        # go to the link and get the download url for data
        html_page = requests.get(href)
        soup_page = BeautifulSoup(html_page.content, 'html.parser', from_encoding="utf-8")
        download_link = soup_page.find(class_="resource-url-analytics").get('href')
        break

# download data and write the file
response = requests.get(download_link, stream=True)

with open(write_path, "wb") as handle:
    for data in response.iter_content():
        handle.write(data)
