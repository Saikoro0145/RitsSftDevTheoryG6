import os
import sys

# srcの中身をimportできるようにパスを追加
sys.path.append(os.path.join(os.path.dirname(__file__), "..", "src"))

from GuessJudge import GuessJudge


def test_guessが短いとき():
    judge = GuessJudge()
    result = judge.judge("abc", "abcd")
    assert result.GetHits() == -1
    assert result.GetBlows() == -1


def test_guessが長いとき():
    judge = GuessJudge()
    result = judge.judge("abcde", "abcd")
    assert result.GetHits() == -1
    assert result.GetBlows() == -1


def test_全部当たり():
    judge = GuessJudge()
    result = judge.judge("abcd", "abcd")
    assert result.GetHits() == 4
    assert result.GetBlows() == 0


def test_文字は合ってるけど場所が全部違う():
    judge = GuessJudge()
    result = judge.judge("dcba", "abcd")
    assert result.GetHits() == 0
    assert result.GetBlows() == 4


def test_hitとblowが混ざる():
    # a だけ位置が合っていて、残りはblow
    judge = GuessJudge()
    result = judge.judge("acbd", "abcd")
    assert result.GetHits() == 2
    assert result.GetBlows() == 2


def test_全部はずれ():
    judge = GuessJudge()
    result = judge.judge("xxxx", "abcd")
    assert result.GetHits() == 0
    assert result.GetBlows() == 0


def test_同じ文字が含まれる場合():
    # aabb と abab → 1文字目と4文字目がhit、残りはblow
    judge = GuessJudge()
    result = judge.judge("aabb", "abab")
    assert result.GetHits() == 2
    assert result.GetBlows() == 2


def test_予想が同じ文字だらけ():
    # aaaa のうち、当たるのは1文字目のaだけ
    judge = GuessJudge()
    result = judge.judge("aaaa", "abcd")
    assert result.GetHits() == 1
    assert result.GetBlows() == 0


def test_答えが同じ文字だらけ():
    judge = GuessJudge()
    result = judge.judge("abcd", "aaaa")
    assert result.GetHits() == 1
    assert result.GetBlows() == 0


def test_全部ずれてて重複もある():
    judge = GuessJudge()
    result = judge.judge("xxaa", "aaxx")
    assert result.GetHits() == 0
    assert result.GetBlows() == 4


def test_予想の重複は1個しか数えない():
    # 予想にaが2つあるけど、答えのaは1つなので片方は数えない
    judge = GuessJudge()
    result = judge.judge("abca", "dabc")
    assert result.GetHits() == 0
    assert result.GetBlows() == 3


def test_空文字同士():
    judge = GuessJudge()
    result = judge.judge("", "")
    assert result.GetHits() == 0
    assert result.GetBlows() == 0
