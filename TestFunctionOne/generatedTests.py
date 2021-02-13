
#Running Test Case: 

#Test Case 17 		(Key = 2.3.2.4.)
#   sort Value                   :  False
#   numChars Value               :  random value
#   Number of lines of document  :  Many
#   Content of lines of document :  Alphanumeric characters both numbers and letters
def test_case_17():
    document = "A2312AAA \n" +
               "bb23bb\n" +
               "CC323CC "
    
    numChars = 42
    sort = False
    result = modify_text(document, numChars, sort)

#Running Test Case: 
#Test Case 8  		(Key = 1.2.2.4.)
#   sort Value                   :  True
#   numChars Value               :  None
#   Number of lines of document  :  Many
#   Content of lines of document :  Alphanumeric characters both numbers and letters
def test_case_8():
    document = "A2312AfdA \n" +
               "22bb23bb\n" +
               "Cfas23CC \n" +
               "bobthebuild \n"
    
    numChars = None
    sort = True
    result = modify_text(document, numChars, sort)

#Running Test Case: 
#Test Case 12 		(Key = 2.2.2.2.)
#   sort Value                   :  False
#   numChars Value               :  None
#   Number of lines of document  :  Many
#   Content of lines of document :  Non-alphanumeric and alphanumeric characters
def test_case_12():
    document = "A2312AfdA \n" +
               "22bb23bb\n" +
               "Cfas23CC \n" +
               "bobthebuild \n"
    
    numChars = None
    sort = False
    result = modify_text(document, numChars, sort)
