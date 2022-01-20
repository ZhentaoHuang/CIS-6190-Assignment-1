"""
Author: Zhentao Huang
This file is used to split the title and text into sequence of strings.
"""
from re import S
from nltk import sent_tokenize


def split(infile, outfile):
    """
    This function is used to conduct the sentence splitting for both title and body texts. 
    Inspired by the sample program.

    Args:
        infile ([file]): [input file]
        outfile ([file]): [output file]
    """
    lines = infile.readlines()
    section = []    #a temporary buffer used to store the section between labels
    for line in lines:
        if line[0] == '$':
            #if the first char in the line is "$", then the line is a label
            
            if len(section) == 0:
                #if there is no lines in the "section" then write the current label
                outfile.write(line)
                next
            else:
                #if there are contents in the "section", write the content first then write the label
                buffer = ' '.join(line[:-1] for line in section)
                sents = sent_tokenize(buffer)
                for sent in sents:
                    outfile.write(sent + '\n')
                section = []
                outfile.write(line)

        else:
            #if it is not label, add the line into "section"
            section.append(line)

    #Write what's left in the section when reach the end of the file       
    buffer = ' '.join(line[:-1] for line in section)
    sents = sent_tokenize(buffer)
    for sent in sents:
        outfile.write(sent + '\n')
    

input = open('samples.txt', 'r')
output = open('samples.splitted', 'w')
split(input, output)
input.close()
output.close()