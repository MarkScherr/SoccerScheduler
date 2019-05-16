import copy
import pandas as pd
import random
team = {}
teamList = ['Hunter Scherr', 'Benjamin Leier', 'Carter Saiko', 'AJ Tannehill', 'Jack Leicht',\
			'Leam Hieserich', 'Logan Serpico', 'Aiden Cole', 'Alexander Gustafson', 'Alex Olson', \
			'Riley Steinert', 'Jackson Mach']

def create_team():
    global team
    for player in teamList:
        """
        [GoalieRank, DefenseRank, MidfieldRank, ForwardRank
        GoalieTurns, DefenseTurns, MidfieldTurns, ForwardTurns, benchTurns
        """
        team[player] = [0,0,0,0,0,0,0,0,0]
    print(team)

def set_rank(player, position, rank):
    global team
    team[player][position] = rank

def add_turn(player, position):
    global team
    if player is not '':
        team[player][position] = team[player][position] + 1

def get_fewest(position):
    global team
    fewestTurns = 9999
    for player in team:
        if team[player][position] < fewestTurns:
            fewestTurns = team[player][position]
    return fewestTurns

def get_best_ranked_remaining(usedPlayerList, position):
    global team
    best_rank = -1
    bestRanked = ''
    for player in team:
        if team[player][position] > best_rank and player not in usedPlayerList:
            bestRanked = player
            best_rank = team[player][position]
    return bestRanked

def get_lowest_ranked_remaining(usedPlayerList, position):
    global team
    lowest_rank = 999999999999999
    lowestRanked = ''
    for player in team:
        if team[player][position] < lowest_rank and player not in usedPlayerList:
            lowestRanked = player
            lowest_rank = team[player][position]
    return lowestRanked

def get_player(usedPlayerList, fewestTurns, isHighRankPick, rating, element):
    global team
    tempUsed = copy.deepcopy(usedPlayerList)
    player = ''
    count = 0
    playersTurns = 999999999999999
    while playersTurns > fewestTurns or player is '':
        if isHighRankPick:
            player = get_best_ranked_remaining(tempUsed, rating)
        else:
            player = get_lowest_ranked_remaining(tempUsed, rating)

        if player is not '':
            playersTurns = team[player][element]
            tempUsed.append(player)
        count += 1
        if count == 11:
            fewestTurns += 1
            tempUsed = copy.deepcopy(usedPlayerList)
            count = 0
    add_turn(player, element)
    return player

def determine_order():
    global team
    schedule = {}
    for index in range(6):
        usedPlayerList = []

        fewestBenchTurns = get_fewest(8)
        fewestForwardTurns = get_fewest(7)
        fewestMidfieldTurns = get_fewest(6)
        fewestDefenseTurns = get_fewest(5)
        fewestGoalieTurns = get_fewest(4)


        bOne = get_player(usedPlayerList, fewestBenchTurns, False, 2 , 8)
        usedPlayerList.append(bOne)

        bTwo = get_player(usedPlayerList, fewestBenchTurns, True, 2 , 8)
        usedPlayerList.append(bTwo)

        bThree = get_player(usedPlayerList, fewestBenchTurns, False, 2 , 8)
        usedPlayerList.append(bThree)

        bFour = get_player(usedPlayerList, fewestBenchTurns, True, 2 , 8)
        usedPlayerList.append(bFour)

        bFive = get_player(usedPlayerList, fewestBenchTurns, False, 2 , 8)
        usedPlayerList.append(bFive)

        bSix = get_player(usedPlayerList, fewestBenchTurns, False, 2, 8)
        usedPlayerList.append(bSix)

        fOne = get_player(usedPlayerList, fewestForwardTurns, index % 2, 3, 7)
        usedPlayerList.append(fOne)

        # randomBit = random.randint(0, 1)
        # if randomBit == 1:
        #     trueOrFalse = True
        # else:
        #     trueOrFalse = False
        g = get_player(usedPlayerList, fewestGoalieTurns, index % 2, 0, 4)
        usedPlayerList.append(g)

        mTwo = get_player(usedPlayerList, fewestMidfieldTurns, False, 2, 6)
        usedPlayerList.append(mTwo)

        mOne = get_player(usedPlayerList, fewestMidfieldTurns, True, 2, 6)
        usedPlayerList.append(mOne)

        dOne = get_player(usedPlayerList, fewestDefenseTurns, True, 1, 5)
        usedPlayerList.append(dOne)

        dTwo = get_player(usedPlayerList, fewestDefenseTurns, False, 1, 5)
        usedPlayerList.append(dTwo)


        schedule[index] = {
            'goalie': g,
            'defenderOne': dOne,
            'defenderTwo': dTwo,
            'midfielderOne': mOne,
            'midfielderTwo': mTwo,
            'forwardOne': fOne,
            'benchOne': bOne,
            'benchTwo': bTwo,
            'benchThree': bThree,
            'benchFour': bFour,
            'benchFive': bFive,
            'benchSix': bSix
        }
        print(schedule)
    return schedule

def main():
    global team
    try:
        teamDF = pd.read_csv('team.csv')
        team = teamDF.to_dict()
        print(team)
    except:
        print('first run')
    if team == {}:
        create_team()
        set_rank('Hunter Scherr', 0, 0)
        set_rank('Hunter Scherr', 1, 0)
        set_rank('Hunter Scherr', 2, 0)
        set_rank('Hunter Scherr', 3, 0)

        set_rank('Benjamin Leier', 0, 0)
        set_rank('Benjamin Leier', 1, 0)
        set_rank('Benjamin Leier', 2, 0)
        set_rank('Benjamin Leier', 3, 0)

        set_rank('Carter Saiko', 0, 0)
        set_rank('Carter Saiko', 1, 0)
        set_rank('Carter Saiko', 2, 0)
        set_rank('Carter Saiko', 3, 0)

        set_rank('AJ Tannehill', 0, 0)
        set_rank('AJ Tannehill', 1, 0)
        set_rank('AJ Tannehill', 2, 0)
        set_rank('AJ Tannehill', 3, 0)

        set_rank('Jack Leicht', 0, 0)
        set_rank('Jack Leicht', 1, 0)
        set_rank('Jack Leicht', 2, 0)
        set_rank('Jack Leicht', 3, 0)

        set_rank('Leam Hieserich', 0, 0)
        set_rank('Leam Hieserich', 1, 0)
        set_rank('Leam Hieserich', 2, 0)
        set_rank('Leam Hieserich', 3, 0)

        set_rank('Logan Serpico', 0, 0)
        set_rank('Logan Serpico', 1, 0)
        set_rank('Logan Serpico', 2, 0)
        set_rank('Logan Serpico', 3, 0)

        set_rank('Aiden Cole', 0, 0)
        set_rank('Aiden Cole', 1, 0)
        set_rank('Aiden Cole', 2, 0)
        set_rank('Aiden Cole', 3, 0)

        set_rank('Alexander Gustafson', 0, 0)
        set_rank('Alexander Gustafson', 1, 0)
        set_rank('Alexander Gustafson', 2, 0)
        set_rank('Alexander Gustafson', 3, 0)

        set_rank('Alex Olson', 0, 0)
        set_rank('Alex Olson', 1, 0)
        set_rank('Alex Olson', 2, 0)
        set_rank('Alex Olson', 3, 0)

        set_rank('Riley Steinert', 0, 0)
        set_rank('Riley Steinert', 1, 0)
        set_rank('Riley Steinert', 2, 0)
        set_rank('Riley Steinert', 3, 0)

        set_rank('Jackson Mach', 0, 0)
        set_rank('Jackson Mach', 1, 0)
        set_rank('Jackson Mach', 2, 0)
        set_rank('Jackson Mach', 3, 0)


    schedule = determine_order()
    scheduleDataFrame = pd.DataFrame.from_dict(schedule)
    teamDataFrame = pd.DataFrame.from_dict(team)
    print(teamDataFrame)
    print (scheduleDataFrame)

    scheduleDataFrame.to_csv('schedule.csv')
    teamDataFrame.to_csv('team.csv', index=False)
    print(schedule)

main()
		
			
			
			
			
			
			
			
			
			
			
