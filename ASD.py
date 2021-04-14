import pprint

##########################################################
### FIRST
##########################################################
def main():
    # Reverse the dictionary to process first the rules
    # with lower precedence
    nont = list(ORD)
    nont.reverse()
    for X in nont:
        for alpha in GRAMMAR[X]:
            PRIMEROS[X].update(primeros(alpha))
    
    pprint.pprint(PRIMEROS)

"""
Return a list containing the primeros for alpha
"""
def primeros(alpha):
    if alpha[0] == 'e':
        return ['e']
    else:
        a1 = alpha[0]
        if a1 not in NONT:
            return [a1]
        else:
            ans = set(PRIMEROS[a1])
            if 'e' in ans:
                ans -= {'e'}
                if len(alpha) == 1:
                    ans.add('e')
                else:
                    ans.update(primeros(alpha[1:]))
            return list(ans)

                    

        

def get_grammar(sample):
    if sample == 0:
        return {
            'S' : [
                ['A', 'uno', 'B', 'C'],
                ['S', 'dos']
            ],
            'A': [
                ['B', 'C', 'D'],
                ['A', 'e'],
            ],
            'B': [
                ['D', 'cuatro', 'C', 'tres'],
                ['e']
            ],
            'C': [
                ['cinco', 'D', 'B'],
                ['e']
            ],
            'D': [
                ['seis'],
                ['e']
            ]
        }
    elif sample == 1:
        return {
            'A': [
                ['B', 'C'],
                ['bad']
            ],
            'B': [
                ['big', 'C', 'boss'],
                ['bet']
            ],
            'C': [
                ['cat'],
                ['cow']
            ]
        }
    else:
        return {
            'A': [
                ['B', 'C'],
                ['ant', 'A', 'all']
            ],
            'B': [
                ['big', 'C'],
                ['bus', 'A', 'boss'],
                ['e']
            ],
            'C': [
                ['cat'],
                ['cow']
            ]
        }

if __name__ == "__main__":
    GRAMMAR = get_grammar(2)
    NONT = set(GRAMMAR.keys())
    ORD = list(GRAMMAR.keys())
    PRIMEROS = {}
    for X in NONT:
        PRIMEROS[X] = set()
    main()
    


