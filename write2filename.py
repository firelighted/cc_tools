# -*- coding: utf-8 -*-
"""
Created on Thu Jan 19 21:36:55 2017

@author: Sarah
"""
testing = 0

def write2filename(text_or_nums, filename, aftertext=None, afternumlines=1, replace=None):
    """
    write2filename:
    This function will append text or numbers to a file. It has optional arguments
    that specify whether the text is appended after a certain string currently in the 
    file. Alternately, the text or numbers can be appended some number of lines after
    the certain string. 
    Ex. file.txt:
    #==
    235
    235	
    #==
    ew
    ar
    
    >> write2filename('this is inserted', 'file.txt', '#==', 1)
    file.txt
    e
    at
    #==
    235
    this is inserted235	
    #==
    this is insertedew
    ar
    """    
    
    if aftertext == None:
        with open(filename, 'a') as f: # append text to the end
            f.write(str(text_or_nums))
        return 1
    else:
        counter = 0  
        f = open(filename,"r+")
        lines = f.readlines()
        listrange = range(len(lines))
        for i in listrange:
             if lines[i].startswith(aftertext):
                    # Before the line three lines after this, i.e. 2 lines later.
                    lines.insert(i+afternumlines,text_or_nums)
                    counter +=1
                    editline = i+afternumlines
              f.seek(0)
              for line in lines:
                f.write(line)
        #f.close
        return counter
if testing: 
    testfile = 'newfile.txt'
    write2filename([(1, 1), (3,3)], testfile)
    write2filename('\n#===\n', testfile)
    write2filename('werwe\n', testfile)
    write2filename('wetrewre\n', testfile)
    write2filename('text\n', testfile)
    write2filename('[(1, 1), (3, 3)]\n', testfile)
    write2filename('#===\n', testfile)
    write2filename('SEVEN!\n', testfile, aftertext='SIX', afternumlines=1)
    write2filename('WHOOOOOOOOO', testfile, 'WERE WE', 1, '[(1, 1), (3, 3)]')