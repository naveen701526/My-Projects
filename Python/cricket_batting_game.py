
import random
import time
players_list = ["Rohit Sharma:4", "Aditya Singh:4", "Virat Kohli:5", "Shreyas Iyer:3", "KL Rahul:4", "Hardik Pandaya:2", "Krunal Pandaya:2", "Bhuvneshwar Kumar:1", "Shardul Thakur:1", "Yuzvendra Chahal:1", "Jasprit Bumrah:1"]
# default values

player1 = players_list[0]
player2 = players_list[1]
player_stars = [3, 3, 4, 2, 3, 2, 2, 1, 1, 1, 1]
player1_runs = 0
player1_balls = 0
player1_fours = 0
player1_sixes = 0
player2_runs = 0
player2_balls = 0
team_wickets = 0
player2_fours = 0
player2_sixes = 0
team_runs = 0
try:
    player1_strike_rate = (player1_runs / player1_balls) * 100
    player2_strike_rate = (player2_runs / player2_balls) * 100
except:
    player1_strike_rate = 0
    player2_strike_rate = 0
team_strike_rate = 0
runs_option_list = [1,2,2,3,3,3,4,4,4,6,6,6,6]
bowlers_list = ["Glenn Macrga","Jimmy Anderson", "Josh Hazelwood", "Muttiah Murlidharan", "Shane Warne", "Mitchell Starc"]
bowlers_over_list = [0, 0, 0, 0, 0, 0, 0]
bowler_run_list = [0, 0, 0, 0, 0, 0, 0]
bowler_wicket_list = [0, 0, 0, 0, 0, 0, 0]
bowler_bowls = 0
bowler = random.choice(bowlers_list)
team_overs = 0
team_bowls = 0
strike = 'player1'
while True:
    def current_bowler():
        for index, i in enumerate(bowlers_list):
            index+=1
            if i == bowler:
                return index
    def select_bowler():
        while True:
            newbowler = random.choice(bowlers_list)
            if newbowler == bowler:
                continue
            elif newbowler != bowler:
                break
        return newbowler
    def player_finder(given_player):
        for j,i in enumerate(players_list):
            
            if i == given_player:
                return int(j)
            j+=1
            
    def bowler_update():
        global team_bowls
        global team_overs
        global bowler_bowls
        global bowlers_over_list
        global bowler_run_list
        global bowler
        global strike
        if bowler_bowls == 6:
            bowlers_over_list[int(current_bowler())] = bowlers_over_list[int(current_bowler())] + 1
            bowler_bowls = 0

            
            bowler = select_bowler()
        if team_bowls == 6:
            team_overs+=1
            team_bowls = 0


    bowler_choice = random.choice(runs_option_list)
    if strike == 'player1':
        try:
            user_choice = int(input(f'Team Score: {team_runs}-{team_wickets}\n{player1.split(":")[0]}: {player1_runs}*|{player1_balls}, {player1_fours} Fours, {player1_sixes} Sixes || Strike Rate: {player1_strike_rate}\n{player2.split(":")[0]}: {player2_runs}|{player2_balls}, {player2_fours} Fours, {player2_sixes} Sixes || Strike Rate: {player2_strike_rate}\nCurrent Bowler: {bowler}|| {bowlers_over_list[int(current_bowler())]}.{bowler_bowls}-{bowler_wicket_list[current_bowler()]}-{bowler_run_list[current_bowler()]}\nOvers: {team_overs}.{team_bowls}\nEnter your Number: '))
        except:
            if user_choice == "exit":
                exit()
            runlist = [1, 1, 1,1,3,3, 1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0, 0,0,0,0, 0, 0,0,0,0,0,0,0, 0, 0, 2,2, 4, 4, 6]
            user_choice = random.choice(runlist)
        print('_____________________________________________________________')
        if user_choice != bowler_choice:
            team_bowls+=1
            bowler_bowls+=1
            bowler_run_list[current_bowler()]+=user_choice
            bowler_update()
            if user_choice == 1 or user_choice == 3:
                player1_runs+=user_choice
                team_runs+=user_choice
                player1_balls+=1
                if user_choice == 4:
                    player1_fours+=1
                elif user_choice == 6:
                    player1_sixes+=1
                if team_bowls != 0:
                    strike = 'player2'
                player1_strike_rate = round((player1_runs / player1_balls) * 100, 2)
            
            else:
                player1_balls+=1
                if user_choice == 4:
                    player1_fours+=1
                elif user_choice == 6:
                    player1_sixes+=1
                player1_runs+=user_choice
                team_runs+=user_choice
                player1_strike_rate = round((player1_runs / player1_balls) * 100, 2)
                if team_bowls == 0:
                    strike = 'player2'
        elif user_choice == bowler_choice:            
            player1roll = player_finder(player1)
            try:
                player = players_list[player1roll]
            except:
                print(player_finder(player1))
            a = player.split(":")

            stars = a[1]
            new_stars = int(stars) - 1

            print(f"{player1} Fall of one Star: Remaining: {new_stars}")
            if new_stars == 0:
                print(f"Fall of wicket: {player1}\nRuns: {player1_runs}\nBalls: {player1_balls}\nWicket: {bowler}")

                players_list.remove(player1)
                
                player1 = players_list[player1roll + 1]
                if player1 == player2:
                    player1 = players_list[player1roll + 2]
                bowler_bowls+=1
                team_bowls+=1
                player1_runs = 0
                bowler_wicket_list[current_bowler()]+=1
                player1_balls = 0
                player1_sixes = 0
                player1_strike_rate = 0
                player1_fours = 0
                team_wickets+=1
            else:
                player1 = f"{player1.split(':')[0]}:{new_stars}"
                players_list[player1roll] = player1

            bowler_update()
            cb = current_bowler()



    if strike == 'player2':   
        try:
            user_choice = int(input(f'Team Score: {team_runs}-{team_wickets}\n{player1.split(":")[0]}: {player1_runs}|{player1_balls}, {player1_fours} Fours, {player1_sixes} Sixes || Strike Rate: {player1_strike_rate}\n{player2.split(":")[0]}: {player2_runs}*|{player2_balls}, {player2_fours} Fours, {player2_sixes} Sixes || Strike Rate: {player2_strike_rate}\nCurrent Bowler: {bowler}|| {bowlers_over_list[int(current_bowler())]}.{bowler_bowls}-{bowler_wicket_list[current_bowler()]}-{bowler_run_list[current_bowler()]}\nOvers: {team_overs}.{team_bowls}\nEnter your Number: '))
        except:
            if user_choice=="exit":
                exit()
            runlist = [1, 1, 1,1,3,3, 0,1,0,0,0,0,1, 0,0,0,0,0,0,0,0,0,0,0,0, 0,0,0,0, 0,0,0,0,0,0,0 ,0, 0, 2,2, 4, 4, 6]
            user_choice = random.choice(runlist)
        print("______________________________________________________")
        if user_choice != bowler_choice:
            team_bowls+=1
            bowler_bowls+=1
            bowler_run_list[current_bowler()]+=user_choice
            
            bowler_update()
            if user_choice == 1 or user_choice == 3:
                
                player2_balls+=1
                if user_choice == 4:
                    player2_fours+=1
                elif user_choice == 6:
                    player2_sixes+=1
                player2_runs+=user_choice
                team_runs+=user_choice
                if team_bowls != 0:
                    strike = 'player1'
                
                player2_strike_rate = round((player2_runs / player2_balls) * 100, 2)

            else:
                player2_balls+=1
                if user_choice == 4:
                    player2_fours+=1
                elif user_choice == 6:
                    player2_sixes+=1
                player2_runs+=user_choice   
                team_runs+=user_choice    
                player2_strike_rate = round((player2_runs / player2_balls) * 100, 2)
                if team_bowls == 0:
                    strike = 'player1'
        elif user_choice == bowler_choice:
            player2roll = player_finder(player2)
            try:
                player = players_list[player2roll]
            except:
                print(player_finder(player2))
            a = player.split(":")

            stars = a[1]
            new_stars = int(stars) - 1
            print(f"{player2} Fall of one Star: Remaining: {new_stars}")
            if new_stars == 0:

                print(f"Fall of wicket: {player2}\nRuns: {player2_runs}\nBalls: {player2_balls}\nWicket: {bowler}")

                players_list.remove(player2)
                
                player2 = players_list[1]
                if player2 == player1:
                    player2 = players_list[2]

                team_wickets+=1

                cb = current_bowler()
                bowler_wicket_list[cb]+=1
                player2_runs = 0
                player2_balls = 0
                player2_sixes = 0
                player2_strike_rate = 0
                player2_fours = 0
            else:
                player2 = f"{player2.split(':')[0]}:{new_stars}"
                players_list[player2roll] = player2
            bowler_bowls+=1
            team_bowls+=1
            bowler_update()
            
            
