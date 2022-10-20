def score_calculator(score):
    if not score.isdigit():
        return 'error input !!!'

    score = int(score)

    if score < 40:
        return score
    else:
        expect_score = 5 * (score//5 + 1)
        if (expect_score - score) < 3:
            return expect_score
        else:
            return score

output = ''

for name in ['德瑞克','尚恩','傑夫','馬基']:
    output += f'\n{name} : {score_calculator(input(f"輸入{name}分數 : "))}'

print(output)