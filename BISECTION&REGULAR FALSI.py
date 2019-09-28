
import time
import math

print("\t\t\t\tWELCOME\nThis is a program that will help you in finding the roots of an equation(in Numerical Analysis) either by:")
print("Bisection Method or False Position Method (Regular Falsi).")
print("INSTRUCTIONS: For now, if for instance, you have an equation of the form x^2 + 3x - 13, please write it as: x,2 + 3*x - 13.")
print("And also make sure you use 'x' as your varaible; no other variable can be used for now.")
print("\t   Thanks for your Cooperation, this will help us serve you better")
#Storage Lists for
leq=[]  #the last list that will hold the user entered equation after sorting it out ...leq >>> lastEquation
nlt=[]  #nlt >>> newList
tp=[]   #tp >>> some kind of random variable name

eq=" "  #to in bringing out terms in the equation list    eq >>> equation

n=[]  #suppose to be for number of iterations 
aa=[]  #values of 'a'
bb=[]  #values of 'b'
xx=[]  #values of 'x'
FoX=[]  #Stores the values of f(x)
flag = 0 #To control error when selecting range (a & b)
flag1 = 0
brk = False
true = False

while(True): #While loop to enable us use the break statement
    re=input("Now let's begin...\n\nEnter your equation: ")  #Accepting user equation input c,2 + 3*c - 5      From here...
    
    #Testing whether the user entered nothing or just white space, sending error message and terminating the program
    if(re=="" or re==" "):  
        print("Oops...\  No input was received from you, you have to enter an equation before we continue!")
        re=input("\nEnter your equation: ")
        if(re=="" or re==" "):
            print("Program ended! You refused to enter an equation.")
            break
    #Testing if the user entered incomplete equation and terminate
    if len(re)<3:
        print("Incomplete equation")
        break
    
    for trials in range(2):
        method=input("Enter 1 to use BISECTION method or 2 to use REGULAR FALSI method: ")
        flag1+=1
        if method != "1" and method != "2" and flag1 != 2:
            print("Please Enter a correct option value[1 or 2]")
            method=input("1 for BISECTION method or 2 for REGULAR FALSI method: ")
        elif flag1 == 2 and method != "1" and method != "2":
            print("Sorry, you still didn't get it after ", flag1, " trials. We'll now use the default method(BISECTION METHOD)")
            method=1
            break
        else:
            break
    
    #Splitting the user input to sort them out
    re=re.split()
   #                                                                                             To here can be a defineed function: userInputAnalysis
  
    #WE're using ',' to detect power, so this is testing where there is power
    for i in range(len(re)):
        if "," in re[i]:
            nlt.append(re[i].split(","))
            tp.append(i)
    #Rearranging the equation by putting the powerr operator (**) in-place of ','       
    for j in range(len(nlt)):
        nlt[j].insert(1, "**")  # 0+1, "**"
        re.pop(tp[j])
        re.insert(tp[j], nlt[j])
        if "ex" in re:
            re.replace(re[j], "math.exp(x)")
    #Combinning the list elements in 're' into one
    for k in re:
        leq+=k
    #Taking out the elements in the list; i.e, removing the list operator '[]'
    for m in range(len(leq)):
        eq+=leq[m]
    #Definning a function that will convert the string above into a statement
    stop=False
    def equation(x):
        try:
            eqt=eval(eq)
            return eqt
        except(TypeError, SyntaxError):
            print("Sorry, you entered a wrong equation; please check your equation and enter the right input.")
            stop=True
    if(stop):
        break
        '''finally:
            print("ERROR 313...\n")
            print("An error occured while processing; this may be due to:\n\t*Wrong user input\n\t*Unexpected character\nCheck your equation and try again.")
            print("Make sure you enter it correctly...") '''
    #Taking a response from the user as to whether it has values for the variables needed ('a' and 'b')     
    response=input("Do you have a given range of values for a and b?[YES/NO]\nYour response here: ")
    response=response.upper()

    if(response=="YES"):  #user response_1
        rawRange=input("Please enter the range separated with comma: ")  #Accepting the range of values of values from the user as string
        if(rawRange=="" or rawRange==" "):
            rawRange.split(",")
            print("You did not enter the range.")
            break
        elif(len(rawRange)<2):
            print("Please enter a complete range of numbers...")
        
        #The below statements will fetch the first two values inputed, assign  the first one to 'a' and the second one to 'b'.
        elif(len(rawRange)>2):
            for l in range(len(rawRange)):
                if(rawRange[l]!=" " and rawRange[l]!=","):
                    a=int(rawRange[l])
                    break
            for k in range(len(rawRange)):
                if(rawRange[k+1]!=" " and rawRange[k+1]!="," and rawRange[k+1]!=a):
                    b=int(rawRange[k+1])
                    break
            print("Alrigth, we have taken note of your input and will use it to solve your problem.")
            print("From your input, we're setting:\na = ",a," and b = ",b)
            iterations = input("Do you have a specific number of iterations to carry out or terminate automatically?\
\nIf yes, enter the number of iterations, otherwise, press Enter: ")
        
            if(iterations.isnumeric()):
                n = int(iterations)
                true=True
                
    elif(response=="NO"):
        print("Alrigth, we will pick a range of values for you.\nA Second...\n")
        time.sleep(0)
        #STEP 1
        #Choosing a value for 'a' and 'b'.
        
        for r in range(1, 11):
            for s in range(1, 10):
                one=equation(r)
                two=equation(s)
                try:
                    mul=one*two
                except(TypeError):
                    print("Unexpected string value encountered, check your equation.")
                    brk=True
                    break
                if(mul < 0):
                    a=r
                    b=s
                    brk=True
                    
                    print("We have successively chosen a range of values for you, and we're setting \na = ",a, "and b =",b)
                    print("Since, f(",a,") = ", equation(a), " and f(",b,") = ", equation(b))
                    iterations = input("Do you have a specific number of iterations to carry out or terminate automatically?\
\nIf yes, enter the number of iterations, otherwise, press Enter: ")
                    
                    if(iterations.isnumeric()):
                        n = int(iterations)
                        true=True
                    print("Processing...")
                    break
            
            if brk:
                break
            elif(r==10 and s==10):
                print("Ooops... We couldn't pick the values due to an error")
                print("REASON:\n\tMay be the equation You entered does not exist; please check and try again!")
                flag = 1
                break
        if flag:
            break
    
    #Testing whether the user entered nothing or just white space as its response       
    elif(response=="" or response==" "):  #user response_2
        print("Sorry, we didn't get a response from you. Type in either \"yes\" or \"no\".")
        response=input(">>> ")
        break
    #Testing if the user entered an unrecognized input
    else:
        print("You entered the wrong input, Please give the right response; enter either yes or no.")
        break
    '''if(brk):  #this is actually an error that I struggled with for some days before i was able ti catch
        break
                '''
    #STEP 2
    #A function defined to determine the value of 'x'
    if method == "1":
        def step_2():
            x=(a+b)/2
            return x
    elif method == "2":
        def step_2():
            x = (a*equation(b) - b*equation(a)) / (equation(b) - equation(a))
            return x
    
    #Saving the first values of 'a', 'b' and f(x) in a list for the later use
    aa.append(a)
    bb.append(b)
    FoX.append(equation(step_2()))
    
    #Solving for the values of f(a), f(x) and testing whether their product is less or greater than zero; to assign f(x) to either a or b
    #Saving the successive values of 'a', 'b' and f(x)
    length = 0
    while(True):
        f_a=equation(a)
        f_x=equation(step_2())
        if(f_a*f_x < 0):
            xx.append(step_2())
            b=step_2()
            aa.append(a)
            bb.append(b)
            FoX.append(equation(step_2()))
            length+=1
        elif(f_a*f_x > 0):
            xx.append(step_2())
            a=step_2()
            aa.append(a)
            bb.append(b)
            FoX.append(equation(step_2()))
            length+=1
        elif(f_a*f_x == 0):
            print("The root of the given equation is: ", step_2())
            break
        if(true):            
            if(length == n):
                result=input("Press Enter to continue")                
                break
            else:
                continue
            
        elif(iterations == ""):         #if no specific number of iterations            
            if(length > 6):             #checking weather the condition is met to terminate iterations at least after 6 iterations
                if(abs(xx[length-1]) <= abs(xx[length-2]) and abs(xx[length-2]) <= abs(xx[length-3]) and abs(xx[length-3]) <= abs(xx[length-4])):
                    print("\t\t\tIteration Successful! \nA total of ", length," iterations has been carried out and the result is ready to be displayed!")
                    result=input("Press Enter to continue") #Prompting the user to determine whether to proceed in printing out the tabulated results or not
                    break
        
    
    #Printing the results if the user press Enter
    line = ("_____" * 20)
    if result=="":
        print("\n\n\t\t\t\tTABLE OF ITERATIONS\n" + line)
        print("n|     \ta\t\t\tb\t\t\tx\t\t\tf(x)") 
        print(line)
        for h in range(len(aa)-1):      #prining out the result of te iterations
            print(h+1,"|\t ", str(format(aa[h], '10f')).ljust(20, " "), str(format(bb[h], '10f')).ljust(25, " "), str(format(xx[h], '10f')).ljust(25, " "), str(format(FoX[h], '10f')).ljust(25, " "))
            print(line)
    
    break #Break statement to finally terminate the program after a successful execution; since we're using an infinite loop, to avoid continous execution
print("Press ENTER to EXIT")

print("\n", "**" * 55, "\n\n\n")
print("\n", "__" * 51)
print(" Powered By:".rjust(56, "*"), "**"*23, "\n \t \t \t\t\tEne-Une Reuben OCHEDI\n", "All Rigths Reserved.".rjust(60, " "), "\n", "(c)2018-2019".rjust(56, " "))
print("\n", "+-" * 51)
print("\tEmail: rubycodes14@gmail.com\t  LinkedIn: Ene-une Ochedi\t  GitHub: RubyCodes14\n\tFacebook: Ene-une Reuben Ochedi\t\t\tWhatsApp: +2348136020460")
print("\n", "==" * 51)


                                                        #THANK YOU JESUS
                                                        #THANK GOD FOR THIS GREAT IDEA
                                                        #IT'S NICE DOING THIS

input("")    
