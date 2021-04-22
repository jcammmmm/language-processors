import pprint

##########################################################
### FIRST
##########################################################

def main():
    grammar, nont_ord = grammar_from_file("incr")
    asd = TopDownSyntacticParser(grammar, nont_ord)
    print("PREDICION")
    pprint.pprint(asd.get_prediction_set())

        
class TopDownSyntacticParser:
    def __init__(self, grammar, nont_ord):
        self.grammar    = grammar
        self.nont_set   = set(nont_ord)
        self.nont_rev   = nont_ord
        self.PRIMEROS   = {}
        self.SIGUIENTES = {}
        self.PRED       = []

        # initializations
        self.nont_rev.reverse()
        for X in self.nont_set:
            self.PRIMEROS[X] = set()
            self.SIGUIENTES[X] = set()

    """
    computes de prediction set for every rule
    """
    def get_prediction_set(self):
        self.__compute_primeros()
        self.__compute_siguientes()
        self.PRED = []
        for X in self.nont_rev:
            for alpha in self.grammar[X]:
                prim = set(self.__p(alpha))
                if 'e' in prim:
                    prim -= {'e'}
                    prim.update(self.SIGUIENTES[X])
                self.PRED.append((prim, X, alpha))
        return self.PRED
                
    
    """
    a root function for primeros computation for every rule
    """
    def __compute_primeros(self):
        # Reverse the dictionary to process first the rules
        # with lower precedence
        for X in self.nont_rev:
            # rule 2c
            for alpha in self.grammar[X]:
                self.PRIMEROS[X].update(self.__p(alpha))
        return self.PRIMEROS

    """
    Return a list containing the primeros for alpha
    param alpha : a sequence of terminal and non terminals
    returs : the set of primeros
    """
    def __p(self, alpha):
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
                        ans.update(self.__p(alpha[1:]))
                return list(ans)

    """
    desde aquí se lanza la funcion recursiva para el calculo de los
    SEGUNDOS por cada no terminal
    """
    def __compute_siguientes(self):
        for X in self.nont_rev:
            self.SIGUIENTES[X].update(self.__s(X))
        return self.SIGUIENTES

    """
    param nont: a nonterminal symbol
    returns : the siguientes set
    """
    # TODO this algorithm does not work well with left recursive grammars, ex. 0
    def __s(self, nont):
        ans = set()
        # si es el simbolo inicial
        if nont == self.nont_rev[-1]:
            ans.add('$')
        # iterate over all rules searching for 'nont'
        for X in self.nont_rev:
            for rule in self.grammar[X]:
                if rule.__contains__(nont):
                    loc = rule.index(nont)
                    # primeros de beta
                    prim_beta = set(self.__p(rule[loc + 1:]))
                    if 'e' in prim_beta:
                        prim_beta -= {'e'}
                        ans.update(self.__s(X))
                    ans.update(prim_beta)
        return list(ans)

"""
Lee un archivo y crea un diccionario que representa esa gramatica
"""
def grammar_from_file(filename):
    f = open("grammar/" + filename + ".gmr", "r")
    grammar = {}
    nont_ord = []
    nont_set = set()
    while True:
        line = f.readline()
        if not line:
            break

        if line[0] == '#' or line[0] == '$' or line[0] == '~' or line[0] == '\n':
            continue
        else:
            X, rule = line.split(':')
            
            X = X.strip()
            if X not in nont_set:
                nont_ord.append(X)
                nont_set.add(X)

            r = rule.strip().split(' ')
            if X in grammar:
                grammar[X].append(r)
            else:
                grammar[X] = [r]

    f.close()
    return grammar, nont_ord 

if __name__ == "__main__":
    main()

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


