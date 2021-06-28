import codecs
import pandas as pd

from icalendar import Calendar


def ical():
    fin = codecs.open("iCalender.ics")
    cal = Calendar.from_ical(fin.read())
    fin.close()
    li = []
    for ev in cal.walk():
        if ev.name == 'VEVENT':
            start_dt = ev.decoded("dtstart")
            summary = ev['summary'].encode('utf-8')
            summary_decode = summary.decode()
            summary_split = ','.join([x.strip() for x in summary_decode.split(' ')])
            li.append("{start},{summary}".format(start=start_dt.strftime("%Y/%m/%d"),
                                                 summary=summary_split))

    ical_csv_pass = "ical.csv"
    f = codecs.open(ical_csv_pass, "w")
    for ld in li:
        f.write(ld + "\n")
    f.close()


col_names = ["date", "artist", "place", "contents", 'over', 'over2', 'over3', 'over4']


def read_ical_csv():
    # todo ical.csvがあるか判断してから読み込み
    data = pd.read_csv('ical.csv', encoding="utf-8", names=col_names)
    return data


ical_df = read_ical_csv()

if __name__ == '__main__':
    print("mainで実行中")
    # ical()
    read_ical_csv()
