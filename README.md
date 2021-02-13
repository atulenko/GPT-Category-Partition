# GPT-3 Black box test generation

## Methodology

1. Use the category partition method for generating black-box test case descriptions.
2. Implement a number of test cases as training data
3. Attempt to generate the remaining test cases using the GPT-3 Model

## Preformance Measurment

Still working on this but I am imagining some score or report that includes:
1. % of passing generated tests
2. Branch or edge coverage percentage of the function

## Test Cases

### Case 1:

Simplified function from my CS 6300 class.
String manipulation function with some inputs

I recomend running the reduced.txt.tsl since the prompt in its current form eats a ton of tokens. Or try reducing the pormpt.
It would be great if openapi could cache the prompt so we don't have to re-send it with each case, I couldn't find this on their docs though.

To run this yourself:
python runTests.py -e ./TestFunctionOne/trainingTestCasesOne.py -t ./TestFunctionOne/reduced.txt.tsl -o ./TestFunctionOne/generatedTests.py

## TODO:
1. tons of stuff

## Reference Docs
1. Category Partition Paper: https://www.cc.gatech.edu/~harrold/6340/cs6340_fall2009/Readings/ostrandCategoryPartition88.pdf
2. OpenAi Doc reference: https://beta.openai.com/docs/introduction

TSLgenerator by Dr. Orso
To generate your own tsl files you can get the TSLgenerator binary from this repo:
https://github.com/alexorso/tslgenerator