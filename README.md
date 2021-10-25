# Python Photo Deleter App

## TL;DR
Python app deletes files that aren't in the `good_photos` folder. 

## Problem:
I shoot photos with a Canon RP body and am too cheap to pay for Photoshop therefore I use GIMP with RawTherapee for photo editing. Unfortunately there isn't the best support for .CR3 raw format. The work around is to conver to .DNG files then edit the photos via RawTherapee -> GIMP. In the end I have files in multiple locations that I will have to delete. 

## Solution:
Create a file structure of:
``` 
mainfolder
|
|---CR3
|       file1.CR3
|       file2.CR3
|
|---DNG
|       file1.DNG
|       file2.DNG
|
|---good_photos
|       file1.jpg
|
|---other folder etc.
```

Python program will list all files in `good_photos` folder, remove file extension then loop through all other folders deleting files that do not match file names from `good_photos` folder. 

## Bugs:
* The way the program strips the file extension from files in `good_files` folder could cause an error if the file extension is more than 4 characters. I don't know if this actually exists and this program was intended for the files in the `good_files` folder to be .jpg files.