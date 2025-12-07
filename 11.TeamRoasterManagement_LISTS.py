import copy

teams = []

def add_team():
    teams.append([input("Add a team").strip()])
    print("Team added")

def add_player():
    if not teams:
        print("No team available!Add a first team!")
        return

    for i in range(len(teams)):
        print(f"{i+1}.{teams[i][0]}")
    idx = int(input("Enter team number:"))-1
    if 0 <= idx < len(teams):
        teams[idx].append(input("Enter player name: ").strip())
        print("Player added!")
    else:
        print("Invalid team number!")

def view_teams():
    if not teams:
        print("No teams available.")
        return
    for team in teams:
        print(f"\nTeam: {team[0]}")
        print("\n".join(team[1:]) if len(team)>1 else "No players!")

def sort_team():
    if not teams:
        print("No teams available.")
        return

    idx = int(input("Enter teamnumber to sort"))-1
    if 0 <= idx < len(teams) and len(teams[idx])>1:
        teams[idx][1:].sort()
        print("Team sorted!")
    else:
        print("Invalid team or no players to sort")


def copy_team():
    if not teams:
        print("Enter team number to copy")
        return
    idx = int(input("Enter the team number to copy: "))-1
    if 0 <= idx < len(teams):
        print("Deep copy created", copy.deepcopy(teams[idx]))
    else:
        print("Invalid team number!")

def main():
    while True:
        choice = input("\n 1.Add Team 2.AddPlayer 3.ViewTeams 4. SortPlayer 5.CopyTeam 6.Exit \n Enter choice : ")
        if choice == "1":  add_team()
        elif choice == "2": add_player()
        elif choice == "3": view_teams()
        elif choice == "4": sort_team()
        elif choice == "5": copy_team()
        elif choice == "6":
            print("GoodBy")
            break
        else:
            print("Invalid option!")



main()







