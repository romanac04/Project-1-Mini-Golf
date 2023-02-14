name = input("Welcome to GC mini golf! What is your name?")
holes = int(input(f" Hi{name}! Would you like to play 3 or 6 holes?"))
current_hole = 1
number_of_putts = 0

for current_hole in range(holes):
    number_of_putts += int(input("How many putts for hole " + str(current_hole + 1)+ "?(par is 3)"))
if holes == 3:
    par = 9
else: par = 18
total_score = par - number_of_putts
if number_of_putts > par:
    print(f"Nice try, {name}. Your total score was +{total_score}.")
elif number_of_putts < par:
    print(f"Great job,{name}! Your total score was -{total_score}.")
elif number_of_putts == par:
    print(f"Good game, {name}. Your total score was {total_score}.")
else:
    print("Great game!")
