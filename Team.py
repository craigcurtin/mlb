import os

class Team (object):
    def __init__(self, team_dict):
        self.team_dict = team_dict
    def id(self):
        return self.team_dict['id']
    def name(self):
        return self.team_dict['name']
    def link(self):
        return self.team_dict['link']
    def season(self):
        return self.team_dict['season']
    def league_id(self):
        return self.team_dict['league']['id']
    def league_name(self):
        return self.team_dict['league']['name']
    def league_link(self):
        return self.team_dict['league']['link']
    def division_id(self):
        return self.team_dict['division']['id']
    def division_name(self):
        return self.team_dict['division']['name']
    def division_link(self):
        return self.team_dict['division']['link']
    def venue_id(self):
        return self.team_dict['venue']['id']
    def venue_name(self):
        return self.team_dict['venue']['name']
    def venue_link(self):
        return self.team_dict['venue']['link']
    def springVenue_id(self):
        return self.team_dict['springVenue']['id']
    def springVenue_link(self):
        return self.team_dict['springVenue']['link']
    def teamCode(self):
        return self.team_dict['teamCode']
    def fileCode(self):
        return self.team_dict['fileCode']
    def abbreviation(self):
        return self.team_dict['abbreviation']
    def teamName(self):
        return self.team_dict['teamName']
    def locationName(self):
        return self.team_dict['locationName']
    def firstYearOfPlay(self):
        return self.team_dict['firstYearOfPlay']
    def sport_id(self):
        return self.team_dict['sport']['id']
    def sport_name(self):
        return self.team_dict['sport']['name']
    def sport_link(self):
        return self.team_dict['sport']['link']
    def shortName(self):
        return self.team_dict['shortName']
    def springLeague_id(self):
        return self.team_dict['springLeague']['id']
    def springLeague_name(self):
        return self.team_dict['springLeague']['name']
    def springLeague_link(self):
        return self.team_dict['springLeague']['link']
    def springLeague_abbreviation(self):
        return self.team_dict['springLeague']['abbreviation']
    def allStarStatus(self):
        return self.team_dict['allStarStatus']
    def active(self):
        return self.team_dict['active']
    def summary_info(self):

        return '{}, play in {}, in {} at {} since: {}'.format( self.name(),
                                                #self.shortName(),
                                                #self.league_name(),
                                                 self.division_name(),
                                                     self.locationName(),
                                                     self.venue_name(),
                                                     self.firstYearOfPlay(),
                                                  os.linesep,
                                                  )