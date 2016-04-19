#-*- coding: utf-8 -*-

from pushbullet import Pushbullet
from github_listener import (
    GithubAccount,
    GithubListener,
)

class GithubPushbullet(object):
    def __init__(self, github_account, access_token):
        self.github_listener = GithubListener(github_account)
        self.access_token = access_token
    
    def run(self, sleep_sec = None):
        @self.github_listener.notification
        def on_notification(change):
            pb = Pushbullet(self.access_token)
            for group in change.n_groups:
                for n in group.notifications:
                    msg = u"Repo. : {0}\n".format(group.group_name)
                    msg += u"Title : {0}\nLink : {1}\nPerson : {2}\nText : {3}".format(n.title, n.link, n.person, n.text)
                    push = pb.push_note(u"Github Pushbullet - Notification", msg)
        if sleep_sec is None:
            self.github_listener.run()
        else:
            self.github_listener.run(sleep_sec)
