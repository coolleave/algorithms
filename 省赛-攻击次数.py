hp = 2025
r = 1
while hp > 0:
    hp -= 5
    if r % 2 != 0:
        hp -= 15
    elif r % 2 == 0:
        hp -= 2
    if r % 3 == 1:
        hp -= 2
    elif r % 3 == 2:
        hp -= 10
    elif r % 3 == 0:
        hp -= 7

    print(f"第{r}回合", hp)
    r += 1
print(r)
