from constants import PLAYERS
from constants import TEAMS
import copy   

player_data = copy.deepcopy(PLAYERS)



def clean_data(player_data):
    cleaned = []
    for user in player_data:
        fixed = {}
        fixed["name"] = user["name"]
        fixed["height"] = int(user["height"].split(" ")[0])
        if user["experience"] == "YES":
            fixed["experience"] = True
        else:
            fixed["experience"] = False
        fixed["guardians"] = user["guardians"].split("and")
        cleaned.append(fixed)
    return cleaned

clean_players = clean_data(player_data)

def balance_teams(clean_players):
    experienced = []
    non_experienced = []
    for user in clean_players:
        if user["experience"] == True:
            experienced.append(user)
        else:
            non_experienced.append(user)
    print(f"experienced: {experienced}")
    print(f"not experienced: {non_experienced}")
    
   
        
    
    
    


    
    
    


if __name__ == "__main__" :
    balance_teams(clean_players)
    