import pprint

##########################################################
### FIRST
##########################################################

def main():
    primeros()
    siguientes()

"""
a root function for primeros computation
"""
def primeros():
    # Reverse the dictionary to process first the rules
    # with lower precedence
    nont = list(ORD)
    nont.reverse()
    for X in nont:
        # rule 2c
        for alpha in GRAMMAR[X]:
            PRIMEROS[X].update(p(alpha))
    
    pprint.pprint(PRIMEROS)

"""
Return a list containing the primeros for alpha
param alpha : a sequence of terminal and non terminals
returs : the set of primeros
"""
def p(alpha):
    if len(alpha) == 0:
        return ['e']

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
                    ans.update(p(alpha[1:]))
            return list(ans)

def siguientes():
    for X in NONT:
        SIGUIENTES[X].update(s(X))
    pprint.pprint(SIGUIENTES)

"""
param nont: a nonterminal symbol
returns : the siguientes set
"""
# TODO this algorithm does not work well with left recursive grammars, ex. 0
def s(nont):
    ans = set()
    if nont == ORD[0]:
        ans.add('$')
    # iterate over all rules searching for 'nont'
    for X in NONT:
        for rule in GRAMMAR[X]:
            if rule.__contains__(nont):
                loc = rule.index(nont)
                prim_beta = set(p(rule[loc + 1:]))
                if 'e' in prim_beta:
                    prim_beta -= {'e'}
                    ans.update(s(X))
                ans.update(prim_beta)
    return list(ans)

def get_grammar(sample):
    if sample == 0:
        # TODO fix case when grammar rule is recursive e.g. A -> A tres ex. 0
        # TODO fix to allow the computation of SIGUIENTES; ex. 0
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
    GRAMMAR = get_grammar(1)
    NONT = set(GRAMMAR.keys())
    ORD = list(GRAMMAR.keys())
    PRIMEROS = {}
    SIGUIENTES = {}
    for X in NONT:
        PRIMEROS[X] = set()
        SIGUIENTES[X] = set()
    main()
    


