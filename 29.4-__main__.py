# Not much to show/demonstrate here. Most commonly recognized by the dunder name dunder main idiom. 

""""
If the file is being run top-level then python sets the attribute __name__ to "__main__" when it starts. 
If however the file is being imported, __name__ is set to whatever it was saved as. So if I call the program from the
terminal, ie 
$ python somefile.py ==> somefile.__name__ = "__main__"

This sets the program to run directly.

but if I import it within another program  somefile.__name__ = "somefile"
and I can execute functions from that program to run when called explicitly

from somefile import function

x.function(y)

By placing the following check you can run certain conditional code only when program is called directly.
"""

if __name__ == "__main__":
    # execute some code
    # often place for unittests