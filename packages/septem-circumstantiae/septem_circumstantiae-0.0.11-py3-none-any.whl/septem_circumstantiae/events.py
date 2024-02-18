# -*- coding: utf-8 -*-
# Python

"""Copyright (c) Alexander Fedotov.
This source code is licensed under the license found in the
LICENSE file in the root directory of this source tree.
"""

# https://alxfed.github.io/blog/posts/2019/02/22/Septem-Circumstantiae.html
circumstantiae = [
    'who', 'what', 'when', 'where', 'why', 'how', 'by_what_means'
]


class Event:
    """ Seven Circumstances, Copyright (c) Aristotle."""
    who: str            = ''  # quis. Who did it or who is reporting a natural event?
    what: str           = ''  # quid. What happened and was observed?
    when: str           = ''  # quando. When did it happen or started happening?
    where: str          = ''  # ubi. Where did it take place?
    why: str            = ''  # cur (for the sake of what?). Is there a cause or reason for the event?
    how: str            = ''  # quem ad modum (in what way?). How did it happen?
    by_what_means: str  = ''  # quibus adminiculis. How was it achieved? Were there any other factors involved?

    """ The story about the event """
    story: str = ''

    def __init__(self, **kwargs):
        for key,value in kwargs.items():
            setattr(self, key, value)
        self.quis = self.who

    @property
    def quis(self):
        self.quis = self.who
        return self.quis

    @quis.setter
    def quis(self, who: str):
        self.quis = who
        self.who = who

    @quis.deleter
    def quis(self):
        del self.quis

    def __call__(self, **kwargs):
        for key,value in kwargs.items():
            setattr(self, key, value)
        return self

    def __repr__(self, *args, **kwargs):
        return f"""     Event:
            who - {self.who},
            what - {self.what},
            when - {self.when},
            where - {self.where},
            why - {self.why},
            how - {self.how},
            by what means - {self.by_what_means}
            
            story - {self.story}
            """


if __name__ == '__main__':
    # For testing
    keyword_arguments = {
        'who': 'I',
        'what': 'do',
        'when': 'now',
        'where': 'here',
        'why': 'because',
        'how': 'in a most simple way',
        'by_what_means': 'manually'
    }
    some_event = Event(**keyword_arguments)
    print(some_event)
