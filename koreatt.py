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

upload_contents = "contents 입니다."
issue_title = "hello github Action! 89명 이하 입니다."
# GITHUB_TOKEN = "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"
access_token = os.environ["GITHUB_TOKEN"]
repository_name = "koreatt"
repo = get_github_repo(access_token, repository_name)

# repo = Github(GITHUB_TOKEN).get_repo(REPO_NAME)  # .get_user().get_repo(REPO_NAME)
print(repo)  # .name)
if r_c <= 89:  # and REPO_NAME == repo:  # .name
    upload_github_issue(repo, issue_title, upload_contents)
    # res = repo.create_issue(title=issue_title, body=issue_body)
    print("Upload Github Issue Success!")
else:
    pass


# issue_title = f"YES24 IT 신간 도서 알림({today_date})"
# upload_contents = extract_book_data(soup)
# repo = get_github_repo(access_token, repository_name)
# upload_github_issue(repo, issue_title, upload_contents)
# print("Upload Github Issue Success!")
