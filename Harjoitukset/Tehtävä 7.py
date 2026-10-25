Aineet = ["omena", "kaneli", "puuro", "kaurahiutale", "suola", "manteli"]

määrä = 0

for sana in Aineet:
    if len(sana) > 5:
        määrä = määrä + 1

print(määrä)
