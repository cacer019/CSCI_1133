#Elias Caceres 
#cacer019
#section 002
#Homework 4

#===============================================================================
# Name:  separate_int_and_str
# Purpose:  Given a list of integer and strings, create two new lists.  One
#   list will contain the integers and the other list will contain the 
#   strings.
#  Precondition:  The list will only contain ints and strings 
#  Input Parameter(s)
#           my_list:  a list containing integers and strings
#  Return Value(s)
#           -- if the input parameter is an emptylist , return a list 
#               with two empty lists:  [ [ ], [ ]]
#           -- else return a list with the 0th index position containing the
#               list of integers, and the 1st index position containing the
#               list of strings.  If there are no ints or strings, return
#               an empty listin that position
#===============================================================================

def separate_int_and_str(mylist):
    str_list = []
    int_list = []
    for x in mylist:
        if isinstance(x, int):
            int_list.append(x)
        else:
            str_list.append(x)
    result = [int_list, str_list]
    return result
    
#===============================================================================
# Name:  average_of_lists
#  Purpose: The purpose of this program is to average the list inputted into
#   this program function. 
#  Precondition:  The list will only contain numbers
#  Input Parameter(s) mylist: a list of lists with numbers or an empty list
#
#  Return Value(s) 
#               -- if the input parameter is an emptylist , return a list 
#               with two empty lists:  [ [ ] ]
#
#               -- if the input parameter is a list, with lists containing 
#                   numbers, return the average of lists: [[a1],[a2]]
#
#===============================================================================

def average_of_lists(mylist):
    result = []
    for x in mylist:
        if x != []:
            result.append(int(round((round(sum(x))/round(len(x))))))
        elif x == []:
            break
    return result
    
#===============================================================================
# Name:  min_of_lists
#  Purpose: The purpose of this program is to return the lowest value in a given
#       number of lists.
#  Precondition:  The lists will only contain numbers
#  Input Parameter(s)
#                   -- mylist: A lists of lists containing numbers or just an 
#                       empty list.
#
#  Return Value(s) if the parameter is a list of lists containing numbers:
#                       The function will return the overall lowest value in the lists.
#                   else: The function will return a 0 for an inputted empty list.
#===============================================================================

def min_of_lists(mylist):
    
    copy = mylist
    new_list = []
    length = len(mylist)
    count = 0
    
    if mylist == []:
        minimum = 0
        return(minimum)
    else:
        while count < length:
            for x in copy[count]:
                if x < copy[count][0]:
                    new_list.append(x)
            count = count + 1

            f = 1
            minimum = new_list[0]
            while f < len(new_list):
                if new_list[f] < minimum:
                    minimum = new_list[f]
                    f = f + 1
        return(minimum)



#===============================================================================   
# Name: greater_than
#   Purpose: The purpose of this program is to take in a list of numbers and a 
#    a seperate number value and compare the two to see if all values in the list
#     are greater than the second inputted value.
#
#   Precondition:  The lists will only contain numbers, or an empty list. 
#                   Second value will only be a positive or negative number. 
#
#   Input Parameter(s)
#               --mylist
#                   list of numbers
#               -- x
#                   second positive or negative number
#
#   Return Value(s)   
#               -- if all the numbers in the list are greater than x
#                   the output will be True. ([] will be handled as zero)
#               
#               -- if all the numbers in the list are less than x
#                   the output will be False. ([] will be handled as zero)
#===============================================================================

def greater_than(mylist,x):
    
    if mylist == [] and (x > 0):
        return True
    elif mylist == [] and (x < 0):
        return True
                
    elif mylist != []:
        num = x
        result = ()
        for i in mylist:
            if i > num:
                result = True
            elif i < num:
                result = False
                break
        return(result)

        
#===============================================================================
#   Name: selection_sort
#     Purpose: The purpose of this script is to take in a list of numbers and 
#       order them from least to greated, while keeping it in the inputted list.
#
#     Precondition: The list will only contain negative or positive numbers. 
#
#
#     Input Parameter(s)
#                       --mylist: list containing numbers
#
#     Return Value(s)
#                   -- the program will not return anything as it's just 
#                   manipulating the string inputted into it. If you are to call 
#                   the value, the list will appear to it. ex. A = [unordered list]
#                      function(A) makes A = [ordered list]
#
#
#===============================================================================
    
def selection_sort(mylist):
    
    count = 0
    length = len(mylist)
    while count < length:
        for x in range(length):
            minimum = x
            for left in range(x+1, length):
                if mylist[minimum] > mylist[left]:
                    minimum = left
                    mylist[x], mylist[minimum] = mylist[minimum], mylist[x]
            count = count + 1

#===============================================================================
# I just used this area below to test the programs
#def main():

        

#if __name__ == "__main__":
#   main()






