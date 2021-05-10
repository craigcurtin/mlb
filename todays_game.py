import statsapi
import datetime
from datetime import datetime as dt
from Game import Game
import logging
import sys
import os

from cc_mail import cc_mail
from util_logger import setup_logger
from yagmail import send_yag

def todays_game():
    today = datetime.date.today()
    tommorrow = today + datetime.timedelta(days=1)
    # sched = statsapi.schedule(start_date='07/01/2018', end_date='07/31/2018', team=143, opponent=121)
    statsapi.lookup_team(147)
    sched_games = statsapi.schedule(start_date=today, end_date=tommorrow)
    today_games = {}
    tomorrow_games = {}
    for game in sched_games:
        if today == dt.strptime(game['game_date'], '%Y-%m-%d').date():
            today_games[game['game_id']] = Game(game)
        else:
            tomorrow_games[game['game_id']] = Game(game)

    body = ""
    # now, print out Today's followed by Tommorrow's games
    body += "Today's Games: {}{}".format(today.isoformat(), os.linesep)
    for game in today_games:
        body += '{}'.format(today_games[game].summary_info())

    body += "Tommorrow's Games: {}{}".format(tommorrow.isoformat(), os.linesep)
    for game in tomorrow_games:
        body += '{}'.format(tomorrow_games[game].summary_info())
    return body


if __name__ == '__main__':
    setup_logger('todays_game', 'c:/Temp', logging.DEBUG)

    email_body = todays_game()
    cc_mail('curtin@computer.org', '{} MLB games'.format(datetime.date.today()), email_body)

    sys.exit(0)
