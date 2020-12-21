run = 1
def prog():
    import os
    psuedo_cwd = str(input("Enter file path: "))

    for root, directories, filenames in os.walk(psuedo_cwd):    #Search all subdirectories of pseudo_cwd
        for filename in filenames:                              #Take each filename
            a = (root + '\\' + filename)                        #Take the absolute file path for each song
            b = str(", ".join(filename.split('- ')[-1:]))       #Split the Bandcamp 'F1-F2-F3' file format and take only the last segment; 'F3', or the song title
            os.system('ren "' + str(a) + '" "' + str(b) + '"')  #Rename the first file, a, to the shorter name, b.

while run == 1:     #Run more than once
    prog()

#Bandcamp albums name each song like this:
#Tower Of The Sun幽霊の次元 - Reset - 01 Guilt.mp3

#If you run this script in Windows and input the directory where the songs are, example:
#E:\github\1\stock

#The songs should be reformatted to look like this:
#01 Guilt.mp3

#This makes them  easier to work with in foobar2000; my preferred music player
#It uses native command prompt stuff to make it work (rudimentary, yes), but it hasn't failed me yet
