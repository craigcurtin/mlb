import re
from collections import namedtuple
from collections import defaultdict

Position = namedtuple('Position', 'pos name')

valid_positions = ['P', 'C', '1B', '2B', '3B', 'SS', 'LF', 'CF', 'RF']

class Roster(object):
    def __init__(self, teamId, roster_list):
        self.teamId = teamId
        self.uniform_number_dict = {}
        self.position_dict = defaultdict(list)
        self.roster_list = roster_list
        for player in roster_list:
            if len(player) == 0:
                continue
            uniform_number, position, name = re.split(r"\s{2,}", player)
            self.uniform_number_dict[uniform_number[1:]] = Position(position, name)
            self.position_dict[position].append(uniform_number[1:])
    def position(self, position):
        if position in valid_positions:
            return self.position_dict[position]
        else:
            return []
    def uniform_number(self, uniform_number):
        return self.uniform_number_dict[uniform_number]
    def roster(self):
        return self.roster

