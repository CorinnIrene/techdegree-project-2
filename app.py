import constants

players = []
for player in constants.PLAYERS:
    players.append(player)
teams = []
for team in constants.TEAMS:
    teams.append(team)

experienced = []
not_experienced = []


def clean_data(data):
    for player in data:
        for key in player:
            if key == "height":
                num = player[key].split()
                player[key] = int(num[0])
            if key == "guardians":
                guardian = player[key].split(' and ')
                player[key] = guardian
            if key == 'experience':
                if player[key] == "YES":
                    player[key] = True
                    experienced.append(player)
                elif player[key] == "NO":
                    player[key] = False
                    not_experienced.append(player)


def balance_teams():
    teams[0] = experienced[:3] + not_experienced[:3]
    teams[1] = experienced[3:6] + not_experienced[3:6]
    teams[2] = experienced[6:] + not_experienced[6:]


def show_stats(lst):
    players = []
    experienced = []
    not_experienced = []
    total_height = 0
    guardians = []
    for player in lst:
        for key in player:
            if key == 'name':
                players.append(player[key])
            if key == 'experience':
                if player[key]:
                    experienced.append(player[key])
                else:
                    not_experienced.append(player[key])
            if key == 'height':
                total_height += player[key]
            if key == 'guardians':
                guardians.append(', '.join(player[key]))
    avg_height = round(total_height / len(players), 1)
    print("-" * 20)
    print(f"Total Players: {len(players)}")
    print(f"Total Experienced: {len(experienced)}")
    print(f"Total inexperienced: {len(not_experienced)}")
    print(f"Average height: {avg_height}")
    print("\nPlayers on team:")
    print(', '.join(players))
    print("\nGuardians:")
    print(', '.join(guardians))
    print('\n')
    input("Press any key to continue to  main menu\n")


def main_menu():
    run = True
    while run:
        print("BASKETBALL TEAM STATS TOOL\n")
        print("-" * 4 + "MENU" + "-" * 4 + "\n")
        print("Here are your choices:")
        print("A) Display Team Stats")
        print("B) Quit\n")
        stats_or_quit = input("What would you like to do? ")
        if stats_or_quit.lower() == 'a':
            print("\nA) Panthers\n"
                  "B) Bandits\n"
                  "C) Warriors\n\n")
            team_pick = input("Enter an option: ").lower()
            if team_pick == 'a':
                print("\nTeam: Panther Stats")
                show_stats(teams[0])
            elif team_pick == 'b':
                print('\nTeam: Bandit Stats')
                show_stats(teams[1])
            elif team_pick == 'c':
                print('\nTeam: Warrior Stats')
                show_stats(teams[2])
            else:
                print("Not valid input. Please try again.\n")
                continue

        elif stats_or_quit.lower() == 'b':
            run = False
            print("Thanks, have a great day!")
            break
        else:
            print("That is not a valid response. Please try again.\n")
            continue


if __name__ == '__main__':
    clean_data(players)
    balance_teams()
    main_menu()






