# Discord-Archive-Scanner

Python Script Designed to scan a json file archive of a discord channel or dm that was created with Discord-Chat-Exporter

Works by creating a thread for each string that you would like to search for

## Installation:

1) create a list.py file with an array named "strings" and place that in the same directory as the downloaded search.py file
2) rename your .json file from Discord-Chat-Exporter to archive.json and place it in the same directory as the other files
3) the script will then create two text file for each string in the array: one that tells the number of times the string was found, and another that contains every instance of that string
