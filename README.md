# qecc
qecc is  suite of Python scripts for performing Quantum Espresso density-functional theory calculations on Compute Canada clusters. 

## Why Python? Couldn't you just do this all in Bash?

Sure could. In fact, I think most people do. Here are the main reasons I opted for Python.

1) Familiarity. 
I started my first DFT project after I had learned the basics of Python, but before I had learned anything about Bash or regular expressions. Doing my scripting in Python let me hit the ground running, instead of first having to learn a bunch of new syntax. Furthermore, since most physics students have some familiarity with Python, writing my code in Python increases the likelihood that it will be useful to any new group members, particularily undergraduates who have never used another programming language before. 

2) Mathematics. A lot of DFT scripting involves the evaluation of mathematical expressions to generate a list of parameters for the input file, e.g. calculating the atomic structure for a series of lattice paramter values. Evaluating mathematical expressions is much more straightforward in Python than in Bash, especially when you can just import the function that does the calculation for you. 







