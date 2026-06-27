from WordProvider import WordProvider
from GuessJudge import GuessJudge
from CliView import CliView


class GameCore:
    def __init__(self):
        self._wordProvider = WordProvider()
        self._judge = GuessJudge()
        self._view = CliView()

        self._answer = self._wordProvider.GetAnswer()

    def play(self):
        self._view.ShowStart()

        while True:
            guess = self._view.ReadGuess()

            result = self._judge.judge(guess, self._answer)

            self._view.ShowGuessResult(result)

            if result.GetHits() == 4:
                self._view.ShowSuccess()
                break


# ファイルを直接実行したとき専用のコードのためテストからは呼ばれない
if __name__ == "__main__":  # pragma: no cover
    game = GameCore()
    game.play()
