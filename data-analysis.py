"""Author: Zhentao Huang
This file is used to perform the data-analysis task. The file takes a pos-tagged file as input and output the analysis. Type -h for help.
"""
import argparse


class document:
    """ A class store all the information of a single document
    """

    doc = ""
    content = ""    # The whole content of the document, including "\n"
    index = 0       # Indicates the start of a document in the text
    length_sentences = 0    # Document length by the number of sentences
    length_tokens = 0       # Document length by the number of tokens
    avg_sentence_length = 0 # Average sentence length by the number of tokens

    def __init__(self, doc, index):
        self.doc = doc
        self.index = index

    def postproc(self):
        """This function is used to get rid of the labels and "\n" in the content for further analysis
        """
        processed_content = []
        for line in self.content:
            if(line[0] != '$'):
                processed_content.append(line[:-1])
        self.content = processed_content

    def calc_length(self):
        """This function is used to calculate the document length by sentences and tokens
        """
        self.length_sentences = len(self.content)   # Length by sentences equals to len(content) since the content is splited by sentences
        
        for sentence in self.content:   # Calculate the length by tokens by splittling the sentence by space
            self.length_tokens += len(sentence.split(" "))
        
        self.avg_sentence_length = self.length_tokens / self.length_sentences
       

        

    

def read_documents(input):
    """This function is used to initialize the document objects and perform post-processing for further calculation

    Args:
        input (file): input file

    Returns:
        docs: a list of document objects
    """

    lines = input.readlines()
    docs = []
    count = 0

    # Read the "$DOC" and set the index of the document object
    for line in lines:
        if line[:4] == "$DOC":
            doc = document(line[:-1], count)
            docs.append(doc)
        count = count + 1

    # Set the content of each document based on current index and next one's index
    for i in range(len(docs)):
        if i == len(docs) - 1:  # If it is the last one, set it to the end of the file
            docs[i].content = lines[docs[i].index:]
        else:
            docs[i].content = lines[docs[i].index:docs[i+1].index]
        
    # Post-processing for documents
    for doc in docs:
        doc.postproc()

    return docs

def analyze(input, output):
    """This function is used to perform the data-analysis task.

    Args:
        input (file): Input file
        output (file): Output file
    """
    documents = read_documents(input)
    
    # Calculate the document length
    for doc in documents:
        doc.calc_length()

    lens_sentences = []
    lens_tokens = []

    # Output the data-analysis
    output.write("Total number of documets in the data collection: %s \n\n" %str(len(documents)))
    output.write("------------------------------------------------------------\n")

    for doc in documents:
        output.write("Document Name: %s \n" %doc.doc)
        output.write("Document Length by Sentences: %s \n" %doc.length_sentences)
        output.write("Document Length by Tokens: %s \n" %doc.length_tokens)
        output.write("Average Sentence Length by Tokens: %s \n" %doc.avg_sentence_length)
        output.write("------------------------------------------------------------\n")
        lens_sentences.append(doc.length_sentences)
        lens_tokens.append(doc.length_tokens)


    output.write("Summary: \n")
    output.write("The minimum document length by the number of sentences is: %s \n" %str(min(lens_sentences)))
    output.write("The average document length by the number of sentences is: %s \n" %str(sum(lens_sentences)/len(lens_sentences)))
    output.write("The maximum document length by the number of sentences is: %s \n" %str(max(lens_sentences)))
    output.write("The minimum document length by the number of tokens is: %s \n" %str(min(lens_tokens)))
    output.write("The average document length by the number of tokens is: %s \n" %str(sum(lens_tokens)/len(lens_tokens)))
    output.write("The maximum document length by the number of tokens is: %s \n" %str(max(lens_tokens)))
    output.write("The average sentence length by tokens of the data collection is: %s \n" %str(sum(lens_tokens)/sum(lens_sentences)))
    

def arg_parse():
    """This function is used for command line argument parsing. It utilizes the argparse library. It provides the user with file choice at runtime.

    Returns:
        args: command line arguments
    """

    # Initialize parser
    parser = argparse.ArgumentParser()
    
    # Adding optional argument
    parser.add_argument("-i", "--Input", default="samples.tagged", help = "The input file (default: samples.tagged)")
    parser.add_argument("-o", "--Output", default="samples.analysis", help = "The output file (default: samples.analysis)")
    
    # Read arguments from command line
    args = parser.parse_args()
    
    print("Input: %s" % args.Input)
    print("Output as: % s" % args.Output)

    return args

def main(args):

    input = open(args.Input, 'r')
    output = open(args.Output, 'w')
    
    analyze(input, output)

    input.close()
    output.close()

if __name__ == "__main__":

    args = arg_parse()
    main(args)