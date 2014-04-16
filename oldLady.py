#-------------------------------------------------------------------------------
# Name:        oldLady.py
# Purpose:     Demo of program control, loops, branches, etc.
#
# Author:      Konrad Roeder, adapted from the nusery rhyme
#              There was an Old Lady song from the
#              Secret History of Nursery Rhymes Book
#              www.rhymes.uk/there_was_an_old_lady.htm
#
# Created:     04/16/2014
# Copyright:   (cc) Konrad Roeder 2014
# Licence:     CC by 4.0
#-------------------------------------------------------------------------------

#There are seven animals in this song, one for each verse
animalName = ['fly','spider','bird','cat','dog','cow','horse']

#Each verse in the song starts with this section, printing this line
def printSectionA(verse):
    print("There was an old lady who swallowed a",animalName[verse-1])

#In section B, the line is different for each verse
def printSectionB(verse):
    #if (verse == 1):  Do nothing
    if (verse == 2):
        print("That wriggled and wiggled and tickled inside her")
    elif (verse == 3):
        print("How absurd to swallow a bird")
    elif (verse == 4):
        print("Fancy that to swallow a cat")
    elif (verse == 5):
        print("What a hog to swallow a dog")
    elif (verse == 6):
        print("I don't know how she swallowed a cow")
    elif (verse == 7):
        print("She's dead, of course!")

def printSectionC(verse):
    #This section only has lines in the middle five verses
    if (verse < 7):
        #The for loop drops through on the first verse
        #In verses 2-6, it prints one line less than the verse number
        for line in range(verse-1, 0, -1):
            print("She swallowed the",animalName[line],
                "to catch the", animalName[line-1])

def printSectionD(verse):
    #This sections exists only in the first six verses
    if (verse < 7):
        print("I don't know why she swallowed a fly - Perhaps she will die!")
        print("")

def song():
    #Print the title
    print("There was an Old Lady song")
    print("")
    #Print each of the seven verses
    for verse in range(1,8):
        #Each verse has four sections
        printSectionA(verse)
        printSectionB(verse)
        printSectionC(verse)
        printSectionD(verse)
    #Print the song's coda (ending)
    print("")
    print("There was an Old Lady song")

song()

