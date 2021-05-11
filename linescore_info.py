import statsapi
from teams_info import teams_info

if __name__ == '__main__':
    teams_dict = teams_info()
    for teamId in teams_dict.keys():
        most_recent_game_id = statsapi.last_game(teamId)
        print(statsapi.boxscore(most_recent_game_id))
        print(statsapi.linescore(most_recent_game_id))


    statsapi.linescore(gamePk, timecode=None)
    params = {
        "gamePk": gamePk,
        "fields": "gameData,teams,teamName,shortName,status,abstractGameState,liveData,linescore,innings,num,home,away,runs,hits,errors",
    }
