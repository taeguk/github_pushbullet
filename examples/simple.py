#-*- coding: utf-8 -*-

from github_pushbullet import (
    GithubAccount,
    GithubPushbullet,
)

account = GithubAccount("username", "password")
gp = GithubPushbullet(account, "access_token")
gp.run()    # infinite loop
# gp.run(5) # check github's events every 5 seconds.
