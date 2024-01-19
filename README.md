# Simple-Pyramid-Decoder-Python
This is a decoder for a text script that spits out an output of a provided code

Sample User Prompt:

3 hate  
6 school  
2 cats  
4 dogs  
1 I  
5 you  

When these values are ordered in a pyramid, they should look like this:  
1  
2 3  
4 5 6  

Such that, the expected output must be the phrases that are correlated to the numbers at the end of each line.
With the following example, the message should be:  
1: I  
3: hate  
6: school  

where the decoder spits out the string "I hate school"
