from constants import PLAYERS
from constants import TEAMS
import copy   
import sys

player_data = copy.deepcopy(PLAYERS)
team_data = copy.deepcopy(TEAMS)


print("BASKETBALL TEAM STATS TOOL")
print("\n---MENU---")
print("\nHere are your choices:")
print("\n1) Display Team Stats")
print("2) Quit")
while True:
    try:
        option = input("\nEnter an option: ")
        if option == "1":
            print("1) Panthers")
            print("2) Bandits")
            print("3) Warriors")
            break
        elif option == "2":
            sys.exit()
        else:
            raise Exception("Please enter 1 or 2")
    except Exception as e:
        print(e)
    

    


    



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
    
    
    new_teams = []
    for team in team_data:
        team_object = {"team_name": team, "players": []}
        new_teams.append(team_object)
        
    while experienced:
        for team in new_teams:
            popped = experienced.pop(0)
            team["players"].append(popped)
            
    while non_experienced:
        for team in new_teams:
            popped2 = non_experienced.pop(0)
            team["players"].append(popped2)
            
            
if __name__ == "__main__" :
    clean_players = clean_data(player_data)
    balance_teams(clean_players)
    
    