import random as rd

def fight(robot1, robot2, tactics):
    n=0
    print(list(robot1.values()))
    print(list(robot2.values()))
    while (robot2['health'] >= 0 and robot1['health'] >= 0) and n<min(len(robot1['tactics']), len(robot2['tactics'])):
        if robot1['speed'] > robot2['speed']:
            robot1['health'] = robot1['health'] - tactics[robot2['tactics'][n]]
            robot2['health'] = robot2['health'] - tactics[robot1['tactics'][n]]
            if robot1['health'] == 0:
                return robot2['name'] +' has won the fight.'
        else:
            robot2['health'] = robot2['health'] - tactics[robot1['tactics'][n]]
            robot1['health'] = robot1['health'] - tactics[robot2['tactics'][n]]
            if robot1['health'] == 0:
                return robot1['name'] +' has won the fight.'
        n+=1
        
    if len(robot1['tactics']) == len(robot2['tactics']) == 0:
        return 'The fight was a draw.'
    elif robot1['health'] > robot2['health']:
        return robot1['name'] +' has won the fight.'
    elif robot2['health'] > robot1['health']:
        return robot2['name'] +' has won the fight.'
    elif len(robot2['tactics']) == 0:
        return robot1['name'] +' has won the fight.'
    elif len(robot1['tactics']) == 0:
        return robot2['name'] +' has won the fight.'
    else:
        return 'The fight was a draw.'

def bots():
    #Randomly generated test problems
    tactics = {"punch": 20, "laser": 30, "missile": 35, 'nuke': 50, 'Space-Laser': 100}
    robot_1 = {"name": "Rocky", "health": rd.randint(1,100), "speed": rd.randint(1,20), "tactics": rd.sample(list(tactics.keys()), rd.randint(0, len(tactics)))}
    robot_2 = {"name": "Missile Bob", "health": rd.randint(1,100), "speed": rd.randint(1,20), "tactics": rd.sample(list(tactics.keys()), rd.randint(0, len(tactics)))}
    return fight(robot_1, robot_2, tactics)

print(bots())