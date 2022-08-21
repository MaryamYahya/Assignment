
win=0
draw=0
defeat=0
score_win=0
score_draw=0
score_defeat=0
total=0

for i in range(1,3):
    result=input(f"Please enter the result of the {i} game: \n win...score=3 \n defeat...score=0 \n draw...score=1 \n :")
    if result == "win" :
        win += 1
        score_win=3 
        total+=score_win
    elif result == "draw":
        draw += 1
        score_draw=1
        total+=score_draw
    elif result == "defeat":
        defeat += 1
        score_defeat=0
        total+=score_defeat
    else:
        print("eror")
print(f"\n\n\n win number: {win}\n and defeat number: {defeat}\n and draw number: {draw}\n\n and total score: {total}")
