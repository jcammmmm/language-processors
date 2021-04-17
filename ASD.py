import pprint

##########################################################
### FIRST
##########################################################

def main():
    GRAMMAR = get_grammar(0)
    
    asd = TopDownSyntacticParser(GRAMMAR)
    PRIMEROS = asd.compute_primeros()
    pprint.pprint(PRIMEROS)
    SIGUIENTES = asd.compute_siguientes()
    pprint.pprint(SIGUIENTES)

"""
se supone la convension de que las reglas con epsilon unico
se escriben siempre al final
"""
# TODO completar el metodo buscando recursivamente en profundidad
def fix_easy_left_recursion(grammar):
    nont_with_recusion = {}

    # buscar recusiones por izquierda y si existe epsilon en 
    # ese no terminal X para solucionar facil
    for X, rules in grammar.items():
        wait_e = False
        i = 0
        for alpha in rules:
            # hay recursion por izquierda
            if alpha[0] == X:
                wait_e = True
                print(X + ' has left recursion')
                # regla a corregir
                if X not in nont_with_recusion:
                    nont_with_recusion[X] = [i]
                else:
                    nont_with_recusion[X].append[i]

            if wait_e and alpha[0] == 'e':
                wait_e = False
                break

            # ubicacion regla, dentro de reglas
            i += 1
        
        # no puedo arreglar facilmente no hay epsilon para
        # suprimir la recursion
        if wait_e:
            raise EnvironmentError

    # corregir la recursividad por izquierda
    for X, loc in nont_with_recusion.items():
        print(X, loc)
        
class TopDownSyntacticParser:
    def __init__(self, grammar):
        self.grammar    = grammar
        self.nont_set   = set(grammar.keys())
        self.nont_rev   = list(grammar.keys())
        self.PRIMEROS   = {}
        self.SIGUIENTES = {}

        # initializations
        self.nont_rev.reverse()
        for X in self.nont_set:
            self.PRIMEROS[X] = set()
            self.SIGUIENTES[X] = set()

    """
    a root function for primeros computation
    """
    def compute_primeros(self):
        # Reverse the dictionary to process first the rules
        # with lower precedence
        for X in self.nont_rev:
            # rule 2c
            for alpha in self.grammar[X]:
                self.PRIMEROS[X].update(self.p(alpha))
        return self.PRIMEROS

    """
    Return a list containing the primeros for alpha
    param alpha : a sequence of terminal and non terminals
    returs : the set of primeros
    """
    def p(self, alpha):
        if len(alpha) == 0:
            return ['e']

        if alpha[0] == 'e':
            return ['e']
        else:
            a1 = alpha[0]
            if a1 not in self.nont_set:
                return [a1]
            else:
                ans = set(self.PRIMEROS[a1])
                if 'e' in ans:
                    ans -= {'e'}
                    if len(alpha) == 1:
                        ans.add('e')
                    else:
                        ans.update(self.p(alpha[1:]))
                return list(ans)

    """
    desde aquí se lanza la funcion recursiva para el calculo de los
    SEGUNDOS
    """
    def compute_siguientes(self):
        for X in self.nont_set:
            self.SIGUIENTES[X].update(self.s(X))
        return self.SIGUIENTES

    """
    param nont: a nonterminal symbol
    returns : the siguientes set
    """
    # TODO this algorithm does not work well with left recursive grammars, ex. 0
    def s(self, nont):
        ans = set()
        # si es el simbolo inicial
        if nont == self.nont_rev[-1]:
            ans.add('$')
        # iterate over all rules searching for 'nont'
        for X in self.nont_set:
            for rule in self.grammar[X]:
                if rule.__contains__(nont):
                    loc = rule.index(nont)
                    # primeros de beta
                    prim_beta = set(self.p(rule[loc + 1:]))
                    if 'e' in prim_beta:
                        prim_beta -= {'e'}
                        ans.update(self.s(X))
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
                ['A', 'tres'],
                ['e'],
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
    main()
    


