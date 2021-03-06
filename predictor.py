import pprint
from lexer import Lexer
from collections import deque
    
class Predictor:
    """
    Given an ordered grammar, when this class is instanced computes the prediction
    set for each grammar rule. When we say ordered that means that the result varies
    with the order of ther rules.
    We recommend put more dependant or global rules above , and rules that are dependencies
    below.
    The attribute 'done' indicates if this Predictor was run already
    """
    def __init__(self, grammar, nont_ord):
        self.grammar    = grammar
        self.nont_set   = set(nont_ord)
        self.nont_rev   = list(nont_ord)
        self.done       = False
        self.PRIMEROS   = {}
        self.SIGUIENTES = {}
        self.PRED       = {}

        # initializations
        self.nont_rev.reverse()
        for X in self.nont_set:
            self.PRIMEROS[X]    = set()
            self.SIGUIENTES[X]  = set()
            self.PRED[X]        = list()

        self.__get_prediction_set()

    def get_rule(self, token):
        terminal = self.__to_terminal(token)
        for pred in self.PRED:
            if terminal in pred[2]:
                return (pred[0], pred[1])
        raise SyntaxError()

    def __to_terminal(self, token):
        return token.split(',')[0][1:]


    """
    computes de prediction set for every rule
    """
    def __get_prediction_set(self):
        if self.done:
            return self.PRED

        self.__compute_primeros()
        self.__compute_siguientes()
        for X in self.nont_rev:
            for alpha in self.grammar[X]:
                prim = set(self.__p(alpha))
                if 'e' in prim:
                    prim -= {'e'}
                    prim.update(self.SIGUIENTES[X])
                self.PRED[X].append((alpha, prim))
        self.done = True
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
    Return a list containing the primeros for alpha. Keep in mind that the processing
    takes into account that grammars have an inherent order from where they should be
    processed.
    param alpha : a sequence of terminal and non terminals
    returns : the set of primeros
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
    desde aqu?? se lanza la funcion recursiva para el calculo de los
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
    def __s(self, nont, recursive=True):
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
                    if recursive and 'e' in prim_beta:
                        prim_beta -= {'e'}
                        ans.update(self.__s(X, False))
                    ans.update(prim_beta)
        return list(ans)


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