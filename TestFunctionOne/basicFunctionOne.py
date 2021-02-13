
# TextModifier
# This function is based off of a function we developed for an assignment on black-box testing for Georgia Tech's CS 6300 class.
# It is intended to be a basic function in order to test the viability of the GPT-3 based test case content generation.
# In:
# - document: String containing arbitray content with lines delimated by the newline character.
# - numChars: Nullable integer repersenting the number of characters to leave in each line.
# - sort: Nullable boolean repersenting if the input document should be sorted. If the input is to be sorted:
#   1. Ignore but keep non-alphanumeric characters.
#   2. Numbers preceed letters.
#   3. Capital letters proceed lower-case.
#   4. Lines with only non-alphanumeric characters are removed.

def modify_text(document, numChars = None, sort = None):
    pass
