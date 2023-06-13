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
![image](https://github.com/ht21992/Python-Scripting-Project/assets/47816410/e7d9bc8e-050b-4941-9e05-4eea5c0b9ad7)


## library Folder After Running The Code
![image](https://github.com/ht21992/Python-Scripting-Project/assets/47816410/75770198-9797-4388-8d57-30a2a28301fa)

## A-Study-In-Scarlet.json
![image](https://github.com/ht21992/Python-Scripting-Project/assets/47816410/10cfa763-5d5d-4e27-8fab-4f3c0aa6e8db)

## metadata.json
![image](https://github.com/ht21992/Python-Scripting-Project/assets/47816410/97460f3b-1525-48af-a9ca-467ad5ac85f2)
