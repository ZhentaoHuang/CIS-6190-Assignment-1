# CIS-6190-Assignment-1
UofG grad course CIS-6190 Assignment 1

Test Environment: Python 3.7.2 linux.socs.uoguelph.ca



* # Sentence Splitting
  * ## Usage
  ```python split.py --Input YourInputFile --Output YourOutputFile```

  The input is set to samples.txt, and the output is set to sample.splitted in default.

  * ## Objectives
  The goal is to split the sentences into sequence of words based on three common end-of-sentence marks: period("."), question("?") and exclamation("!"). The program should also avoid to split the labels which starts with a "$".
  

* # 2. Tokenization
  * ## Usage
  ```python tokenization.py --Input YourInputFile --Output YourOutputFile```

  The input is set to samples.splitted, and the output is set to sample.tokenized in default.

  * ## Objectives
  The goal is to perform tokenization by scanner-generation tool Ply.lex. There are total seven categories: LABEL, WORD, NUMBER, APOSTROPHIZED, HYPHENATED, DELIMITER, and PUNCTUATION. After the tokenization, a post-processing would be applied for HYPHENATED, APOSTROPHIZED and WORD type to split certain type into sequence of tokens.
  
  * ## Test Plan
  The test cases are added at the top of sample.txt file. Such as "this-is-just-a-test's" or "-123abc". Please check the file for full details.

* # 3. POS-Tagging
  * ## Usage
  ```python pos-tag.py --Input YourInputFile --Output YourOutputFile```

  The input is set to samples.tokenized, and the output is set to sample.tagged in default.

  * ## Objectives
  The goal of this program is to apply POS-tagger in NLTK to tag the words with their POS tags. All the output tokens are paired up with their POS tags

* # 4. Data Analysis
  * ## Usage
  ```python data-analysis.py --Input YourInputFile --Output YourOutputFile```

  The input is set to samples.tagged, and the output is set to sample.analysis in default.

  * ## Objectives
  The goal of this program is to analysis the tagged file and generate a summary file. The file indicates: the total amount of documents, the min, avg and max document lengths by the number os sentences/tokens, the average sentence lengths by the number of tokens for the whole data collection as well as all individual documents, etc.
