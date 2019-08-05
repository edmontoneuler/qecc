# qecc
qecc is  suite of Python scripts for performing Quantum Espresso density-functional theory calculations on Compute Canada clusters. 

## Why Python? Couldn't you just do this all in Bash?

Sure could. In fact, I think most people do. Here are the main reasons I opted for Python.

1) Familiarity. I started my first DFT project after I had learned the basics of Python, but before I had learned anything about Bash or regular expressions. Doing my scripting in Python let me hit the ground running. Furthermore, since Python is the language of instruction at my university, writing my code in Python ensures that it will be useful (or at least readable) to new members of the research group. 

2) Mathematics. A lot of DFT scripting involves the evaluation of mathematical expressions to generate a list of parameters for the input file, e.g. if we were performing a convergence test on the value of a lattice parameter, we would need to calculate the new lattice vectors/atomic coordinates for each new parameter value. Evaluating mathematical expressions is much more straightforward in Python than in Bash, especially for someone with a physics background. 







