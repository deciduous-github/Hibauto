import pandas as pd
from main import ical_df

place_3_frames_list = ['LINE CUBE SHIBUYA(渋公)', 'Honey Road st.']


class Place(object):

    @staticmethod
    def dropna_over():
        # Contentsよりカラムが多い物を処理しています。
        drop = ical_df.dropna(how='all', axis=1)
        drop = drop.dropna(subset=['over'])
        return drop

    @staticmethod
    def place_3_frames(data):
        data[2] = data[2] + ' ' + data[3] + ' ' + data[4]
        data[3] = data[5]
        data[4] = data[5] = 'NaN'

    @staticmethod
    def over_column():
        # todo ical_dfに値を返さないといけない
        for index, data in Place.dropna_over().iterrows():
            for i in range(len(place_3_frames_list)):
                b = place_3_frames_list[i].split(' ')
                if data['place'] == b[0] and data['contents'] == b[1]:
                    Place.place_3_frames(data)

            print(data)
            print('--------------------')
        return None


if __name__ == '__main__':
    Place.over_column()
