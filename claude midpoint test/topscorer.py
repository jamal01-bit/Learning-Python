playerlist = []
scorelist = []
while True:
 player = input("Enter player name ('or done' to finish): ")
 if (player == 'done' or player == 'Done'):
  break
 else:
  playerlist.append(player)
  score = int(input(f"Enter score for {player}: "))
  scorelist.append(score)
print(f"--- Results ---")
print(f"Total players: {len(playerlist)}")
print(f"Average score: {round(sum(scorelist) / len(scorelist), 1)}")
topscorer = ''
highestscore = 0
for i in range(len(playerlist)):
 score = scorelist[i]
 player = playerlist[i]
 if (score > highestscore):
  highestscore = score
  topscorer = player
print(f"Top scorer: {topscorer} ({highestscore} points)") 

