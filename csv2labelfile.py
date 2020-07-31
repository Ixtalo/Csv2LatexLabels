#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
AST, 06.11.2018

Format of CSV input:  

| Datum |	Was? |	Wo gekaut? | Wert? | Als Etikett drucken? |
|---|---|---|---|---|
| 21.10.2015 |	Raspberry Pi 2 | XYZ  | 19.10 | 75,99 € | 1 |


"""

import os
import sys
import csv
from codecs import open

MAXTEXTLENGTH = 52




with open('Inventar-Elektronikbauteile - Tabellenblatt1.csv', 'r', 'utf8') as fin:
    with open('names.dat', 'w', 'utf8') as fout:
        reader = csv.reader(fin)
        for i,row in enumerate(reader):
            if i==0:
                ## skip header line
                continue
                
            try:
                date,item,seller,amount,price,total_price,shipping_costs,toprint = row
            except ValueError as ex:
                print("Error in line %d: %s, [%s]" % (i, ex, row))
                sys.exit(1)
            
            if not toprint:
                ## skip items not explicitly marked as to be printed
                continue

            ## trim long titles
            if len(item) > MAXTEXTLENGTH:
                item = "%s..." % item[:MAXTEXTLENGTH]

            fout.write("\\textbf{%s}\n" % item)
            if seller:
                fout.write("%s\n" % seller)
            fout.write("\\small{%s, %s x %s}\n" % (date, amount, price))

            fout.write('\n'*2)

