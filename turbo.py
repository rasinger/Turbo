import os

import jinja2
import webapp2

import random

JINJA_ENVIRONMENT = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__) + '/templates')
)

class HomePage(webapp2.RequestHandler):
    def get(self):

        template = JINJA_ENVIRONMENT.get_template('index.html')
        template_values = {
          'hello': 'world'
        }
        phrases = [
            'Urban Communication Strategies',
            'Urban Communication Technologies',
            'Urban Communication Solutions',
            'Urban Communication Innovation',
            'Urban Information Technologies',
            'Urban Information Solutions',
            'Urban Information Strategies',
            'Urban Information Innovation',
            'Urban Solution Technologies',
            'Urban Innovation Strategies',
            'Urban Technology Communication'
        ]
        phrase = random.choice(phrases)
        template_values['phrase'] = phrase
        self.response.headers['Strict-Transport-Security'] = 'max-age=31536000'
        self.response.headers['P3P'] = 'max-age=31536000'
        self.response.write(template.render(template_values))


application = webapp2.WSGIApplication([
    ('/', HomePage),
], debug=True)
