# Stone.Scissors.Paper game
import random
print("Welcome to the SSP game!")
matches_counter = int(input("Matches:"))

items = ["STONE","SCISSORS","PAPER"]
count = 0
human_count = 0
bot_count = 0
draws = 0
while 1:
    if count == matches_counter:
        break
    human = input("Please, choose one item:")
    human = human.upper()
    if human not in items:
        print("Incorrect item")
        break
    bot = random.choice(items)
    print("Bot choice:" + bot)

    if human == "STONE" and bot == "STONE":
        print("draw")
        draws += 1
    if human == "STONE" and bot == "SCISSORS":
        print("Human win!")
        human_count += 1
    if human == "STONE" and bot == "PAPER":
        print("Bot win!")
        bot_count += 1
    if human == "SCISSORS" and bot == "STONE":
        print("Bot win!")
        bot_count += 1
    if human == "SCISSORS" and bot == "SCISSORS":
        print("draw")
        draws += 1
    if human == "SCISSORS" and bot == "PAPER":
        print("Human win!")
        human_count += 1
    if human == "PAPER" and bot == "STONE":
        print("Human win!")
        human_count += 1
    if human == "PAPER" and bot == "SCISSORS":
        print("Bot win!")
        bot_count += 1
    if human == "PAPER" and bot == "PAPER":
        print("draw")
        draws += 1
    count += 1

print("Matches:"+str(count),
      "\nHuman wins:"+str(human_count),
      "\nBot wins:"+str(bot_count),
      "\nDraws:"+str(draws))
