import pandas as pd
import random


class WordProvider:
    def GetAnswer(self):
        df = pd.read_excel("sampleohsystemdevelope.xlsx")

        row_count = len(df)
        col_count = len(df.columns)

        random_row = random.randint(0, row_count - 1)

        # ランダム関数を使う。Excelでは1からやけど、
        # Pythonでは0からカウントされるので1ずれている。
        random_col = random.randint(0, col_count - 1)

        # ilocで決めたデータの取得
        a = df.iloc[random_row, random_col]

        # 文字列に変換
        moziretsu = str(a)

        # 小文字に変換
        answer = moziretsu.lower()

        return answer
