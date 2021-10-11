class Char():
    def __init__(self, player_name, money=31, position = 1):
        self.position = position
        self.money = money
        self.play_next_round = True
        self.player_name = player_name
    
    def __repr__(self):
        ret =  f"""
        name:{self.player_name}
        money:{self.money}
        position:{self.position}
        next round:{self.play_next_round}"""
        return ret

    def __len__(self):
        return self.position

    def update_money(self, int):
        self.money = self.money+int
        
    def update_position(self, int):
        self.position = int
        
    def roll_dice(self, die = 6):
        self.position = (self.position+randint(die)+1)%33
        
    def not_play_next_round(self):
        self.play_next_round = False