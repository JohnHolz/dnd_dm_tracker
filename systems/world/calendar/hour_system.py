class Hour():
    def __init__(self, hour = 0, minute = 0):
        self.hour = hour
        self.minute = minute

    def __repr__(self):
        zero_hour = ''
        zero_min = ''
        if self.hour < 10:
            zero_hour = '0'
        if self.minute < 10:
            zero_min = '0'
        return f'{zero_hour}{self.hour}:{zero_min}{self.minute}'
    
    def foward(self, value, update = 'hour'):
        if update == 'hour':
            self.hour = (self.hour+value)%24
        if update == 'minute':
            new_minute = self.minute+value
            if new_minute>70:
                self.hour += 1
            self.minute = new_minute%70