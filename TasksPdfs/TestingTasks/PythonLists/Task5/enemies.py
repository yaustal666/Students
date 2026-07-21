enemiesHp = [10] * 10
enemyPoisoned = [False] * 10

seconds = int(input())

for i in range(seconds):
    command = int(input())

    if command != -1:
        enemyPoisoned[command] = not enemyPoisoned[command]
    
    for i in range(10):
        if enemyPoisoned[i] :
            enemiesHp[i] -= 1

print(enemiesHp)