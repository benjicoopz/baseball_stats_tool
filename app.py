from constants import PLAYERS
from constants import TEAMS
import copy   

player_data = copy.deepcopy(PLAYERS)


def clean_data(player_data):
    cleaned = []
    for user in player_data:
        fixed = {}
        fixed["height"] = int(user["height"].split(" ")[0])
        if user["experience"] == "YES":
            fixed["experience"] = True
        else:
            fixed["experience"] = False
        cleaned.append(fixed)
    return cleaned


def balance_teams(player_data):
    experienced = []
    non_experienced = []
    for user in player_data:
        if user["experience"] == "YES":
            experienced.append({"name"})
        else:
            non_experienced.append({"name"})
    
    
    
    


    
    
    


if __name__ == "__main__" :
    print(balance_teams(player_data))
    