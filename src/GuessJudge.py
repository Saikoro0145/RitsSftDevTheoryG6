from GuessResult import GuessResult


class GuessJudge:
    def judge(self, guess, answer):
        if guess == answer:
            return "Correct"
        elif len(guess) < len(answer):
            return "Too few characters"
        elif len(guess) > len(answer):
            return "Too many characters"

        answer = list(answer)
        guess = list(guess)

        hit = 0
        blow = 0
        for i in range(len(answer)):
            if guess[i] == answer[i]:
                hit += 1
                # この場合guessからgを削除する、削除して配列がずれないようにnullを入れる
                guess[i] = None
                answer[i] = None

        for j in answer:
            if j is None:
                continue
            if j in guess:
                blow += 1
                # この場合guessからgを削除する、削除して配列がずれないようにnullを入れる
                guess[guess.index(j)] = None

        return GuessResult(hit, blow)
