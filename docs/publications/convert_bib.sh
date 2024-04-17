#! bin/bash

pandoc -t markdown_strict --citeproc pandoc-bib.md -o publication_list.md --bibliography IDA_Wireless_Group.bib