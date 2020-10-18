# Basim Siddiqui
# PSID: 1517778

class Team:
    def __init__(self):
        self.team_name = 'none'
        self.team_wins = 0
        self.team_losses = 0

    def set_team(self, team_name):
        self.team_name = team_name

    def set_wins(self, team_wins):
        self.team_wins = team_wins

    def set_losses(self, team_losses):
        self.team_losses = team_losses

    def get_win_percentage(self):
        percentage = self.team_wins / (self.team_wins + self.team_losses)
        return percentage

if __name__ == "__main__":
    team = Team()
    team_name = input()
    num_wins = int(input())
    num_losses = int(input())

    team.set_team(team_name)
    team.set_wins(num_wins)
    team.set_losses(num_losses)

    if team.get_win_percentage() >= 0.5:
        print("Congratulations, Team", team.team_name, "has a winning average!")
    else:
        print('Team', team.team_name, "has a losing average.")