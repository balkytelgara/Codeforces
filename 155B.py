n = int(input())
effective_cards = 0
effective_cards_scores = 0
effective_cards_bonuses = 0
score = []
ans = 0

for _ in range(n):
  a, b = map(int, input().split())

  if b > 0:
    effective_cards_scores += a
    effective_cards_bonuses += b
    effective_cards += 1
  else:
    score.append(a)

score.sort(reverse=True)

effective_cards_bonuses -= effective_cards - 1

if effective_cards_bonuses <= 0:
  print(score[0])
else:
  print(sum(score[:effective_cards_bonuses]) + effective_cards_scores)