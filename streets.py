import sys
import re
import simplejson as json
import csv
from pprint import pprint

class Blocks():
  def __init__(self):
    self.blocks = {}

  def __len__(self):
    return len(self.blocks)

  def add(self, street):
    new_block = Block(street)
    key = "%s %s %s" % (new_block.direction, new_block.street, new_block.suffix)
    key = re.sub('[^0-9a-zA-Z ]+', '', key)
    try:
      self.blocks[key].append(new_block)
    except KeyError:
      self.blocks[key] = [new_block]

  def reg(self, r):
    lowest = int(r[0])
    highest = int(r[1])
    key = re.sub('[^0-9a-zA-Z ]+', '', r[2])
    reg_text = r[3].replace("'", '')
    reg_key = r[4].replace("'", '').strip()
    try:
      for block in self.blocks[key]:
        if block.lowest in range(lowest, highest) or block.highest in range(lowest, highest):
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

  def __init__(self, f):
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
  with open(sys.argv[1]) as f:
    dialect = csv.Sniffer().sniff(f.read(1024))
    f.seek(0)
    streets = csv.reader(f, dialect)
    for street in streets:
      all_blocks.add(street)
  with open(sys.argv[2]) as f:
    dialect = csv.Sniffer().sniff(f.read(1024))
    f.seek(0)
    regs = csv.reader(f, dialect)
    for reg in regs:
      all_blocks.reg(reg)
  print json.dumps(all_blocks.dump(), sort_keys = True, indent = 4)

if __name__ == '__main__':
  main()

