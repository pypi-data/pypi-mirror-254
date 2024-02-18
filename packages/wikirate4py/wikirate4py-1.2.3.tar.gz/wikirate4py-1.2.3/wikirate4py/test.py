import time

import wikirate4py
from wikirate4py import Cursor

api = wikirate4py.API('ThessaloWikiRate')

cursor = Cursor(api.get_answers_by_id,
                identifier=826615,
                year=2021,
                view='detailed',
                verification='community_verified'
                )

answers = []
while cursor.has_next():
    answers.extend(cursor.next())

