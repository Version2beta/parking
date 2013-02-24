from streets import *
from expecter import expect
from pprint import pprint

blocks = [
  '1;19139;"COUNTY LINE";"W";"RD";6801;7599;6800;7598;"0102000000020000000AD7A3F0EF564341F6285C8FC4EB1A4189416095E2514341D578E9A6D0EA1A41";"STREETS"',
  '2;19140;"COUNTY LINE";"W";"RD";7601;8399;0;0;"01020000000200000089416095E2514341D578E9A6D0EA1A4108AC1C4AAC4C4341CDCCCCCCB5E91A41";"STREETS"',
  '3;19141;"COUNTY LINE";"W";"RD";8401;9099;8400;9098;"01020000000200000008AC1C4AAC4C4341CDCCCCCCB5E91A419CC420B08B47434117D9CEF767E81A41";"STREETS"',
  '4;19095;"COUNTY LINE";"W";"RD";9101;9499;9100;9498;"0102000000020000009CC420B08B47434117D9CEF767E81A4179E92601DA44434162105839A7E71A41";"STREETS"',
  '5;802834;"COUNTY LINE";"W";"RD";9501;9899;9500;9898;"01020000000200000079E92601DA44434162105839A7E71A41CBA145B65342434108AC1C5AF2E61A41";"STREETS"'
]

regs = [
  "6800,6899,'W COUNTY LINE RD','No Winter Night Parking',noWinter",
  "6900,6999,'W COUNTY LINE RD','No Winter Night Parking',noWinter",
  "7000,7099,'W COUNTY LINE RD','No Winter Night Parking',noWinter",
  "7100,7199,'W COUNTY LINE RD','No Winter Night Parking',noWinter",
  "7200,7299,'W COUNTY LINE RD','No Winter Night Parking',noWinter",
  "7300,7399,'W COUNTY LINE RD','No Winter Night Parking',noWinter",
  "7400,7499,'W COUNTY LINE RD','No Winter Night Parking',noWinter",
  "7500,7599,'W COUNTY LINE RD','No Winter Night Parking',noWinter",
  "7600,7699,'W COUNTY LINE RD','No Winter Night Parking',noWinter",
  "7700,7799,'W COUNTY LINE RD','No Winter Night Parking',noWinter",
  "7800,7899,'W COUNTY LINE RD','No Winter Night Parking',noWinter",
  "7900,7999,'W COUNTY LINE RD','No Winter Night Parking',noWinter",
  "8000,8099,'W COUNTY LINE RD','No Winter Night Parking',noWinter",
  "8100,8199,'W COUNTY LINE RD','No Winter Night Parking',noWinter",
  "8200,8299,'W COUNTY LINE RD','No Winter Night Parking',noWinter",
  "8300,8399,'W COUNTY LINE RD','No Winter Night Parking',noWinter",
  "8400,8499,'W COUNTY LINE RD','No Winter Night Parking',noWinter",
  "8500,8599,'W COUNTY LINE RD','No Winter Night Parking',noWinter",
  "8600,8699,'W COUNTY LINE RD','No Winter Night Parking',noWinter",
  "8700,8799,'W COUNTY LINE RD','No Winter Night Parking',noWinter",
  "8800,8899,'W COUNTY LINE RD','No Winter Night Parking',noWinter",
  "8900,8999,'W COUNTY LINE RD','No Winter Night Parking',noWinter",
  "9000,9099,'W COUNTY LINE RD','No Winter Night Parking',noWinter",
  "9100,9199,'W COUNTY LINE RD','No Winter Night Parking',noWinter",
  "9200,9299,'W COUNTY LINE RD','No Winter Night Parking',noWinter",
  "9300,9399,'W COUNTY LINE RD','No Winter Night Parking',noWinter"
  "9400,9499,'W COUNTY LINE RD','No Winter Night Parking',noWinter",
  "9500,9599,'W COUNTY LINE RD','No Winter Night Parking',noWinter",
  "9600,9699,'W COUNTY LINE RD','No Winter Night Parking',noWinter",
  "9700,9799,'W COUNTY LINE RD','No Winter Night Parking',noWinter",
  "9800,9899,'W COUNTY LINE RD','No Winter Night Parking',noWinter",
  "9900,9999,'W COUNTY LINE RD','No Winter Night Parking',noWinter"
]

all_blocks = Blocks()
key = "W COUNTY LINE RD"
for b in blocks:
  all_blocks.add(b)

def test_parse_address_range():
  expect(Block.Parse_address_range([0, 1, 1, 1])) == (1, 1)
  expect(Block.Parse_address_range([0, 1, 1, 1])) == (1, 1)

def test_import_a_street():
  block = Block(blocks[0])
  expect(block.lowest) == 6800

def test_import_a_street_with_zero_addresses():
  block = Block(blocks[1])
  expect(block.lowest) == 7601

def test_blocks():
  expect(len(all_blocks)) == 1

def test_import_regs():
  all_blocks.reg(regs[0])
  expect(len(all_blocks.blocks[key][0].regs)) == 1
