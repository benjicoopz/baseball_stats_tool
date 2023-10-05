from constants import PLAYERS
from constants import TEAMS
import copy   
import sys

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



new_teams = []
def balance_teams(player_data):
    experienced = []
    non_experienced = []
    
    for user in player_data:
        if user["experience"] == True:
            experienced.append(user)
        else:
            non_experienced.append(user)
            
    
    
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

    

    
    
            
def menu():
    while True:            
        print("BASKETBALL TEAM STATS TOOL")
        print("\n---MENU---")
        print("\nHere are your choices:")
        print("\n1) Display Team Stats")
        print("2) Quit")
        try:
                option = input("\nEnter an option: ")
                if option == "1":
                    menu2()
                    break
                elif option == "2":
                    print("Thanks for checking out the stats!")
                    sys.exit()
                else:
                    raise Exception("Please enter 1 or 2")
        except Exception as e:
                print(e)
    
    
def menu2():
    team_total = len(new_teams)
    for index, team in enumerate(new_teams):
        print(f"\n{index + 1}) {team['team_name']}")
    while True:
        option2 = input("\nEnter an option: ")
        if option2 == "1":
            print(f"\nTeam:{0}{team['team_name']} Stats")
            print("--------------------------")
            print("Total players: ", )
            print("Players on Team: ")
            print("Karl Saygan, Les Clay, Herschel Krustofski, Matt Gill, Joe Kavalier, Eva Gordon")
            
            
    


    
    
    
    
    
            
            
            
            
            
if __name__ == "__main__":
    clean_players = clean_data(player_data)                
    balance_teams(clean_players)
    menu()
               
            
            
            
            