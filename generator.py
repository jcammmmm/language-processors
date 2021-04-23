from predictor import Predictor, grammar_from_file
from pprint import pprint
from string import Template

TOKEN_FUN = "get_curr_token"
EMPAR_FUN = "match"
TAB       = "  "

def main():
    grammar, nont_ord = grammar_from_file("grammar/asdrtest.gmr")
    predictor = Predictor(grammar, nont_ord)
    pred = predictor.PRED
    # pred = get_pred_test()
    gen_asdr(pred)

def get_pred_test():
    return {
        'A' : [
                (['Z', 'tk0'], {'tk3', 'tk8'}), 
                (['U', 'tk0', 'R'], {'tk3', 'tk8'}), 
                (['T', 'tk0', 'S'], {'tk3', 'tk8', 'tk1'}),
                (['A', 'tk0', 'S'], {'tk2', 'tk8', 'tk1'})
        ],
        'B' : [
                (['Z', 'tk0'], {'tk3', 'tk8'}), 
                (['U', 'tk0', 'R'], {'tk3', 'tk8'}), 
                (['T', 'tk0', 'S'], {'tk3', 'tk8', 'tk1'}),
                (['A', 'tk0', 'S'], {'tk2', 'tk8', 'tk1'})
        ],
        'C' : [
                (['T', 'tk0'], {'tk3', 'tk8'}), 
                (['Y', 'tk2', 'W'], {'tk9', 'tk1'}), 
                (['W', 'tk2', 'A'], {'tk2', 'tk1', 'tk3'})
        ]
    }

def gen_asdr(pred_set):
    """writes to a file python code that can perform ASDR
    Parameters
    ----------
    pred_set: a prediction set, such as the returned by 'grammar_from_file(...)'
    """
    # PRED.item = X: ([...], {...})
    f_def = Template("def $id():")
    for X, rules in pred_set.items():
        print(f_def.substitute(id=X))
        gen_nont_call(X, rules)


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
    print(cond)

def build_bool_xpr(pred, ini=False):
    _if = ("if" if ini else "elif")
    or_cnd = TAB + _if + " "
    compare = Template("$get_token() == '$cur_symbol' || ")
    for sym in pred:
        or_cnd += compare.substitute(get_token=TOKEN_FUN, cur_symbol=sym)
    or_cnd = or_cnd[:-4]
    or_cnd += ":\n"
    return or_cnd

def build_cnd_body(alpha):
    emparejar = Template(TAB*2 + "$empar_fun('$terminal')")
    nont_call = Template(TAB*2 + "$nont_fun()")
    body = ""
    for sym in alpha:
        if sym.islower():
            cmd = emparejar.substitute(empar_fun=EMPAR_FUN, terminal=sym)
        else:
            cmd = nont_call.substitute(nont_fun=sym)
        body += cmd + '\n'
    return body

def build_else(rules):
    cnd = TAB + "else:\n" + TAB*2 + "raise SyntaxError("
    expect = Template("'$token', ")
    for r in rules:
        for tk in r[1]:
            cnd += expect.substitute(token=tk)
    cnd = cnd[:-2] + ")"
    return cnd
        
if __name__ == "__main__":
    main()