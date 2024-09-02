import random
import time

operator = ['+', '-', '*']
min_operand = 3
max_operand = 14
total_problems = 10

def generator_problem():
    left = random.randint(min_operand, max_operand)
    right = random.randint(min_operand, max_operand)
    operators = random.choice(operator)

    expr = str(left)+ " " + operators + " " + str(right)
    answer = eval(expr)
    return expr, answer


wrong  = 0

input("Press enter to start: ")
print("-----------------------------------------------------")
start_time = time.time()

for i in range(total_problems):
    expr, answer = generator_problem()
    while True:
        guess = input("Problem #" + str(i + 1) + ": " + expr + " = ")
        if guess == str(answer):
            break
        wrong += 1


end_time = time.time()
total_time = round(end_time - start_time, 2)

print("-----------------------------------------------------")
print("Nice Work! You Finished in", total_time , "seconds! and your score is: ", total_problems - wrong, "out of: ", total_problems)
