import sys
from pathlib import Path
from unittest.mock import patch

sys.path.insert(0, str(Path(__file__).parent.parent / "src"))

from GameCore import GameCore


# テスト用の偽WordProvider（常に "baby" を返す）
class StubWordProvider:
    def GetAnswer(self):
        return "baby"


# テスト用の偽CliView（入力を順番に返す）
class StubCliView:
    def __init__(self, inputs):
        self._inputs = inputs
        self._index = 0
        self.success_called = False
        self.show_start_count = 0
        self.show_guess_result_count = 0

    def ShowStart(self):
        self.show_start_count += 1

    def ReadGuess(self):
        guess = self._inputs[self._index]
        self._index += 1
        return guess

    def ShowGuessResult(self, result):
        self.show_guess_result_count += 1

    def ShowSuccess(self):
        self.success_called = True

    def ShowError(self, message):
        pass


def test_正解したらShowSuccessが呼ばれる():
    # FIXED: patch で answers.csv の読み込みをスキップ
    with patch("WordProvider.WordProvider.GetAnswer", return_value="baby"):
        game = GameCore()
        stub_view = StubCliView(inputs=["baby"])
        game._view = stub_view
        game._answer = "baby"

        game.play()

        assert stub_view.success_called


def test_ゲーム開始時にShowStartが呼ばれる():
    with patch("WordProvider.WordProvider.GetAnswer", return_value="baby"):
        game = GameCore()
        stub_view = StubCliView(inputs=["baby"])
        game._view = stub_view
        game._answer = "baby"

        game.play()

        assert stub_view.show_start_count == 1


def test_毎回ShowGuessResultが呼ばれる():
    with patch("WordProvider.WordProvider.GetAnswer", return_value="baby"):
        game = GameCore()
        stub_view = StubCliView(inputs=["xyzw", "baby"])  # 2回入力
        game._view = stub_view
        game._answer = "baby"

        game.play()

        assert stub_view.show_guess_result_count == 2


def test_不正解の後に正解するとループが終わる():
    # patch で answers.csv の読み込みをスキップ
    with patch("WordProvider.WordProvider.GetAnswer", return_value="baby"):
        game = GameCore()
        stub_view = StubCliView(inputs=["xyzw", "baby"])
        game._view = stub_view
        game._answer = "baby"

        game.play()

        assert stub_view.success_called
