#!/usr/bin/python3

import os
import bibtexparser

def sort_bib_database_by_date(bib_database):
    sorted_entries = sorted(bib_database.entries,
                            key=lambda x: (x.get('year', ''), x.get('month', '')),
                            reverse=True)
    bib_database.entries = sorted_entries

def format_ieeetran(entry):
    authors = entry.get('author', '').split(' and ')

    author_list = ', '.join(author.split(',')[-1].strip() + ' ' + author.split(',')[0].strip() for author in authors)
    last_comma_index = author_list.rfind(',')    
    # Replace the last comma with "and"
    if last_comma_index != -1:
        author_list = author_list[:last_comma_index] + ' and' + author_list[last_comma_index+1:]

    title = entry.get('title', '')
    title = title.replace("{", "").replace("}", "")

    journal = entry.get('journal', '')
    journal = journal.replace("{", "").replace("}", "")
    year = entry.get('year', '')
    conference = entry.get('booktitle', '')
    conference = conference.replace("{", "").replace("}", "")

    month_abbreviations = {
        'jan': 'January',
        'feb': 'February',
        'mar': 'March',
        'apr': 'April',
        'may': 'May',
        'jun': 'June',
        'jul': 'July',
        'aug': 'August',
        'sep': 'September',
        'oct': 'October',
        'nov': 'November',
        'dec': 'December'}
    month = entry.get('month', '')
    if month in month_abbreviations.keys():
        month = month_abbreviations[month]

    volume = entry.get('volume', '')
    number = entry.get('number', '')
    pages = entry.get('pages', '')
    doi = entry.get('doi', '')

    ieee_str = f"{author_list}, \"**{title}**\", "
    if journal is not '':
        ieee_str += f"*{journal}*, "
    if conference is not '':
        ieee_str += f" In *{conference}*, "
    if volume is not '':
        ieee_str += f"vol. {volume}, "
    if number is not '':
        ieee_str += f"no. {number}, "
    if pages is not '':
        ieee_str += f"pp. {pages}, "
    if year is not '':
        ieee_str += f"{year}"
        if month is not '':
            ieee_str += f", "
        else:
            ieee_str += f". "
    if month is not '':
        ieee_str += f"{month}. "
    if doi is not '':
        ieee_str += f"<https://doi.org/{doi}>"

    return ieee_str



bib_db = {}

with open('IDA_Wireless_Group.bib') as file:
    bibtex_str = file.read()

    bib_db = bibtexparser.loads(bibtex_str)
    sort_bib_database_by_date(bib_db)

os.remove("pub_list.md")
f = open("pub_list.md", "a")



for entry in bib_db.entries:
    # print(entry)
    print("-------------------")
    string = format_ieeetran(entry)
    print(string)
    f.write(string + "\n\n")

f.close
    
