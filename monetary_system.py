class Money():
    def __init__(self, cp, sp, ep, gp, pp):
        self.cp = cp
        self.sp = sp
        self.ep = ep
        self.gp = gp
        self.pp = pp

    def __repr__(self):
        ret = f"""
        cp: {self.cp}
        sp: {self.sp}
        ep: {self.ep}
        gp: {self.gp}
        pp: {self.pp}
        """
        return ret

    def __len__(self):
        return self.cp/100+self.sp/10+self.ep/2+self.gp+self.pp*10

    def update_money(value, coin='gp'):
        exec(f'self.{coin} = self.{coin}+value')


transformation_matrix = {
    'cp': [1    , 1/10, 1/50 , 1/100 , 1/1000],
    'sp': [10   , 1   , 1/5  ,  1/10 ,  1/100],
    'ep': [50   , 5   , 1    ,   1/2 ,   1/20],
    'gp': [100  , 10  , 2    ,     1 ,   1/10],
    'pp': [1000 , 100 , 20   ,    10 ,      1]
}

coin_index = {
    'cp': 0,
    'sp': 1,
    'ep': 2,
    'gp': 3,
    'pp': 4
}


def exchange_coin(value, coin_from='sp', coin_to='gp'):
    return transformation_matrix[coin_from][coin_index[coin_to]]*value
