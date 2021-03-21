from collections import deque
import re

def main():
  st = StateMachine('in/01.txt')
  st.next_token()

class StateMachine:
  def __init__(self, filename):
    self.source = open(filename, 'r')
    self.buffer = deque(list(self.source.read(10)))
    self.state = 0

  def next_token(self):
    while 1:
      self.buffer.append(self.source.read(1))
      c = self.buffer.popleft()
      if c == '': # EOF
        break
      print(c)
      state = self.next_state(c)
      print(state)

  def next_state(self, c):
    if self.state == 0:
      if re.match("[a-zA-Z]", c):
        return (1, 0)
      elif re.match("[0-9]", c):
        return (2, 0)
      elif re.match("-", c):
        return (5, 0)
    elif self.state == 1:
      if re.match("[a-zA-Z0-9]|[_]", c):
        return (1, 0)
      else:
        return (0, 1)
    elif self.state == 2:
      if re.match("[0-9]", c):
        return (2, 0)
      elif re.match("\.", c):
        return (3, 0)
      else:
        return (0, 0) # INTEGER
    elif self.state == 3:
      if re.match("[0-9]", c):
        return (4, 0)
      else:
        return (0, 2) # INTEGER
    elif self.state == 4:
      if re.match("[0-9]", c):
        return (4, 0)
      else:
        return (0, 1) # FLOAT
    elif self.state == 5:
      if re.match("[0-9]", c):
        return (2, 0)
      else:
        return (-1, 0)

  def turn_off(self):
    self.source.close()

if __name__ == '__main__':
  main()