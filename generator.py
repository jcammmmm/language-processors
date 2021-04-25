from predictor import Predictor
from pprint import pprint
from string import Template

TOKEN_FUN = "globals.token"
EMPAR_FUN = "match"
TAB       = "  "

def main():
    gen_asdr("grammar/02.gmr")

def get_pred_test():
    return {
        'A' : [
                (['Z', 'tk0'], {'tk3', 'tk8'}), 
                (['U', 'tk0', 'R'], {'tk3', 'tk8'}), 
                (['e'], {'tk3', 'tk8', 'tk1'}),
                (['A', 'tk0', 'S'], {'tk2', 'tk8', 'tk1'})
        ],
        'B' : [
                (['Z', 'tk0'], {'tk3', 'tk8'}), 
                (['e'], {'tk3', 'tk8'}), 
                (['T', 'tk0', 'S'], {'tk3', 'tk8', 'tk1'}),
                (['A', 'tk0', 'S'], {'tk2', 'tk8', 'tk1'})
        ],
        'C' : [
                (['T', 'tk0'], {'tk3', 'tk8'}), 
                (['e'], {'tk9', 'tk1'}), 
                (['W', 'tk2', 'A'], {'tk2', 'tk1', 'tk3'})
        ]
    }

def gen_asdr(filename):
    """writes to a file python code that can perform ASDR
    Parameters
    ----------
    pred_set: a prediction set, such as the returned by 'grammar_from_file(...)'
    """
    grammar, nont_ord = grammar_from_file(filename)
    predictor = Predictor(grammar, nont_ord)
    pred_set = predictor.PRED

    # imports
    code = ""
    code += "from main import {}\n".format(EMPAR_FUN)
    code += "import globals\n\n"
    
    # boostrap
    code += "def begin():\n"
    code += TAB + Template("$function_name()").substitute(function_name=nont_ord[0])
    code += "\n\n"

    # asdr
    # pred_set.item = X: ([...], {...})
    for X, rules in pred_set.items():
        body = gen_nont_call(X, rules)
        f_def = Template("def $id():\n$body\n\n").substitute(id=X, body=body)
        code += f_def

    # print(code)
    open("asdr.py", "w").write(code)

def gen_nont_call(nont, rules):
    cond = ""
    res = Template("$expr$body")
    ini = True
    for rule in rules:
        # rule = ([...], {...})
        expr = build_bool_xpr(rule[1], ini)
        body = build_cnd_body(rule[0])
        cond += res.substitute(expr=expr, body=body)
        ini = False
    cond += build_else(rules)
    return cond

def build_bool_xpr(pred, ini=False):
    _if = ("if" if ini else "elif")
    or_cnd = TAB + _if + " "
    compare = Template("$get_token == '$cur_symbol' or ")
    for sym in pred:
        or_cnd += compare.substitute(get_token=TOKEN_FUN, cur_symbol=sym)
    or_cnd = or_cnd[:-4]
    or_cnd += ":\n"
    return or_cnd

def build_cnd_body(alpha):
    emparejar = Template(TAB*2 + "$empar_fun('$terminal')")
    nont_call = Template(TAB*2 + "$nont_fun()")
    do_nothin = TAB*2 + "pass"
    body = ""
    for sym in alpha:
        if sym == 'e':
            if len(alpha) != 1:
                raise TabError("Epsilon should appear alone within a rule")
            else:
                cmd = do_nothin
        elif not sym.isupper():
            cmd = emparejar.substitute(empar_fun=EMPAR_FUN, terminal=sym)
        else:
            cmd = nont_call.substitute(nont_fun=sym)
        body += cmd + '\n'
    return body

def build_else(rules):
    cnd = TAB + "else:\n" + TAB*2 + "raise SyntaxError("
    expect = Template("'$token', ")
    exp_tk = set()
    for r in rules:
        for tk in r[1]:
            if tk not in exp_tk:
                exp_tk.add(tk)
                cnd += expect.substitute(token=tk)
    cnd = cnd[:-2] + ")"
    return cnd

"""
Lee un archivo y crea un diccionario que representa esa gramatica
"""
def grammar_from_file(filename):
    f = open(filename, "r")
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