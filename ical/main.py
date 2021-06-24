import codecs
from icalendar import Calendar

ical_pass = "iCalender.ics"

def ical():
    fin = codecs.open(ical_pass)
    cal = Calendar.from_ical(fin.read())
    fin.close()
    li = []
    for ev in cal.walk():
        if ev.name == 'VEVENT':
            start_dt = ev.decoded("dtstart")
            end_dt = ev.decoded("dtend")
            summary = ev['summary'].encode('utf-8')
            summary2 = summary.decode().replace('\u3000', '')
            summary3 = ','.join([x.strip() for x in summary2.split(' ')])
            # todo 別ファイルに例外処理をまとめるファイルを作りたい。.replace('\u3000', '')
            li.append("{start},{end},{summary}".format(start=start_dt.strftime("%Y/%m/%d"),
                                                       end=end_dt.strftime("%Y/%m/%d"),
                                                       summary=summary3))

    ical_csv_pass = "ical.csv"
    f = codecs.open(ical_csv_pass, "w")
    for ld in li:
        f.write(ld + "\n")
    f.close()

if __name__ == '__main__':
    ical()
    print("mainで実行中")