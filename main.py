import webapp2
import json
import itertools, random

class MainPage(webapp2.RequestHandler):
    def get(self):

        # make a deck of cards
        deck = list(itertools.product(range(1,14),['s','h','d','c']))
        # shuffle the cards
        random.shuffle(deck)
        # draw five cards
        card_url = "https://slack-175822.appspot.com/cards/%s%02d.bmp" % (deck[0][1], deck[0][0])

        obj = {
            "response_type": "in_channel",
            "attachments": [
                {
                    "image_url": card_url
                }
            ]
        }

        self.response.headers['Content-Type'] = 'application/json'
        self.response.write(json.dumps(obj))


app = webapp2.WSGIApplication([
    ('/', MainPage),
], debug=True)
