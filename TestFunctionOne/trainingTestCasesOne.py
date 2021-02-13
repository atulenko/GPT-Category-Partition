#Generate test cases for the modify_text function in the python programming language.

# Test Case 6  		(Key = 1.2.2.2.)
#    sort Value                   :  True
#    numChars Value               :  None
#    Number of lines of document  :  Many
#    Content of lines of document :  Non-alphanumeric and alphanumeric characters
def test_case_6():
    document = "FDHJ*329 \n" +
               "car8\n" +
               "34Fg()"
    
    numChars = None
    sort = True
    result = modify_text(document, numChars, sort)
#end

# Test Case 11 		(Key = 1.3.2.4.)
#    sort Value                   :  True
#    numChars Value               :  random value
#    Number of lines of document  :  Many
#    Content of lines of document :  Alphanumeric characters both numbers and letters
def test_case_11():
    document = "A2312AfdA \n" +
               "22bb23bb\n" +
               "Cfas23CC \n" +
               "bobthebuild \n"
    
    numChars = 42
    sort = True
    result = modify_text(document, numChars, sort)
#end

# Test Case 15 		(Key = 2.3.2.2.)
#    sort Value                   :  False
#    numChars Value               :  random value
#    Number of lines of document  :  Many
#    Content of lines of document :  Non-alphanumeric and alphanumeric characters
def test_case_15():
    document = "A2312AfdA \n" +
               "22bb23bb\n" +
               "&&\n" +
               "Cf534@##23CC \n" +
               "bo$$4543ild \n"
    
    numChars = 67
    sort = False
    result = modify_text(document, numChars, sort)
#end

# Test Case 17 		(Key = 2.3.2.4.)
#    sort Value                   :  False
#    numChars Value               :  random value
#    Number of lines of document  :  Many
#    Content of lines of document :  Alphanumeric characters both numbers and letters
def test_case_17():
    document = "A2312AAA \n" +
               "bb23bb\n" +
               "CC323CC "
    
    numChars = 42
    sort = False
    result = modify_text(document, numChars, sort)
#end

# Test Case 7  		(Key = 1.2.2.3.)
#    sort Value                   :  True
#    numChars Value               :  None
#    Number of lines of document  :  Many
#    Content of lines of document :  Both capitalization and non-capitalization of alphanumeric characters
def test_case_7():
    document = "AAAA \n" +
               "bbbb\n" +
               "CCCC "
    
    numChars = None
    sort = True
    result = modify_text(document, numChars, sort)
#end