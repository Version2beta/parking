import sys
import simplejson as json
from pprint import pprint

class Blocks():
  def __init__(self):
    self.blocks = {}

  def __len__(self):
    return len(self.blocks)

  def add(self, street):
    new_block = Block(street)
    key = "%s %s %s" % (new_block.direction, new_block.street, new_block.suffix)
    try:
      self.blocks[key].append(new_block)
    except KeyError:
      self.blocks[key] = [new_block]

  def reg(self, reg):
    r = reg.split(',')
    lowest = int(r[0])
    highest = int(r[1])
    key = r[2].replace("'", '')
    reg_text = r[3].replace("'", '')
    reg_key = r[4].replace("'", '').strip()
    try:
      for block in self.blocks[key]:
        if lowest in range(block.lowest, block.highest) and highest in range(block.lowest, block.highest):
          block.regs[reg_key] = reg_text
    except KeyError:
      pass

  def dump(self):
    retval = []
    for k in self.blocks:
      for b in self.blocks[k]:
        retval.append(b.to_dict())
    return retval

class Block():
  @classmethod
  def Parse_address_range(self, a):
    a = [int(x) for x in a if int(x) > 0]
    if len(a):
      smallest = min(a)
      largest = max(a)
      return smallest, largest
    else:
      return 0, 0

  def __init__(self, street):
    f = street.split(';')
    self.gid = f[0]
    self.record_number = f[1]
    self.street = f[2].replace('"', '')
    self.direction = f[3].replace('"', '')
    self.suffix = f[4].replace('"', '')
    self.lowest, self.highest = self.Parse_address_range(f[5:9])
    self.regs = {}

  def to_dict(self):
    return dict(
        gid = self.gid,
        record_number = self.record_number,
        direction = self.direction,
        street = self.street,
        suffix = self.suffix,
        lowest = self.lowest,
        highest = self.highest,
        regs = self.regs
        )

def main():
  all_blocks = Blocks()
  for line in open(sys.argv[1], 'r').readlines():
    all_blocks.add(line)
  for line in open(sys.argv[2], 'r').readlines():
    all_blocks.reg(line.replace('"', ''))
  print json.dumps(all_blocks.dump(), sort_keys = True, indent = 4)

if __name__ == '__main__':
  main()

