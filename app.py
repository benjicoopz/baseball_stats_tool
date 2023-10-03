from constants import PLAYERS
from constants import TEAMS
import copy   

player_data = copy.deepcopy(PLAYERS)
team_data = copy.deepcopy(TEAMS)


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
        fixed["guardians"] = user["guardians"].split(" and ")
        cleaned.append(fixed)
    return cleaned


def balance_teams(player_data):
    experienced = []
    non_experienced = []
    for user in player_data:
        if user["experience"] == True:
            experienced.append(user)
        else:
            non_experienced.append(user)
    print(f"experienced: {experienced}")
    print(f"not experienced: {non_experienced}")
    
    new_teams = []
    for team in team_data:
        team_object = {team: {"players": []}}
        new_teams.append(team_object)
    while experienced:
        for team in team_data:
            popped = experienced.pop(0)
            popped.append(new_teams)
            
        
            
        
            
           
            
         
          
            
    
   
        
    
    
    


    
    
    


if __name__ == "__main__" :
    clean_data(player_data)
    clean_players = clean_data(player_data)
    balance_teams(clean_players)
    
    