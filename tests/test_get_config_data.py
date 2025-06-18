from utils.myconfigparser import *

def test_get_gmail_url():
    assert getGmailUrl() == 'qa.gmail.com'