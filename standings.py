import statsapi


def standings():
    standings = statsapi.standings(leagueId="103,104",
                                   division="all",
                                   include_wildcard=True,
                                   season=None,
                                   standingsTypes=None,
                                   date=None, )
    return standings

def standings_data():
    standings_data = statsapi.standings_data(
            leagueId="103,104",
            division="all",
            include_wildcard=True,
            season=None,
            standingsTypes=None,
            date=None,)
    return standings_data

if __name__ == '__main__':
    standings = standings()
    print (standings)

    standings_data = standings_data()
    print (standings_data)