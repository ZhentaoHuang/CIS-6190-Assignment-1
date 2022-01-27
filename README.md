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

* # 3. POS-Tagging
  * ## Usage
  ```python pos-tag.py --Input YourInputFile --Output YourOutputFile```

  The input is set to samples.tokenized, and the output is set to sample.tagged in default.

  * ## Objectives

* # 4. Data Analysis
  * ## Usage
  ```python data-analysis.py --Input YourInputFile --Output YourOutputFile```

  The input is set to samples.tagged, and the output is set to sample.analysis in default.

  * ## Objectives
