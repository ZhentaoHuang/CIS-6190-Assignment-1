""" Author: Zhentao Huang
This file is used for pos-tagging task. The original code is taken from pos-tag.py from SamplePrograms.
"""

from nltk import pos_tag
import argparse

def tag(infile, outfile):
    """This function is used to perform the pos-tagging task. The original code is taken from pos-tag.py from SamplePrograms. It adds a feature to avoid tagging the label.

    Args:
        infile (file): input file
        outfile (file): output file
    """
    lines = infile.readlines()
    for line in lines:
        if(line[0] == '$'):     #if it is a label, then write the original line without tagging
            outfile.write(line)
        else:
            tokens = line.split()
            tagged = pos_tag(tokens)
            paired = [word + '/' + tag for (word, tag) in tagged]
            outfile.write(' '.join(paired) + '\n')

def arg_parse():
    """This function is used for command line argument parsing. It utilizes the argparse library. It provides the user with file choice at runtime.

    Returns:
        args: command line arguments
    """

    # Initialize parser
    parser = argparse.ArgumentParser()
    
    # Adding optional argument
    parser.add_argument("-i", "--Input", default="samples.tokenized", help = "The input file (default: samples.tokenized)")
    parser.add_argument("-o", "--Output", default="samples.tagged", help = "The output file (default: samples.tagged)")
    
    # Read arguments from command line
    args = parser.parse_args()
    
    print("Input: %s" % args.Input)
    print("Output as: % s" % args.Output)


    return args

def main(args):

    input = open(args.Input, 'r')
    output = open(args.Output, 'w')
    
    tag(input, output)

    input.close()
    output.close()

if __name__ == "__main__":

    args = arg_parse()
    main(args)

