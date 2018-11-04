# Catch5
The game is always winnable

A random player won about **24%** of the games. It was suprising to me as I didnt expect it to take 1/2/3 steps in correct order. But as there are multiple ways of winning the same game as from 9 to 5 we can go via -1/-3, -2/-2 and -3/-1 this helps random play to win so much.

Epoch: 10 Wins: 2 (20.00%) Losses: 8 (80.00%)
Epoch: 20 Wins: 7 (35.00%) Losses: 13 (65.00%)
Epoch: 30 Wins: 11 (36.67%) Losses: 19 (63.33%)
Epoch: 40 Wins: 18 (45.00%) Losses: 22 (55.00%)
Epoch: 50 Wins: 27 (54.00%) Losses: 23 (46.00%)
Epoch: 60 Wins: 35 (58.33%) Losses: 25 (41.67%)
Epoch: 70 Wins: 44 (62.86%) Losses: 26 (37.14%)
Epoch: 80 Wins: 51 (63.75%) Losses: 29 (36.25%)
Epoch: 90 Wins: 60 (66.67%) Losses: 30 (33.33%)
Epoch: 100 Wins: 67 (67.00%) Losses: 33 (33.00%)

In 100 iterations it has 67% win rate well above the 24% the random bot won. Important to note that this AI is still making 30% moves randomly so we are winning a lot more in reality. We check this in next section.

We train on 100 random games and then play 1000 games on no randomness and we win every game.
Epoch: 1000 Wins: 1000 (100.00%) Losses: 0 (0.00%)