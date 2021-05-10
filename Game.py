import datetime
import pytz
import os


class Game(object):
    """Class Game - methods to extract various data pieces of the Game dictionary"""

    def __init__(self, game_dict):
        self.game_dict = game_dict

    def game_id(self):
        return self.game_dict['game_id']

    def game_time(self):
        return self.game_dict['game_datetime']

    def home_name(self):
        return self.game_dict['home_name']

    def away_name(self):
        return self.game_dict['away_name']

    def home_probable_pitcher(self):
        return self.game_dict['home_probable_pitcher'] or 'TBD'

    def away_probable_pitcher(self):
        return self.game_dict['away_probable_pitcher'] or 'TBD'

    def venue_name(self):
        return self.game_dict['venue_name']

    def summary_info(self):
        # datetime info is stored as UTC, extract the 'trailing Z' from the string
        utc_datetime = datetime.datetime.fromisoformat(self.game_time()[:-1])
        utc_datetime = utc_datetime.replace(tzinfo=pytz.utc)
        local_timezone = pytz.timezone("US/Eastern")
        local_datetime = utc_datetime.astimezone(local_timezone)

        return '{} {} at {}, SP: {} vs {}{}'.format(local_datetime.strftime("%H:%MET"),
                                                  self.away_name(),
                                                  self.home_name(),
                                                  self.away_probable_pitcher(),
                                                  self.home_probable_pitcher(),
                                                  os.linesep,
                                                  )
