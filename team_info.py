import statsapi
from util_logger import setup_logger
import logging
from Team import Team
import sys

def team_info():
    #teams = statsapi.get('teams',{'sportIds':1,'activeStatus':'Yes','fields':'teams,name,id,division,league'})
    team_dict ={}
    teams = statsapi.get('teams', {'sportIds': 1, 'activeStatus': 'Yes'})
    for team in teams['teams']:
        team_dict[team['id']] = Team(team)

    return team_dict


if __name__ == '__main__':
    setup_logger('teams', 'c:/Temp', logging.DEBUG)
    team_dict = team_info()
    buffer = []
    for team_id in team_dict.keys():
        buffer.append(team_dict[team_id].summary_info())
    buffer.sort()
    for buf in buffer:
        print (buf)
    logging.info("normal termination")
    sys.exit(0)