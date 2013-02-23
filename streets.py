class Regs():
  def __init__(self, reg):
    pass

class Block():
  def __init__(self, street):
    f = street.split(';')
    self.row_id = f[0]
    self.street = f[2]
    self.direction = f[3]
    self.suffix = f[4]
    self.lowest = min(f[5:8])
    self.highest = max(f[5:8])
    self.regs = {}
