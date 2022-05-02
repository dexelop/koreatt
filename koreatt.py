import re
from urllib.request import urlopen
from bs4 import BeautifulSoup

from github import Github, Issue
from github_utils import get_github_repo, upload_github_issue
import datetime
from pytz import timezone
from dateutil.parser import parse
import os

# site = "http://www.koreatakgu.com/seoul/2017/Do.jsp?urlSeq=1105&ldf=D&raceSeq=1249"
# res = urlopen(site)
# soup = BeautifulSoup(res, "html.parser")
# reg_count = soup.select_one("td:nth-child(2) > a > span").string
# r_c = int(reg_count.split("명")[0])
r_c = 10

if r_c <= 89:
    print("접수하세요~")
else:
    print("대기합니다.")

issue_title = "hello github Action! 89명 이하 입니다."
upload_contents = "contents 입니다."
access_token = os.environ["GITHUB_TOKEN"]
repository_name = "koreatt"
repo = get_github_repo(access_token, repository_name)

print(repo)
if r_c <= 89:
    upload_github_issue(repo, issue_title, upload_contents)
    print("Upload Github Issue Success!")
else:
    print("nothin happen")
