#!/usr/bin/python
import argparse
import csv
import json
import os, sys
import urllib
import urllib2

BASE_DIR = os.path.dirname(os.path.dirname(__file__))
INFILE = os.path.join(BASE_DIR, 'input', 'glossary.csv')
OUTPUT_DIR = os.path.join(BASE_DIR, 'output')

CSV_FORMAT = {
              'term_en': 0,
              'desc_en': 1,
              'term_ti': 2,
              'desc_ti': 3,
              'credit_ti': 4,
              'term_am': 5,
              'desc_am': 6,
              'credit_am': 7,

              }

def run(): 
    
    current_alpha = None
    alphabet_used = []
    f = None
    
    with open(INFILE, 'rb') as csvfile:
        file_reader = csv.reader(csvfile, delimiter=',', quotechar='"')
        for counter, row in enumerate(file_reader):
            # skip first row as has the headings
            if counter == 0:
                continue
            
            term_en = row[CSV_FORMAT['term_en']]
            print term_en
            if term_en[0].lower() != current_alpha:
                if f and current_alpha:
                    f.write("</table>\n</body></html>")
                    f.close()
                current_alpha = term_en[0].lower()
                out_file = os.path.join(OUTPUT_DIR, current_alpha + ".html")  
                f = open(out_file, 'w') 
                f.write("<html>\n<head>")
                f.write ("<meta http-equiv=\"Content-Type\" content=\"text/html;charset=utf-8\" /></head>\n<body>\n<table>\n")
                f.write("<tr><th>Term</th><th>Term (lang)</th><th>Definition</th></tr>\n")
    
            f.write("<tr>")
            f.write("<td>")
            f.write(term_en)
            f.write("</td>")
            f.write("<td>")
            f.write(term_en)
            f.write("</td>")
            f.write("<td>")
            f.write(row[CSV_FORMAT['desc_en']])
            f.write("</td>")
            f.write("</tr>\n")
            

            if row[CSV_FORMAT['term_ti']]:
                f.write("<tr>")
                f.write("<td>")
                f.write("&nbsp;")
                f.write("</td>")
                f.write("<td>")
                f.write(row[CSV_FORMAT['term_ti']])
                f.write("</td>")
                f.write("<td>")
                f.write(row[CSV_FORMAT['desc_ti']])
                f.write("</td>")
                f.write("</tr>\n")
            
            if row[CSV_FORMAT['term_am']]:
                f.write("<tr>")
                f.write("<td>")
                f.write("&nbsp;")
                f.write("</td>")
                f.write("<td>")
                f.write(row[CSV_FORMAT['term_am']])
                f.write("</td>")
                f.write("<td>")
                f.write(row[CSV_FORMAT['desc_am']])
                f.write("</td>")
                f.write("</tr>\n")
            
    # create the index
    output_index = os.path.join(OUTPUT_DIR,"index.hml")    
    f = open(output_index, 'w') 
    
    f.write("<html><head><title>Glossary</title></head><body>") 
    
    f.write("</body></html>") 
    f.close()
    
if __name__ == "__main__":
    parser = argparse.ArgumentParser()

    args = parser.parse_args()
    run() 