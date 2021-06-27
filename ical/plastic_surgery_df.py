import pandas as pd
from main import ical_df


class platic_surgery_ical_df(object):

    def dropna_over(self):
        # Contentsよりカラムが多い物を処理しています。
        drop = ical_df.dropna(how='all', axis=1)
        drop2 = drop.dropna(subset=['over'])
        print(drop2)


if __name__ == '__main__':
    test = platic_surgery_ical_df()
    test.dropna_over()
