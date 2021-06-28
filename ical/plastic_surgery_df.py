import pandas as pd
import numpy as np
from main import ical_df, col_names

blank_between_artists_list = ['鈴木\u3000雅之',
                              '岡村\u3000靖幸']

place_2_frames_list = ['KT Zepp横浜',
                       'ZEPP 札幌',
                       'ZEPP 名古屋',
                       'ZEPP Haneda',
                       '東広島芸術文化ホール くらら',
                       ]

place_3_frames_list = ['LINE CUBE SHIBUYA(渋公)',
                       'Honey Road st.',
                       'Zepp Osaka bayside']


def df_ical_loc(index, data):
    for col_index, col_name in enumerate(col_names):
        ical_df.loc[index, col_name] = data[col_index]


class Artist(object):

    @staticmethod
    def blank_between_artists():
        for index, data in ical_df.iterrows():
            for i in range(len(blank_between_artists_list)):
                j = blank_between_artists_list[i]
                if data['artist'] == j:
                    data[1] = j.replace('\u3000', '')
                    df_ical_loc(index, data)


class Place(object):

    @staticmethod
    def place_2_frames(data):
        data[2] = data[2] + ' ' + data[3]
        data[3] = data[4]
        data[4] = data[5] = np.nan

    @staticmethod
    def place_3_frames(data):
        data[2] = data[2] + ' ' + data[3] + ' ' + data[4]
        data[3] = data[5]
        data[4] = data[5] = np.nan

    @staticmethod
    def over_column():
        for index, data in ical_df.dropna(subset=['over']).iterrows():
            for i in range(len(place_2_frames_list)):
                b = place_2_frames_list[i].split(' ')
                if data['place'] == b[0] and data['contents'] == b[1]:
                    Place.place_2_frames(data)
                    df_ical_loc(index, data)

            for i in range(len(place_3_frames_list)):
                b = place_3_frames_list[i].split(' ')
                if data['place'] == b[0] and data['contents'] == b[1]:
                    Place.place_3_frames(data)
                    df_ical_loc(index, data)

        return


if __name__ == '__main__':
    Place.over_column()
    Artist.blank_between_artists()
    print(ical_df.dropna(how='all', axis=1))
