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
    for index, team in enumerate(new_teams):
        print(f"\n{index + 1}) {team['team_name']}")
    while True:
        try:
            option2 = input("\nEnter an option: ")
            if option2 == "1":
                print(f"\nTeam: {new_teams[0]['team_name']} Stats")
                print("--------------------------")
                print("Total players: ", len(new_teams[0]["players"]))
                print("\nPlayers on Team: \n")
                team1_players = []
                for player in new_teams[0]['players']:
                    team1_players.append(player['name'])
                team1_playerzz = ", ".join(team1_players)
                print(team1_playerzz)
                input("\nPress anything to continue: ")
                menu()
            elif option2 == "2":
                print(f"\nTeam: {new_teams[1]['team_name']} Stats")
                print("--------------------------")
                print("Total players: ", len(new_teams[1]["players"]))
                print("\nPlayers on Team: \n")
                team2_players = []
                for player in new_teams[1]['players']:
                    team2_players.append(player['name'])
                team2_playerzz = ", ".join(team2_players)
                print(team2_playerzz)
                input("\nPress anything to continue: ")
                menu()
            elif option2 == "3":
                print(f"\nTeam: {new_teams[2]['team_name']} Stats")
                print("--------------------------")
                print("Total players: ", len(new_teams[2]["players"]))
                print("\nPlayers on Team: \n")
                team3_players = []
                for player in new_teams[2]['players']:
                    team3_players.append(player['name'])
                team3_playerzz = ", ".join(team3_players)
                print(team3_playerzz)
                input("\nPress anything to continue: ")
                menu()
            else:
                raise Exception("Please enter 1-3 to view stats")
        except Exception as err:
            print(err)
            
            
           
            
       
                
            
    


    
    
    
    
    
            
            
            
            
            
if __name__ == "__main__":
    clean_players = clean_data(player_data)                
    balance_teams(clean_players)
    menu()
    
               
            
            
            
            