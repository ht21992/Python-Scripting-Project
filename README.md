### Python-Scripting-Project

Assumptions:

- data directory contains many files and directories
- you are only interested in the pdf ebooks
- each ebook is stored in a directory with a name that contains the word "ebook" or the data direcrtoy itself
- each ebook directory contains a single .pdf file that its meta data and number of pages must be extracted from that file


Project Steps/Requirements:

- Find all ebooks directories from /data (including the ebooks inside the data folder)
- create folders for the ebooks that have no subdirectory(such as Paycheck-to-Paycheck.pdf)
- Create a new /library directory
- Copy and remove the "ebook" suffix of all ebooks into the /library directory
- Create a .json file with the information about the all ebooks
- Create a seprate .json file with the meta data information about the ebook

## data Folder Before Running The Code
![image](https://github.com/ht21992/Python-Scripting-Project/assets/47816410/1e56e485-7384-4f0f-a724-868263033074)

## library Folder After Running The Code
![image](https://github.com/ht21992/Python-Scripting-Project/assets/47816410/0f484a3b-2162-4bb7-ae43-5df00fb7d989)

## A-Study-In-Scarlet.json
![image](https://github.com/ht21992/Python-Scripting-Project/assets/47816410/a6de4a5f-6f8b-4656-a631-eb82794da482)

## metadata.json
![image](https://github.com/ht21992/Python-Scripting-Project/assets/47816410/22f19dba-48a3-4a3c-9880-791b18def09a)
