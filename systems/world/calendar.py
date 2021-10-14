import pandas as pd
import numpy as np
import sys
sys.path.append('../')
from world.time import DateTime

def get_calendar():
    day = pd.DataFrame(pd.Series(np.arange(0,400)),columns=['day'])
    day['key'] = 0

    hour = pd.DataFrame(pd.Series(np.arange(0,25,3)),columns=['hour'])
    hour['key'] = 0

    calendar = day.drop('key',axis=1)#day.merge(hour, on='key', how='outer').drop('key',axis=1)
    def ap(serie):
        return DateTime(serie[0])

    calendar['re'] = calendar.apply(ap,axis=1)
    calendar['month'] = calendar['re'].apply(lambda x:x.month)
    calendar['season'] = calendar['re'].apply(lambda x:x.season)
    calendar['day'] = calendar['re'].apply(lambda x:x.month_day)
    return calendar.iloc[:,[0,2,3]]