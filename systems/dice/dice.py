from numpy.random import randint

def dice(d):
    ## ! create a dice roll with randint - minimum of 0 and max of d
    return randint(1,d+1)

def rand_dice(dice = 'd6'):
    ## ! return an string to be evaluated with the calculus
    if 'd' not in dice:
        return dice
    
    ## split
    vec = dice.split('d')
    
    if vec[0]=='':
        vec[0]='1'
    
    ## @ string to be evaluated
    eval_string = f'{vec[0]}'+'*'+f'dice({vec[1]})'
    return eval_string

def roll(ŕoll='2d6+4'):
    ## !TODO fazer recursivo
    ## ! roll dice function and return the value
    ## ! just work with +, - not implemented
    return sum(list(map( lambda y: eval(rand_dice(y)), ŕoll.split('+'))))