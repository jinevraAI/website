import threading
from mailchimp3 import MailChimp
import os
from django.conf import settings
from urllib.error import HTTPError

class SendSubscriberMail(object):
    def __init__(self, email):
        self.email = email
        thread = threading.Thread(target=self.run, args=())
        thread.daemon = True
        thread.start()

    def run(self):
        API_KEY = os.environ.get('MC_API', '')
        LIST_ID = os.environ.get('MC_LIST', '')
        client = MailChimp(mc_api=os.environ.get('MC_API', ''))
        try:
            client.lists.members.create(LIST_ID, data={
                'email_address': self.email,
                'status': 'subscribed',
                })
            return True
        except HTTPError as e:
            if e.response.status_code == 400:
                json = e.response.json()
                print("ERROR:", profile)
                raise MailChimpError(
                    json.get('errors') or json.get('detail') or json)
                return json
            else:
                print(e)
                print(profile)
                return False
