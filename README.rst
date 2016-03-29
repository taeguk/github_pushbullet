Github Pushbullet
=====================

.. image:: https://img.shields.io/pypi/v/github_pushbullet.svg
    :target: https://pypi.python.org/pypi/github_pushbullet

.. image:: https://img.shields.io/pypi/dm/github_pushbullet.svg
    :target: https://pypi.python.org/pypi/github_pushbullet

Push github notifications to pushbullet.


Installation
-----------------

.. code-block:: bash

    $ pip install github_pushbullet


Simple Example
---------------
.. code-block:: python

    from github_pushbullet import (
      GithubAccount,
      GithubPushbullet,
    )
    
    account = GithubAccount("username", "password")
    gp = GithubPushbullet(account, "access_token")
    gp.run()    # infinite loop

`See more examples.
<https://github.com/taeguk/github_pushbullet/tree/master/examples>`_


Contributing
-----------------
Welcome! I'm waiting contributors!
