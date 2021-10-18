import sys
sys.path.append('../../')
from places.urban import Urban

Selgaunt = Urban('Selgaunt','a Cidade Branca, Capital Militar','city')
description = """    - Cidade praticamente toda em pedra, arquitetura aredondada com pilares largos. 
            - A agua banha toda a cidade por corregos de agua limpa passando entre montes. 
            - A cidade é bem arborizada, com arvores frutiferas por todo lado
            - A noite a cidade é iluminada por torchas espalhadas por toda a cidade, por torres farol magicas e pela lua, povos da cidade falam que é bençao divina de Sehanine, deusa da lua
            - A cidade é bem militarizada
            - Muros exteros e dos portos são muito grandes, impressionam as pessoas
            - Não existe preconceito, a cidade tem todas as raças passando indo e voltando por conta de ser entrada pro continente
            - Cidade tem muitos templos, shrines e estatua de deuses bons"""
Selgaunt.add_info('description',description)