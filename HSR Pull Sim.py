#Takes in number of Stellar Jades and Number of times you wish to run the simulator as inputs. Returns the average number of 5 star characters pulled over the number of sims run.

import random
fifty_fifty_chance = 564 #the chance of winning 50-50 in HSR is 564/1000
five_star_base_chance = 6 #the base chance of rolling a 5 star character in HSR is before 75 is 6/1000
pull_counter = 0 #internal tracker for soft/hard pity
event_five_star = 0 #counter for event featured 5 star char, won 5050 or hard pity
standard_five_star = 0 #counter for standard 5 star char losing 5050
fiftyfifty_loss = 0 #tracker for winning or losing 5050
pull_number_win = [] #list for tracking at what pull you won 5050
pull_number_lose = [] #list for tracking at what pull you lost 5050

num_of_pulls = int(int(input('Please enter the number of stellar jades you have'))/160)
n_sims = int(input('Please enter the number of times the simulator should run'))

for num in range(n_sims):
    for passes in range(num_of_pulls):
        pull_counter +=1
        if pull_counter < 74:
            five_star_base_chance = 6
        if pull_counter >= 74:
            five_star_base_chance += 60 
        if random.randint(1, 1000) <= five_star_base_chance and fiftyfifty_loss == 0: #pulled a 5 star, not on hard pity
            fiftyfifty_loss = random.randint(0,1000) #check if lose or win 5050
            if fiftyfifty_loss > 564:
                standard_five_star += 1
                pull_number_lose.append(pull_counter)
                pull_counter = 0
                five_star_base_chance = 6
            else:
                event_five_star += 1
                pull_number_win.append(pull_counter)
                pull_counter = 0
                five_star_base_chance = 6
                fiftyfifty_loss = 0
        elif random.randint(1, 1000) <= five_star_base_chance and fiftyfifty_loss != 0: #pulled 5 star on hard pity
            event_five_star += 1
            pull_number_win.append(pull_counter)
            pull_counter = 0
            five_star_base_chance = 6
            fiftyfifty_loss = 0

print (f"On average, you pulled {int(event_five_star/n_sims)} event five stars on pull number {int(sum(pull_number_win)/len(pull_number_win))}. You pulled {int(standard_five_star/n_sims)} standard five stars on pull(s) number {int(sum(pull_number_lose)/len(pull_number_lose))}.")
    
        
    
