import re
from urllib.request import urlopen
from bs4 import BeautifulSoup

from github import Github, Issue
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

issue_body = str(r_c) + " 명 입니다."
issue_title = "hello github Action! 89명 이하 입니다."
GITHUB_TOKEN = "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"
# GITHUB_TOKEN = os.environ["GITHUB_TOKEN"]
REPO_NAME = "koreatt"
repo = Github(GITHUB_TOKEN).get_user().get_repo(REPO_NAME)
if r_c <= 89 and REPO_NAME == repo.name:
    res = repo.create_issue(title=issue_title, body=issue_body)
    print(res)
else:
    res = repo.create_issue(title="빈자리가 없네요", body="돌아가")

