import statsapi
from Team import Team
from datetime import datetime
from Roster import Roster
from Roster import valid_positions

def team_roster(teamId):
    team_roster = statsapi.roster(teamId, rosterType=None, season=datetime.now().year, date=None)
    return team_roster

if __name__ == '__main__':
    team_dict = {}
    teams = statsapi.get('teams', {'sportIds': 1, 'activeStatus': 'Yes'})
    for team in teams['teams']:
        team_dict[team['id']] = Team(team)
    league_roster_dict = {}
    for teamId in team_dict.keys():
        roster = team_roster(teamId)
        team_roster_list = roster.split('\n')
        league_roster_dict[teamId] = Roster(teamId, team_roster_list)
        print (team_dict[teamId].summary_info())
        for position in valid_positions:
             for uniform_number in league_roster_dict[teamId].position(position):
                 print ('{}, #{}, {}'.format(position,
                                             uniform_number,
                                             league_roster_dict[teamId].uniform_number(uniform_number)))



