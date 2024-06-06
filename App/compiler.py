#Kieran Woodrow
#u19304308
#COS341 practical 1. Making the lexer 

#Used for regex expressions in python
import re

#Token class. Used to create successful token objects and output them in the array
class Token:
    def __init__(self, tokenCatagory, word):
      self.tokenCatagory = tokenCatagory
      self.word = word

    #used for formatting nicely
    def __repr__(self): 
        return "Token Catagory: % s Token: % s" % (self.tokenCatagory, self.word)
        
#Error class. Used to create unsuccessful token objects and output them in the array, indicating their line number and token number for error
class Error:
      def __init__(self, errorCatagory, errorCharacter, errorLine, errorIndex):
         self.errorCatagory = errorCatagory
         self.errorCharacter = errorCharacter
         self.errorLine = errorLine
         self.errorIndex = errorIndex

      #used for formatting nicely
      def __repr__(self): 
        return "Error Catagory: % s Token that caused error: % s Line: % s Position: % s " % (self.errorCatagory, self.errorCharacter, self.errorLine, self.errorIndex)

#This is the driver function that calls the lexer
def mainFunction():
   #The lexer returns an array of all tokens. Set the returned array to an array 
   tokensArray = lexerFunction()

   #print('Below is the linked list of tokens. NOTE: If there was an error, it will only display the error with the corresponding line number and index number on that line\n')

   for i, a in enumerate(tokensArray):
      if(i == 0 ):
         print(str(a))

      else:
         print(str(a)+'-')
   exit(0)

#This is the main function that handles the lexer
def lexerFunction():
   #save the input file in a variable. You need to specify the file you would like to open.
   #eg open(test.txt) (The one i used to practice with). On the server, the file is saved under
   #../
   inputFile = open("text.txt")
   #keeps count of inner loop. i.e what number the character is on in the line
   innerLoopCounter = 0
   #keeps count of outer loop. i.e what number line the token is on
   outerLoopCounter = 0
   length = 0
   amount = 0
   #used to hold tokens
   tokensArray=[]
   #keepts track of what DFAstate we are in
   DFAstate=1
   #used to concatonate tokens
   words = ''
   #for each word in the text file
   for line in inputFile:
      outerLoopCounter+=1
      #for each character in the current word
      for currentcharacter in line:
         innerLoopCounter+=1
         #boolean variable for controlling main loop
         flag=True
         #while flag is true/
         #THIS IS ONE GIANT WHILE LOOP. WHILE THERE IS ANOTHER TOKEN TO PROCESS...
         while(flag):
            #set to false immediately after so we can break loop EVENTUALLY
            flag=False
            #if DFAstate is DFAstate1. THIS IS THE STARTING STATE FOR ALL INPUT. 
            if( DFAstate == 1 ):

               #note:
               #DFAstate 1 is the beginning DFAstate. There can be several options in the beginning DFAstate. These options are:
               #'\n', " ", "\'", '=', ';', '<', '>', ',', '(', ')', '{', '}', '-', '0', '[1-9]'
               #There are also these ones that are the starting letters of the keywords:
               #'a', 'e', 'f', 'h', 'i', 'm', 'n', 'o', 'p', 's', 't', 'w'
               #which leaves [b-dgj-lqruvx-z] as another case

               #The last first case is anything else..eg undefined letters in the alphabet (&%$@) or capital letters

               #Order. Do  all the symbols first, then letters, then numbers

               #Note: YOU COULD ALSO DO ONE GIANT SWITCH STATEMENT. BUT PYTHON SWICTH STATEMENT LOOKED
               #WEIRD SO I STUCK TO NESTED ELSE IF STATEMENTS

               #start for all number stuff
               # i.e.'\n', " ", "\'", '=', ';', '<', '>', ',', '(', ')', '{', '}'

               if( currentcharacter == '\n' or currentcharacter == " " ):
                  words=''
                  DFAstate = 1

               elif( currentcharacter == "\'" ):
                  words = words + currentcharacter
                  DFAstate = 2

               elif( currentcharacter == ',' ):
                  words = words + currentcharacter
                  DFAstate = 3

               elif( currentcharacter == ';' ):
                  words = words + currentcharacter
                  DFAstate = 4

               elif( currentcharacter == '>' ):
                  words = words + currentcharacter
                  DFAstate = 5
                  
               elif( currentcharacter == '<' ):
                  words = words + currentcharacter
                  DFAstate = 6

               elif( currentcharacter == '=' ):
                  words = words + currentcharacter
                  DFAstate = 7

               elif( currentcharacter == '\)' ):
                  words = words + currentcharacter
                  DFAstate = 8

               elif( currentcharacter == '\(' ):
                  words = words + currentcharacter
                  DFAstate = 9

               elif( currentcharacter == '\}' ):
                  words = words + currentcharacter
                  DFAstate = 10

               elif( currentcharacter == '\{' ):
                  words = words + currentcharacter
                  DFAstate = 11

               #all special characters are done.
               #start for all number characters 
               #i.e. '0', '-', '[1-9]'

               elif( currentcharacter == '0' ):
                  words = words + currentcharacter
                  DFAstate = 12

               elif( currentcharacter == '-' ):
                  words = words + currentcharacter
                  DFAstate = 13

               elif( re.match( '[1-9]', currentcharacter )):
                  words = words + currentcharacter
                  DFAstate = 14

               #all number characters are done.
               #start for all special letter characters. i.e. keyword first letters
               #i.e. 'a', 'e', 'f', 'h', 'i', 'm', 'n', 'o', 'p', 's', 't', 'w'

               elif( 'a' == currentcharacter ):
                  words = words + currentcharacter
                  DFAstate = 15

               elif( 'e' == currentcharacter ):
                  words = words + currentcharacter
                  DFAstate = 16

               elif( 'f' == currentcharacter ):
                  words = words + currentcharacter
                  DFAstate = 17

               elif( 'h' == currentcharacter ):
                  words = words + currentcharacter
                  DFAstate = 18

               elif( 'i' == currentcharacter ):
                  words = words +currentcharacter
                  DFAstate = 19

               elif( 'm' == currentcharacter ):
                  words = words + currentcharacter
                  DFAstate = 20

               elif( 'n' == currentcharacter ):
                  words = words +currentcharacter
                  DFAstate = 21

               elif( 'o' == currentcharacter ):
                  words = words +currentcharacter
                  DFAstate = 22

               elif( 'p' == currentcharacter ):
                  words = words +currentcharacter
                  DFAstate = 23

               elif( 's' == currentcharacter ):
                  words = words +currentcharacter
                  DFAstate = 24

               elif( 't' == currentcharacter ):
                  words = words + currentcharacter
                  DFAstate = 25

               elif( 'w' == currentcharacter ):
                  words = words +currentcharacter
                  DFAstate = 26

               elif( re.match( '[b-dgj-lqruvx-z]', currentcharacter )) :
                  words = words +currentcharacter
                  DFAstate = 27

                  #flaged all first test cases. The final lese covers anything that falls outside of them
                  #i.e. characters not part of alphabet. eg '$', '%', '^', '@', '[A-Z]'

               else:
                  words = words +currentcharacter
                  e=Error("Token is not part of alphabet.", currentcharacter, outerLoopCounter, innerLoopCounter)
                  #tokensArray.append(e)
                  print([e])
                  exit(0)

            #Below are all the other states that are available. Look at DFA diagram for more understanding
            elif( DFAstate == 2):
               if( "\"" == currentcharacter ):
                  words = words + currentcharacter
                  DFAstate = 46

               elif( re.match( "[a-z0-9]", currentcharacter ) and length < 8 ):
                     words= words + currentcharacter
                     length += 1
                     DFAstate = 2
               else:
                  if( re.match( "[a-z0-9]", currentcharacter )):
                     words = words + currentcharacter
                     e = Error("String contains too many characters.", currentcharacter, outerLoopCounter, innerLoopCounter)
                     print([e])+'The string is: '+length+'characters long'
                     exit(0)

            elif( DFAstate == 3 ):
               tokensArray.append( ["Token number: " + str(amount), "TYPE: SYMBOL", words])
               flag = True
               DFAstate = 1
               amount += 1
               words = ""
              
            elif( DFAstate == 4 ):
               tokensArray.append( ["Token number: " + str(amount), " TYPE: SYMBOL", words] )
               flag = True
               DFAstate = 1 
               amount += 1
               words = ""
               
            elif( DFAstate == 5 ):
               tokensArray.append( ["Token number: " + str(amount), "TYPE: SYMBOL", words] )
               flag = True
               DFAstate = 1 
               amount += 1
               words = ""
              
            elif( DFAstate == 6 ):
               tokensArray.append( ["Token number: " + str(amount), "TYPE: SYMBOL", words] )
               flag = True
               DFAstate = 1
               amount += 1
               words = ""

            elif( DFAstate == 7 ):
               tokensArray.append( ["Token number: " + str(amount), "TYPE: SYMBOL", words] )
               flag = True
               DFAstate = 1
               amount += 1
               words = ""
               
            elif( DFAstate == 8):
               if( re.match( "[a-z0-9]", currentcharacter )):
                  words = words + currentcharacter
                  DFAstate = 27

               else:
                  tokensArray.append( ["Token number: " + str(amount), "TYPE: KEYWORD", words] )
                  flag = True
                  DFAstate = 1
                  amount += 1
                  words = ""

            elif( DFAstate == 9 ):
               if( re.match( "d", currentcharacter )):
                  words = words + currentcharacter
                  DFAstate = 8

               elif( re.match( "[a-ce-z0-9]", currentcharacter ) ):
                  words = words + currentcharacter
                  DFAstate = 27

               else:
                  tokensArray.append( ["Token number:  " + str(amount), "TYPE: ID", words] )
                  flag = True
                  DFAstate = 1
                  amount += 1
                  words = ""

            elif( DFAstate == 10 ):
               tokensArray.append( ["Token number:  " + str(amount), "TYPE: SYMBOL", words] )
               flag = True
               DFAstate = 1
               amount += 1
               words = ""

            elif( DFAstate == 11 ):
               tokensArray.append( ["Token number: " + str(amount), "TYPE: SYMBOL", words] )
               flag = True
               DFAstate = 1
               amount += 1
               words = ""

            elif( DFAstate == 12):
               if( re.match( "[0-9]", currentcharacter ) ):
                  words = words + currentcharacter
                  e=Error('Number is undefined', words, outerLoopCounter, innerLoopCounter )
                  print([e])
                  exit(0)

               else:
                  tokensArray.append( ["Token number: " + str(amount), "TYPE: NUMBER", words] )
                  flag = True
                  DFAstate = 1
                  amount += 1
                  words = ""
                  
            elif( DFAstate == 13):
               if( re.match( "[1-9]", currentcharacter ) ):
                  words = words + currentcharacter
                  DFAstate = 14

               else:
                  words = words + currentcharacter
                  e=Error('Number is undefined', words, outerLoopCounter, innerLoopCounter )
                  print([e])
                  exit(0)

            elif( DFAstate == 14 ):
               if re.match( "[0-9]", currentcharacter ):
                  words = words + currentcharacter
                  DFAstate = 14

               else:
                  tokensArray.append(["Token number: " + str(amount), "TYPE: NUMBER", words] )
                  flag = True
                  DFAstate = 1
                  amount += 1
                  words = ""
                 
            elif( DFAstate == 15 ):
               if( "n" == currentcharacter ):
                  words = words + currentcharacter
                  DFAstate = 32

               elif( "d" == currentcharacter ):
                  words = words + currentcharacter
                  DFAstate = 9

               elif re.match( "[a-ce-mo-z0-9]", currentcharacter ):
                  words = words + currentcharacter
                  DFAstate = 27

               else:
                  tokensArray.append( ["Token number: " + str(amount), "TYPE: ID", words] )
                  flag = True
                  DFAstate = 1
                  amount += 1
                  words = ""

            elif( DFAstate == 16 ):
               if( "l" == currentcharacter ):
                  words = words + currentcharacter
                  DFAstate = 30

               elif( "q" == currentcharacter ):
                  words = words + currentcharacter
                  DFAstate = 31

               elif re.match( "[a-km-pr-z0-9]", currentcharacter ):
                  words = words + currentcharacter
                  DFAstate = 27

               else:
                  tokensArray.append( ["Token number:" + str(amount), "TYPE: ID", words] )
                  flag = True
                  DFAstate = 1
                  amount += 1
                  words = ""
                
            elif( DFAstate == 17 ):
               if( "o" == currentcharacter ):
                  words = words + currentcharacter
                  DFAstate = 43

               elif re.match( "[a-np-z0-9]", currentcharacter ):
                  words = words + currentcharacter
                  DFAstate = 27

               else:
                  tokensArray.append( ["Token number: " + str(amount), "TYPE: ID", words] )
                  flag = True
                  DFAstate = 1
                  amount += 1
                  words = ""

            elif( DFAstate == 18 ):
               if( "a" == currentcharacter ):
                  words = words + currentcharacter
                  DFAstate = 44

               elif re.match( "[b-z0-9]", currentcharacter ):
                  words = words + currentcharacter
                  DFAstate = 27

               else:
                  tokensArray.append( ["Token number: " + str(amount), "TYPE: ID", words] )
                  flag = True
                  DFAstate = 1
                  amount += 1
                  words = ""

            elif( DFAstate == 19 ):
               if( "f" == currentcharacter ):
                  words = words + currentcharacter
                  DFAstate = 39

               elif( "n" == currentcharacter ):
                  words = words + currentcharacter
                  DFAstate = 40

               elif re.match( "[a-eg-mo-z0-9]", currentcharacter ):
                  words = words + currentcharacter
                  DFAstate = 27

               else:
                  tokensArray.append( ["Token number: " + str(amount), "TYPE: ID", words] )
                  flag = True
                  DFAstate = 1
                  amount += 1
                  words = ""

            elif( DFAstate == 20 ):
               if("u" == currentcharacter ):
                  words = words + currentcharacter
                  DFAstate = 37

               elif re.match( "[a-mo-z0-9]", currentcharacter ):
                  words = words + currentcharacter
                  DFAstate = 27

               else:
                  tokensArray.append( ["Token number: " + str(amount), "TYPE: ID", words] )
                  flag = True
                  DFAstate = 1
                  amount += 1
                  words = ""
                  
            elif( DFAstate == 21 ):
               if( "o" == currentcharacter ):
                  words = words + currentcharacter
                  DFAstate = 36

               elif re.match( "[a-np-z0-9]", currentcharacter ):
                  words = words + currentcharacter
                  DFAstate = 27

               else:
                  tokensArray.append( ["Token number: " + str(amount), "TYPE: ID", words] )
                  flag = True
                  DFAstate = 1
                  amount += 1
                  words = ""
                 
            elif( DFAstate == 22 ):
               if re.match( "r", currentcharacter ):
                  words = words + currentcharacter
                  DFAstate = 34

               elif( "u" == currentcharacter ):
                  words = words + currentcharacter
                  DFAstate = 35

               elif re.match( "[a-qstv-z0-9]", currentcharacter ):
                  words = words + currentcharacter
                  DFAstate = 27

               else:
                  tokensArray.append( ["Token number: " + str(amount), "TYPE: ID", words] )
                  flag = True
                  DFAstate = 1
                  amount += 1
                  words = ""

            elif( DFAstate == 23):
               if("r" == currentcharacter ):
                  words = words + currentcharacter
                  DFAstate = 38

               elif re.match( "[a-qs-z0-9]", currentcharacter ):
                  words = words + currentcharacter
                  DFAstate = 27

               else:
                  tokensArray.append( ["Token number: " + str(amount), "TYPE: ID", words] )
                  flag = True
                  DFAstate = 1
                  amount += 1
                  words = ""
                 
            elif( DFAstate == 24 ):
               if( "u" == currentcharacter ):
                  words = words + currentcharacter
                  DFAstate = 45

               elif re.match( "[a-tv-z0-9]", currentcharacter ):
                  words = words + currentcharacter
                  DFAstate = 27

               else:
                  tokensArray.append( ["Token number: " + str(amount), "TYPE: ID", words] )
                  flag = True
                  DFAstate = 1
                  amount += 1
                  words = "" 

            elif( DFAstate == 25 ):
               if( "h" == currentcharacter ):
                  words = words + currentcharacter
                  DFAstate = 41

               elif re.match( "[a-gi-z0-9]", currentcharacter ):
                  words = words + currentcharacter
                  DFAstate = 27

               else:
                  tokensArray.append(["Token number: " + str(amount), "TYPE: ID", words] )
                  flag = True
                  DFAstate = 1
                  amount += 1
                  words = ""
   
            elif( DFAstate == 26):
               if( "h" ==currentcharacter ):
                  words = words + currentcharacter
                  DFAstate = 42

               elif re.match( "[a-gi-z0-9]", currentcharacter ):
                  words = words + currentcharacter
                  DFAstate = 27

               else:
                  tokensArray.append( ["Token number: " + str(amount), "TYPE: ID", words] )
                  flag = True
                  DFAstate = 1
                  amount += 1
                  words = ""

            elif( DFAstate == 27):
               if re.match( "[a-z0-9]", currentcharacter):
                  words = words + currentcharacter

               else:
                  tokensArray.append( ["Token number: " + str(amount), "TYPE: ID", words] )
                  flag = True
                  DFAstate = 1
                  amount += 1
                  words = ""
                 
            elif( DFAstate == 28 ):
               tokensArray.append( ["Token number: " + str(amount), "TYPE: SYMBOL", words] )
               flag = True
               DFAstate = 1
               amount += 1
               words = ""

            elif( DFAstate == 29 ):
               tokensArray.append( ["Token number: " + str(amount), "TYPE: SYMBOL", words] )
               flag = True
               DFAstate = 1
               amount += 1
               words = ""

            elif( DFAstate == 30 ):
               if re.match( "s", currentcharacter ):
                  words = words + currentcharacter
                  DFAstate = 47

               elif re.match( "[a-rt-z0-9]", currentcharacter ):
                  words = words + currentcharacter
                  DFAstate = 27

               else:
                  tokensArray.append( ["Token number: " + str(amount), "TYPE: ID", words] )
                  flag = True
                  DFAstate = 1
                  amount += 1
                  words = ""

            elif( DFAstate == 31 ):
               if re.match( "[a-z0-9]", currentcharacter ):
                  words = words + currentcharacter
                  DFAstate = 27

               else:
                  tokensArray.append( ["Token number: " + str(amount), "TYPE: KEYWORD", words] )
                  flag = True
                  DFAstate = 1
                  amount += 1
                  words = ""

            elif( DFAstate == 32):
               if re.match( "d", currentcharacter ):
                  words = words + currentcharacter
                  DFAstate = 33

               elif re.match( "[a-ce-z0-9]", currentcharacter ):
                  words = words + currentcharacter
                  DFAstate = 27
                  
               else:
                  tokensArray.append( ["Tokens number: " + str(amount), "TYPE: ID", words] )
                  flag = True
                  DFAstate = 1
                  amount += 1
                  words = ""
                
            elif( DFAstate == 33 ):
               if re.match( "[a-z0-9]", currentcharacter):
                  words = words + currentcharacter
                  DFAstate = 27

               else:
                  tokensArray.append( ["Token number: " + str(amount), "TYPE: KEYWORD", words] )
                  flag = True
                  DFAstate = 1
                  amount += 1
                  words = ""
                  
            elif( DFAstate == 34 ):
               if re.match( "[a-z0-9]", currentcharacter):
                  words = words + currentcharacter
                  DFAstate = 27

               else:
                  tokensArray.append( ["Token number: " + str(amount), "TYPE: KEYWORD", words] )
                  flag = True
                  DFAstate = 1
                  amount += 1
                  words = ""

            elif( DFAstate == 35 ):
               if( "t" == currentcharacter ):
                  words = words + currentcharacter
                  DFAstate = 48

               elif(re.match( "[a-su-z0-9]", currentcharacter ) ):
                  words = words + currentcharacter
                  DFAstate = 27

               else:
                  tokensArray.append( ["Token number: " + str(amount), "TYPE: ID", words] )
                  flag = True
                  DFAstate = 1
                  amount += 1
                  words = ""
                 
            elif( DFAstate == 36 ):
               if( "t" == currentcharacter ):
                  words = words + currentcharacter
                  DFAstate = 53

               elif re.match( "[a-su-z-9]", currentcharacter ):
                  words = words + currentcharacter
                  DFAstate = 27
                  
               else:
                  tokensArray.append( ["Token number: " + str(amount), "TYPE: ID", words] )
                  flag = True
                  DFAstate = 1
                  amount += 1
                  words = ""
                  
            elif( DFAstate == 37 ):
               if( "l" == currentcharacter ):
                  words = words + currentcharacter
                  DFAstate = 54

               elif re.match( "[a-km-z0-9]", currentcharacter ):
                    words = words + currentcharacter
                    DFAstate = 27

               else:
                  tokensArray.append( ["Token number: " + str(amount), "TYPE: ID", words] )
                  flag = True
                  DFAstate = 1
                  amount += 1
                  words = ""
                
            elif( DFAstate == 38 ):
               if( "o" == currentcharacter ):
                  words = words + currentcharacter
                  DFAstate = 56

               elif(re.match( "[a-np-z0-9]", currentcharacter ) ):
                  words = words + currentcharacter
                  DFAstate = 27

               else:
                  tokensArray.append( ["Token number: " + str(amount), "TYPE: ID", words] )
                  flag = True
                  DFAstate = 1
                  amount += 1
                  words = ""
               
            elif( DFAstate == 39 ):
               if( re.match( "[a-z0-9]", currentcharacter )) :
                  words = words + currentcharacter
                  DFAstate = 27

               else:
                  tokensArray.append( ["Token number: " + str(amount), "TYPE: KEYWORD", words] )
                  flag = True
                  DFAstate = 1
                  amount += 1
                  words = ""
                
            elif( DFAstate == 40 ):
               if( "p" == currentcharacter ):
                  words = words + currentcharacter
                  DFAstate = 58

               elif( re.match( "[a-oq-z0-9]", currentcharacter ) ):
                  words = words + currentcharacter
                  DFAstate = 27

               else:
                  tokensArray.append( ["Token number: " + str(amount), "TYPE: ID", words] )
                  flag = True
                  DFAstate = 1
                  amount += 1
                  words = ""
               
            elif( DFAstate == 41 ):
               if( "e" == currentcharacter ):
                  words = words + currentcharacter
                  DFAstate = 61

               elif( re.match( "[a-df-z0-9]", currentcharacter )):
                  words = words + currentcharacter
                  DFAstate = 27

               else:
                  tokensArray.append( ["Token number: " + str(amount), "TYPE: ID", words] )
                  flag = True
                  DFAstate = 1
                  amount += 1
                  words = ""
                 
            elif( DFAstate == 42 ):
               if( "i" == currentcharacter ):
                  words = words + currentcharacter
                  DFAstate = 63

               elif( re.match("[a-hj-z0-9]", currentcharacter) ):
                  words = words + currentcharacter
                  DFAstate = 27

               else:
                  tokensArray.append( ["Token number: " + str(amount), "TYPE: ID", words] )
                  flag = True
                  DFAstate = 1
                  amount += 1
                  words = ""

            elif( DFAstate == 43 ):
               if( "r" == currentcharacter ):
                  words = words + currentcharacter
                  DFAstate = 66

               elif( re.match("[a-qs-z0-9]", currentcharacter) ):
                  words = words + currentcharacter
                  DFAstate = 27

               else:
                  tokensArray.append( ["Token number: " + str(amount), "TYPE: ID", words] )
                  flag = True
                  DFAstate = 1
                  amount += 1
                  words = ""
                 
            elif( DFAstate == 44 ):
               if( "l" == currentcharacter ):
                  words = words + currentcharacter
                  DFAstate = 67

               elif( re.match("[a-km-z0-9]", currentcharacter )):
                  words = words + currentcharacter 
                  DFAstate = 27

               else:
                  tokensArray.append(["Token number: " + str(amount), "TYPE: ID", words] )
                  flag = True
                  DFAstate = 1
                  amount += 1
                  words = ""
                 
            elif( DFAstate == 45 ):
               if( "l" == currentcharacter ):
                  words = words + currentcharacter
                  DFAstate = 69

               elif( re.match( "[ac-z0-9]", currentcharacter )):
                  words = words + currentcharacter
                  DFAstate = 27

               else:
                  tokensArray.append( ["Token number: " + str(amount), "TYPE: ID", words] )
                  flag = True
                  DFAstate = 1
                  amount += 1
                  words = ""
                 
            elif( DFAstate == 46):
               length = 0
               tokensArray.append(["Token number: " + str(amount), "TYPE: STRING", words] )
               flag = True
               DFAstate = 1
               amount += 1
               words = ""
               
            elif( DFAstate == 47 ):
               if( "e" == currentcharacter ):
                  amount = amount + currentcharacter
                  DFAstate = 52

               elif( re.match("[a-df-z0-9]", currentcharacter )):
                  amount = amount + currentcharacter
                  DFAstate = 27

               else:
                  tokensArray.append( ["Token number: " + str(amount), "TYPE: ID", words] )
                  flag = True
                  DFAstate = 1
                  amount += 1
                  words = ""
                 

            elif( DFAstate == 48):
               if( "p" == currentcharacter ):
                  words = words + currentcharacter
                  DFAstate = 49

               elif( e.match("[a-oq-z0-9]", currentcharacter) ):
                  words = words + currentcharacter
                  DFAstate = 27

               else:
                  tokensArray.append( ["Token number: " + str(amount), "TYPE: ID", words] )
                  flag = True
                  DFAstate = 1
                  amount += 1
                  words = ""
                
            elif( DFAstate == 49):
               if( "u" == currentcharacter ):
                  words = words + currentcharacter
                  DFAstate = 50

               elif( re.match("[a-tv-z0-9]", currentcharacter )):
                  words = words + currentcharacter
                  DFAstate = 27

               else:
                  tokensArray.append(["Token number: " + str(amount), "TYPE: ID", words] )
                  flag = True
                  DFAstate = 1
                  amount += 1
                  words = ""

            elif( DFAstate == 50 ):
               if( "t" == currentcharacter ):
                  words = words + currentcharacter
                  DFAstate = 51
                  
               elif( re.match("[a-su-z0-9]", currentcharacter )):
                  words = words + currentcharacter
                  DFAstate = 27

               else:
                  tokensArray.append( ["Token number: " + str(amount), "TYPE: ID", words] )
                  flag = True
                  DFAstate = 1
                  amount += 1
                  words = ""
               
            elif( DFAstate == 51):
               if( re.match( "[a-z0-9]", currentcharacter )):
                  words = words + currentcharacter
                  DFAstate = 27

               else:
                  tokensArray.append( ["Token number: " + str(amount), "TYPE: KEYWORD", words] )
                  flag = True
                  DFAstate = 1
                  amount += 1
                  words = ""

            elif( DFAstate == 52 ):
               if( re.match( "[a-z0-9]", currentcharacter )):
                  words = words + currentcharacter
                  DFAstate = 27

               else:
                  tokensArray.append( ["Token number: " + str(amount), "TYPE: KEYWORD", words] )
                  flag = True
                  DFAstate = 1
                  amount += 1
                  words = ""

            elif( DFAstate == 53 ):
               if( re.match("[a-z0-9]", currentcharacter) ):
                  words = words + currentcharacter
                  DFAstate = 27

               else:
                  tokensArray.append(["Token number: " + str(amount), "TYPE: KEYWORD", words] )
                  flag = True
                  DFAstate = 1
                  amount += 1
                  words = ""

            elif( DFAstate == 54):
               if( "t" == currentcharacter ):
                  words = words + currentcharacter
                  DFAstate = 55

               elif( re.match("[a-su-z0-9]", currentcharacter ) ):
                  words = words + currentcharacter
                  DFAstate = 27

               else:
                  tokensArray.append(["Token number: " + str(amount), "TYPE: ID", words] )
                  flag = True
                  DFAstate = 1
                  amount += 1
                  words = ""

            elif( DFAstate == 55 ):
               if( re.match("[a-z0-9]", currentcharacter )):
                  words = words + currentcharacter
                  DFAstate = 27

               else:
                  tokensArray.append( ["Token number: " + str(amount), "TYPE: KEYWORD", words] )
                  flag = True
                  DFAstate = 1
                  amount += 1
                  words = ""
                
            elif( DFAstate == 56 ):
               if re.match("c", currentcharacter):
                  words = words + currentcharacter 
                  DFAstate = 57

               elif( re.match("[a-su-z0-9]", currentcharacter ) ):
                  words = words + currentcharacter
                  DFAstate = 27
                  
               else:
                  tokensArray.append(["Token number: " + str(amount), "TYPE: ID", words] )
                  flag = True
                  DFAstate = 1
                  amount += 1
                  words = ""
               
            elif( DFAstate == 57 ):
               if( re.match("[a-z0-9]", currentcharacter )) :
                  words = words + currentcharacter
                  DFAstate = 27

               else:
                  tokensArray.append(["Token number: " + str(amount), "TYPE: KEYWORD", words ] )
                  flag = True
                  DFAstate = 1
                  amount += 1
                  words = ""
                 
            elif( DFAstate == 58 ):
               if( "u" == currentcharacter ):
                  words = words + currentcharacter
                  DFAstate = 59

               elif re.match("[a-tv-z0-9]", currentcharacter ):
                  words = words + currentcharacter
                  DFAstate = 27

               else:
                  tokensArray.append( ["Token number: " + str(amount), "TYPE: ID", words] )
                  flag = True
                  DFAstate = 1
                  amount += 1
                  words = ""

            elif( DFAstate == 59):
               if( "t" == currentcharacter ):
                  words = words + currentcharacter
                  DFAstate = 60

               elif( re.match("[a-su-z0-9]", currentcharacter )):
                  words = words + currentcharacter
                  DFAstate = 27

               else:
                  tokensArray.append(["Token number:  " + str(amount), "TYPE: ID", words] )
                  flag = True
                  DFAstate = 1
                  amount += 1
                  words = ""

            elif( DFAstate == 60 ):
               if( re.match("[a-z0-9]", currentcharacter) ):
                  words = words + currentcharacter
                  DFAstate = 27

               else:
                  tokensArray.append(["Token number: " + str(amount), "TYPE: KEYWORD", words] )
                  flag = True
                  DFAstate = 1
                  amount += 1
                  words = ""

            elif( DFAstate == 61 ):
               if( "n" == currentcharacter ) :
                  words = words + currentcharacter
                  DFAstate = 62

               elif( re.match("[a-mo-z0-9]", currentcharacter )) :
                  words = words + currentcharacter
                  DFAstate = 27

               else:
                  tokensArray.append( ["Token number:  " + str(amount), "TYPE: ID", words] )
                  flag = True
                  DFAstate = 1
                  amount += 1
                  words = ""

            elif( DFAstate == 62):
               if( re.match("[a-z0-9]", currentcharacter )):
                  words = words + currentcharacter
                  DFAstate = 27

               else:
                  tokensArray.append(["Token number: " + str(amount), "TYPE: KEYWORD", words] )
                  flag = True
                  DFAstate = 1
                  amount += 1
                  words = ""
               
            elif( DFAstate == 63 ):
               if( "l" == currentcharacter ):
                  words = words + currentcharacter
                  DFAstate = 64

               elif( re.match("[a-km-z0-9]", currentcharacter )):
                  words = words + currentcharacter
                  DFAstate = 27

               else:
                  tokensArray.append( ["Token number: " + str(amount), "TYPE: ID", words] )
                  flag = True
                  DFAstate = 1
                  amount += 1
                  words = ""
               
            elif( DFAstate == 64 ):
               if( "e" == currentcharacter ):
                  words = words + currentcharacter
                  DFAstate = 65

               elif( re.match("[a-df-z0-9]", currentcharacter )):
                  words = words + currentcharacter
                  DFAstate = 27

               else:
                  tokensArray.append(["Token number: " + str(amount), " TYPE: ID", words] )
                  flag = True
                  DFAstate = 1
                  amount += 1
                  words = ""

            elif( DFAstate == 65 ):
               if( re.match("[a-z0-9]", currentcharacter) ):
                  words = words + currentcharacter
                  DFAstate = 27

               else:
                  tokensArray.append(["Token number: " + str(amount), "TYPE: KEYWORD", words ])
                  flag = True
                  DFAstate = 1
                  amount += 1
                  words= ""
                
            elif( DFAstate == 66):
               if( re.match("[a-z0-9]", currentcharacter )):
                  words = words + currentcharacter
                  DFAstate = 27

               else:
                  tokensArray.append(["Token number: " + str(amount), "TYPE: KEYWORD", words] )
                  flag = True
                  DFAstate = 1
                  amount += 1
                  words = ""
                 
            elif( DFAstate == 67):
               if( "t" == currentcharacter ):
                  words = words + currentcharacter
                  DFAstate = 68

               elif( re.match("[a-su-z0-9]", currentcharacter) ):
                  words = words + currentcharacter
                  DFAstate = 27

               else:
                  tokensArray.append( ["Token number: " + str(amount), "TYPE: ID", words] )
                  flag = True
                  DFAstate = 1
                  amount += 1
                  words = ""
                 
            elif( DFAstate == 68 ):
               if( re.match("[a-z0-9]", currentcharacter ) ):
                  words = words + currentcharacter
                  DFAstate = 27

               else:
                  tokensArray.append(["Token number: " + str(amount), "TYPE: KEYWORD", words])
                  flag = True
                  DFAstate = 1
                  amount += 1
                  words = ""
                  
            elif( DFAstate == 69 ):
               if( re.match("[a-z0-9]", currentcharacter ) ):
                  words = words + currentcharacter
                  DFAstate = 27

               else:
                  tokensArray.append(["Token number: " + str(amount), "TYPE: KEYWORD", words ])
                  flag = True
                  DFAstate = 1
                  amount += 1
                  words = ""

   #Sort the tokens into different catagories and push into the array


   if( DFAstate != 13 and DFAstate != 1 ):
      #Holds all the symbol tokens
      if( DFAstate in [3, 4, 5, 6, 7, 10, 11, 28, 29] ):
         tokensArray.append( ["Token number: " + str(amount), "TYPE: SYMBOL", words ] )

      #Holds all the Keyword tokens
      elif( DFAstate in [8, 31, 33, 34, 39, 51, 52, 53, 55, 57, 60, 62, 65, 66, 68, 69] ):
         tokensArray.append( ["Token number: " + str(amount), "TYPE: KEYWORD", words] )

      #Holds all the number tokens
      elif( DFAstate in [12, 14] ):
         tokensArray.append([ "Token number: " + str(amount), "TYPE: NUMBER", words] )

      #Holds all the short-string tokens
      elif( DFAstate in [46] ):
         tokensArray.append( ["Token number: " + str(amount), "TYPE: STRING", words] )

      #Holds the errors
      elif( DFAstate in [2] ):
         e = Error("Lexical error", words, outerLoopCounter, innerLoopCounter)
         print([e])
         exit(0)

      #Holds all the ID tokens(Variable Names)
      else:
         tokensArray.append(["Token number: " + str(amount), "TYPE: ID", words])

      amount += 1
      #close the file
      inputFile.close()

   #return the array
   return tokensArray

#This indicates what the main driver function is called so the compiler knows what function to run. 
if __name__ == "__main__":
   mainFunction()