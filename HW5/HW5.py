#Elias Caceres
#cacer019
#section 002
#CSCI 1133
#Homework 5

#=================================================================
# Name: cnt_occur(X, Y)
#
# Purpose: The purpose of this function is to count the number
#          of times a certain elements appears in a list, even
#          if it's embedded in inner lists too.
#
# Precondition: For this function, it is expected that the values
#               being entered in the list be either strings or ints
#               and that the element being called is also as well.
#               No complex objects such as lists or tuples.
#
# Input Parameters: The X input will be the list of ints and strings
#                   the list can also have embedded lists.
#                   The Y input will be the element we're counting
#                   in the list put in for x.
#
# Return Value: The return value of this function will be the number
#               of time the Y input is found in the list entered for
#               X. If there's no values in the list for X, the function
#               will return 0.
#=================================================================

def cnt_occur(x, y):

    if x == []:
        return 0

    elif isinstance(x[0], list):
        return cnt_occur(x[0], y) + cnt_occur(x[1:], y)


    elif x[0] != y:
        return cnt_occur(x[1:], y)


    elif x[0] == y:
        return 1 + cnt_occur(x[1:], y)

#=================================================================
# Name: position_helper(x, y, count, l)
#
# Purpose: The purpose of this function is to be a helper to problem
#          2. This helper function does the main work while adding a
#          counter and new list to return position(x, y). 
#
# Precondition: There are no preconditions for this helper funtion
#               as it's expected to only be called when position(x, y)
#               is used.
#
# Input Parameters: The x input will be the x input that's passed
#                   through for position(x, y). Input y will also
#                   be the y input of position(x, y). Count can be any
#                   integer you would want the count to be and l is
#                   expected to be an empty list.
#
# Return Value: This function will return the indexes of y in a list of
#               x. This function will be called by position(x, y) for it
#               and the indexes will return on it's behalf.
#=================================================================

def position_helper(x, y, count, l):

    if x == []:

        return []

    elif x[0] == y and len(x) == 1:

        l.append(x.index(x[0]) + count)

        return l

    elif x[0] == y and len(x) != 1:

        l.append(x.index(x[0]) + count)

        return position_helper(x[1:], y, count + 1, l)

    elif x[0] != y and len(x) == 1:

        return l

    elif x[0] != y and len(x) != 1:

        return position_helper(x[1:], y, count + 1, l)

#=================================================================
# Name: position(x, y)
#
# Purpose: The purpose of this function is to return the index positions
#          of the input y value in a list from a given list in the x
#          input.
#
# Precondition: The inputted value for x should be a list (doesn't need
#               to have the value of y in it for it to work).
#
# Input Parameters: The x input for this function will be a list of
#                   numbers.
#
#                   The y input for this function will be an int, that's
#                   index will be looked up and curate a list of them.
#
# Return Value: This function will return a list of the indexes where y
#               is found in the x list. If the y value isn't in the x list
#               the function will return an empty list.
#=================================================================

def position(x, y):

    return position_helper(x, y, 0, [])

#=================================================================
# Name: dups_helper(x, l)
#
# Purpose: The purpose of this function is to create and return a
#          list that has the order of a given list with only one of
#          it's value given a single repetative sequence. This function
#          is a helper function to rm_conseq_dups(x), that allows a new
#          list to pass through for the returned list.
#
# Precondition: The list enetered for x will have no embedded lists.
#               The list will only have ints or strings.
#
# Input Parameters: The x input of this function will be the x input for
#                   rm_conseq_dups(x). The l function will be defaulted to
#                   an empty list when called by rm_conseq_dups(x).
#
# Return Value: The return value for this function will be the list (l) of single
#               instances of a value that are not followed again by the same
#               value. This function will return to rm_conseq_dups(x).
#=================================================================

def dups_helper(x, l):

     if x == []:

         return []

     elif len(x) != 1 and x[0] == x[1]:

         return dups_helper(x[1:], l)

     elif len(x) == 1 and x[0] ==  l[-1]:
         l.append(x[0])
         return l

     elif len(x) != 1 and x[0] != x[1]:
         l.append(x[0])
         return dups_helper(x[1:], l)

     elif len(x) == 1 and x[0] != l[-1]:
         l.append(x[0])
         return l

#=================================================================
# Name: rm_conseq_dups(x)
#
# Purpose: The purpose of this function is to create and return a
#          list that has the order of a given list with only one of
#          it's value given a single repetative sequence. This function
#          will call the helper function,dups_helper(x, l), to have that
#          return the created list on it's behalf.
#
# Precondition: The list enetered for x will have no embedded lists.
#               The list will only have ints or strings.
#
# Input Parameters: The x input of this function will be a list of ints
#                   and/or strings.
#
# Return Value: The return value for this function will be the list (l) of single
#               instances of a value that are not followed again by the same
#               value. This function will be called from dups_helper(x, l) and
#               be returned by rm_conseq_dups(x).
#=================================================================

def rm_conseq_dups(x):
    
    return dups_helper(x, [])

#=================================================================
# Name: sequence_helper(x, newsum, sequence)
#
# Purpose: This function models the sequence = {3, 6, 12, 24, 48, 96, ...}
#          to the nth number of whatever x is. And will return the number of
#          the sequence that x is in. This is a helper function to sequence(x).

# Precondition: x will always be an int.
#
#               newsum will start at 3
#
# Input Parameters: The x input of this function will whatever x is entered for
#                   sequence(x)
#
#                   newsum is used to add the upcoming number in the sequence.
#
#                   sequence is the list returned by the function. Is intended to be []
#                   in the beginning. 
#
# Return Value: The return value for this function will be the list (sequence). It
#               will be returned to the function sequence(x), for it to return it
#               on it's behalf. 
#=================================================================

def sequence_helper(x, newsum, sequence):

    if sequence == []:

        sequence.append(newsum)

        return sequence_helper(x, newsum, sequence)

    elif len(sequence) < x:

        newsum = newsum * 2

        sequence.append(newsum)

        return sequence_helper(x, newsum, sequence)

    elif len(sequence) == x:

        sequence.append(newsum * 2)

        return sequence[x-1]

#=================================================================
# Name: sequence(x)
#
# Purpose: This function models the sequence = {3, 6, 12, 24, 48, 96, ...}
#          to the nth number of whatever x is. And will return the number of
#          the sequence that x is in. This is a helper function to sequence(x).
#
# Precondition: x will always be an int.
#
# Input Parameters: The x input of this function will be whatever nth of the
#                   entered x is wanted to be returned from the sequence.
#
# Return Value: The return value for this function will be the xth number
#               in the sequence. 
#=================================================================

def sequence(x):

    return sequence_helper(x, 3, [])

#=================================================================
# Name: rangeIt_helper(x, y, range)
#
# Purpose: This function returns a list of integers ranging between
#          x and y. This is a helper function to rangeIt(x, y). 
#
# Precondition: x and y will always be ints. 
#
# Input Parameters: The x input of this function will be whatever x is for
#                   rangeIt(x, y).
#
#                   The y input of this function will be whatever y is for
#                   rangeIt(x, y).
#
#                   range will be an empty list for the returning list in
#                   rangeIt(x, y). 
#
# Return Value: The return value for this function will be the list of
#               numbers between x and y. It will return range. 
#=================================================================

def rangeIt_helper(x, y, range):

    if range == []:

        range.append(x)

        return rangeIt_helper(x + 1, y, range)

    elif range[-1] != y:

        range.append(x)

        return rangeIt_helper(x + 1, y, range)

    elif range[-1] == y:

        return range

#=================================================================
# Name: rangeIt(x, y)
#
# Purpose: This function returns a list of integers ranging between
#          x and y. It will do it by calling the function rangeIt_helper(x, y, range).
#
# Precondition: x and y will always be ints.
#               The first number will always be less than or = to the second number.
#
# Input Parameters: The x input of this function will be whatever the user wants
#                   the ranged list to start on. 
#
#                   The y input of this function will be whatever the user wants
#                   the ranged list to end at.
#
# Return Value: The return value for this function will be the list of
#               numbers between x and y.
#=================================================================

def rangeIt(x, y):

    return rangeIt_helper(x, y, [])
















