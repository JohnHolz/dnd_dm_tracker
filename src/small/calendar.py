months = {'0': 'Auril`s Month',
          '1': 'Celestia`s Month',
          '2': 'Leira`s Month',
          '3': 'Corellon`s Month',
          '4': 'Rillifane`s Month',
          '5': 'Sehanine Moonbow`s Month',
          '6': 'Malar`s Month',
          '7': 'Lilira`s Month',
          '8': 'Pelor`s Month',
          '9': 'Bahamut`s Month',
          '10': 'Tiamat`s Month',
          '11': 'Heironeous`s Month',
          '12': 'Tempus`s Month',
          '13': 'Kord`s Month',
          '14': 'Talos`s Month',
          '15': 'Ogmhar`s Month',
          '16': 'Ogmhar`s Month'}

seasons = {'0': 'Cold Season',
           '1': 'Flowers Season',
           '2': 'Sun Season',
           '3': 'Wood Season',
           '4': 'Wood Season'}

eras = {'fa.': {'name': 'First Age', 'years': '5000~50_000'},
        'ge.': {'name': 'God`s Era', 'years': '50_000~200_000'},
        'wa.': {'name': 'Higher beens war', 'years': '5_000~20_000'},
        'fe.': {'name': 'First Mortal Era', 'years': '50_000'},
        'we.': {'name': 'First Great war', 'years': '5000'},
        'se.': {'name': 'Second Great Era', 'years': '15_000'},
        'sw.': {'name': 'Second Great war', 'years': '2000'},
        'te.': {'name': 'Third Era', 'years': 'now = 1300'}, }


class Time():
    def __init__(self, day, hour=0, minute=0, year=0, era='te.'):
        self.year = year
        self.day = day
        self.hour = hour
        self.minute = minute
        self.month_number = int(self.day/25)
        self.month = months[f'{self.month_number}']
        self.season = seasons[f'{int(self.day/100)}']
        self.age = 'te.'
        self.month_day = self.day % 25 + 1

    def get_json(self):
        ret = dict()
        ret['year'] = self.year
        ret['day'] = self.day
        ret['hour'] = self.hour
        ret['minute'] = self.minute
        ret['month_number'] = self.month_number
        ret['month'] = self.month
        ret['season'] = self.season
        ret['age'] = self.age
        ret['month_day'] = self.month_day
        ret['full'] = self.__repr__()
        return ret

    def __repr__(self):
        minute = self.minute
        if minute < 10:
            minute = f'0{minute}'
        hour = self.hour
        if hour < 10:
            hour = f'0{hour}'
        day = self.month_day
        year = f'{self.year} {self.age}'
        month_season = f'{self.month} ({self.season})'
        date_time = f"{hour}:{minute} day {day}"
        return f'{date_time} {month_season} {year}'

    def __add__(self, other):
        year = self.year + other.year
        day = self.day + other.day
        hour = self.hour + other.hour
        minute = self.minute + other.minute

        if minute >= 70:
            hour = hour+int(minute/70)
            minute = minute % 70
        if hour >= 24:
            day = day+int(hour/24)
            hour = hour % 24
        if day >= 400:
            year = year+int(hour/400)
            day = hour % 400
        return Time(day, hour, minute, year)

    def foward(self, value, update):
        if update == 'day':
            return self + Time(value, 0)
        if update == 'hour':
            return self + Time(0, value)


def get_calendar():
    import pandas as pd
    import numpy as np

    day = pd.DataFrame(pd.Series(np.arange(0, 400)), columns=['day'])
    day['key'] = 0

    hour = pd.DataFrame(pd.Series(np.arange(0, 25, 3)), columns=['hour'])
    hour['key'] = 0

    # day.merge(hour, on='key', how='outer').drop('key',axis=1)
    calendar = day.drop('key', axis=1)

    def ap(serie):
        return Time(serie[0])

    calendar['re'] = calendar.apply(ap, axis=1)
    calendar['month'] = calendar['re'].apply(lambda x: x.month)
    calendar['season'] = calendar['re'].apply(lambda x: x.season)
    calendar['day'] = calendar['re'].apply(lambda x: x.month_day)
    return calendar.iloc[:, [0, 2, 3]]
