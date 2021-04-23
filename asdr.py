def S():
  if get_curr_token() == 'cinco' or get_curr_token() == 'tres' or get_curr_token() == 'seis' or get_curr_token() == 'uno' or get_curr_token() == 'cuatro':
    A()
    match('uno')
    B()
    C()
  elif get_curr_token() == 'cinco' or get_curr_token() == 'tres' or get_curr_token() == 'seis' or get_curr_token() == 'uno' or get_curr_token() == 'cuatro':
    S()
    match('dos')
  else:
    raise SyntaxError('cinco', 'tres', 'seis', 'uno', 'cuatro')

def D():
  if get_curr_token() == 'seis':
    match('seis')
  elif get_curr_token() == 'dos' or get_curr_token() == 'uno' or get_curr_token() == 'tres' or get_curr_token() == 'seis' or get_curr_token() == 'cuatro' or get_curr_token() == '$':
    pass
  else:
    raise SyntaxError('seis', 'dos', 'uno', 'tres', 'cuatro', '$')

def A():
  if get_curr_token() == 'cinco' or get_curr_token() == 'tres' or get_curr_token() == 'seis' or get_curr_token() == 'cuatro' or get_curr_token() == 'uno':
    B()
    C()
    D()
  elif get_curr_token() == 'cinco' or get_curr_token() == 'tres' or get_curr_token() == 'seis' or get_curr_token() == 'cuatro':
    A()
    match('tres')
  elif get_curr_token() == 'tres' or get_curr_token() == 'uno':
    pass
  else:
    raise SyntaxError('cinco', 'tres', 'seis', 'cuatro', 'uno')

def C():
  if get_curr_token() == 'cinco':
    match('cinco')
    D()
    B()
  elif get_curr_token() == 'dos' or get_curr_token() == '$' or get_curr_token() == 'tres' or get_curr_token() == 'seis' or get_curr_token() == 'uno':
    pass
  else:
    raise SyntaxError('cinco', 'dos', '$', 'tres', 'seis', 'uno')

def B():
  if get_curr_token() == 'seis' or get_curr_token() == 'cuatro':
    D()
    match('cuatro')
    C()
    match('tres')
  elif get_curr_token() == 'dos' or get_curr_token() == '$' or get_curr_token() == 'cinco' or get_curr_token() == 'tres' or get_curr_token() == 'seis' or get_curr_token() == 'uno':
    pass
  else:
    raise SyntaxError('seis', 'cuatro', 'dos', '$', 'cinco', 'tres', 'uno')

