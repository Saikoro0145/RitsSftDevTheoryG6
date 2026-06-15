
class CliView:

    def ShowStart(self):
        print("================================")
        print("      HIT & BLOW GAME")
        print("================================")
        print("4文字の英単語を当ててください")
        print()

    def ReadGuess(self) -> str:
        return input("単語を入力してください > ").lower()

    def ShowGuessResult(self, result):
        print()
        print(f"Hit : {result.GetHits()}")
        print(f"Blow: {result.GetBlows()}")
        print()

    def ShowSuccess(self):
        print()
        print("================================")
        print("       CONGRATULATIONS!")
        print("================================")
        print("正解です！")
        print()

    def ShowError(self, message: str):
        print()
        print(f"[ERROR] {message}")
        print()