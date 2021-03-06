class Team(object):
    name = ''
    score = 0.0


class Match(object):
    id = None
    teams = None
    running = 0
    link = None
    winner = None
    loser = None
    winner_matches = None
    loser_matches = None


class Phase(object):
    title = None
    link = None
    matches = []
    running = False

__all__ = ('Team', 'Match', 'Phase')
