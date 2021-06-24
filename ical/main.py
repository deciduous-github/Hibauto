import codecs
from icalendar import Calendar

def flatten_2d(data):
    for block in data:
        for elem in block:
            yield elem

ical_pass = "iCalender.ics"
fin = codecs.open(ical_pass)
cal = Calendar.from_ical(fin.read())
fin.close()
for ev in cal.walk():
    if ev.name == 'VEVENT':
        start_dt = ev.decoded("dtstart")
        end_dt = ev.decoded("dtend")
        summary = ev['summary'].encode('utf-8')
        summary2 = summary.decode().replace('\u3000', '').split(" ")
        # 半角スペースで区切りたい
        print("{start} - {end} : {summary}".format(start=start_dt.strftime("%Y/%m/%d"),
                                                   end=end_dt.strftime("%Y/%m/%d"),
                                                   summary=summary2))
