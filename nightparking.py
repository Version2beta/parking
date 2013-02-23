# Imports from other standard dependencies
from bs4 import BeautifulSoup
import requests


def grab_streets():
    '''
    Scraper to get current Milwaukee street parking regulation
    information.

    Created for Open Data Day 2013 by Allan James Vestal
    (ajvestal@jrn.com) and the Milwaukee Data Initiative
    (milwaukeedata.org).
    '''
    url = 'http://mpw.milwaukee.gov/services/winterregs'

    html = requests.get(url).text
    soup = BeautifulSoup(html, "html5lib")

    tables = soup.findAll('table', class_='parkingtable')

    all_streets = []
    for table in tables:
        trs = table.findAll('tr')[2:]

        for tr in trs:
            cells = tr.findAll('td')

            start_range = cells[0].span.text.strip().split('-')[0].strip()
            end_range = cells[0].span.text.strip().split('-')[1].strip()

            blocks = split_blocks(int(start_range), int(end_range))

            for block in blocks:
                block_regulation = {}

                block_regulation['start_range'] = block[0]
                block_regulation['end_range'] = block[1]
                block_regulation['street_name'] = cells[1].span.text.strip()
                block_regulation['regulation_text'] = cells[2].a.text
                block_regulation['regulation_href'] = cells[2].a['onclick'
                                                            ].split('#')[1
                                                            ].split("'")[0]
                all_streets.append(block_regulation)

    return all_streets


def split_blocks(start, end):
    '''
    Given a starting and ending address, returns a list of blocks in
    between this range.

    For example, given 18 and 539 (representing the area between 18 and
    539 Elm St., say), will return a list containing the values 18 to
    99, 100 to 199, 200 to 299, 300 to 399, 400 to 499 and 500 to 539.

    Takes two required arguments:
        * start: an integer representing the start of the range.
        * end: an integer representing the end of the range.

    Created for Open Data Day 2013 by Allan James Vestal
    (ajvestal@jrn.com) and the Milwaukee Data Initiative
    (milwaukeedata.org).
    '''
    address_range = [0, 99]
    continue_generator = True
    valid_ranges = []

    while continue_generator:
        if address_range[1] <= start:
            address_range[0] += 100
            address_range[1] += 100
        elif address_range[1] > start and address_range[1] <= end:
            continue_generator = True
            if address_range[0] < start:
                valid_ranges.append([start, address_range[1]])
            else:
                valid_ranges.append([address_range[0], address_range[1]])
            address_range[0] += 100
            address_range[1] += 100
        elif address_range[1] > end:
            if end >= address_range[0]:
                valid_ranges.append([address_range[0], end])
            continue_generator = False
        else:
            pass

    return valid_ranges
