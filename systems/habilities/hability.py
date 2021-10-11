class Hability():
    def __init__(self, name, hability_cost, effect, value = '',description=''):
        self.name = name
        self.cost = hability_cost
        self.effect = effect
        self.roll = value
        self.description = description

    def __repr__(self) -> str:
        ret = f"""
        {self.name}
            cost:           {self.cost}
            effect:         {self.effect}
            roll:           {self.roll}
            description:    {self.description}
        """
        return ret