from hour_system import Hour
class Calendar():
    def __init__(self, year, day):
        self.year = year
        self.day = day
        self.hour = Hour(0,0)
        self.month_number = 1+int(self.day/25)
        months = {'1': 'Auril`s Month',
          '2': 'Celestia`s Month',
          '3': 'Leira`s Month',
          '4': 'Corellon`s Month',
          '5': 'Rillifane`s Month',
          '6': 'Sehanine Moonbow`s Month',
          '7': 'Malar`s Month',
          '8': 'Lilira`s Month',
          '9': 'Pelor`s Month',
          '10': 'Tiamat`s Month',
          '11': 'Bahamut`s Month',
          '12': 'Heironeous`s Month',
          '13': 'Tempus`s Month',
          '14': 'Kord`s Month',
          '15': 'Talos`s Month',
          '16': 'Ogmhar`s Month'}
        seasons = {'1': 'Cold Season',
          '2': 'Flowers Season',
          '3': 'Sun Season',
          '4': 'Wood Season'}
        self.month = months[f'{self.month_number}']
        self.season = seasons[f'{1+int(self.day/100)}']
    
    def __repr__(self):
        ret = f"""{self.year}y {self.day}/{self.month[:3]} {self.hour}"""
        return ret
    
    def foward(self, value):
           pass
        
        
#     def backward(self):