#Elias Caceres
#cacer019
#section 002
#CSCI 1133
#Homework 6

                            #Problem 1#
#=================================================================
# Name: sameKeys(diction1, diction2)
#
# Purpose: The purpose of this function is to return a dictionary
#          with the keys and same key values found in two inputted
#          dictionaries. Multiple key values will be put in a list
#
# Precondition: For this function, any value or element should keep
#               it's data structure intact.
#
# Input Parameters: The diction1 input will be one desired list to be
#                   copmared to diction2.
#
#                   diction2 is the second dictionary being compared.
#
# Return Value: The return value of this function will be the a new
#               dictionary with keys and key values found both in
#               diction1 and diction2. The key values will be in a list
#               and if there aren't any the function will return an
#               empty list.
#=================================================================

def sameKeys(diction1, diction2):

    dic_return = {}

    if diction1 == {} or diction2 == {}:

        return {}

    else:

        for x in diction1:

            if x in diction2:

                dic_return[x] = [diction1[x], diction2[x]]

    return dic_return

                            #Problem 2#
#=================================================================
# Name: averageGrades({scores})
#
# Purpose: The purpose of this function is to return a dictionary
#          with the keys represting students and their key values
#          representing their average test scores.
#
# Precondition: The preconditions for this function is that the key
#               values for the students test scores be ints.
#
# Input Parameters: The input for {scores} will be a dictionary
#                   with keys of students and a list of their test
#                   scores.
#
# Return Value: The return value of this function will be the a new
#               dictionary with keys representing the students and
#               their average scores. If the student wasn't given any
#               scores for their key value the average will return  0.
#=================================================================

def averageGrades(diction):

    average_return = {}

    if diction == {}:

        return {}

    else:

        for x in diction:

            if diction[x] == []:

                average_return[x] = 0

            else:

                average_return[x] = int(sum(diction[x])/len(diction[x]))

        return average_return

                            #Problem 3#
#=================================================================
# Name: allKeys(diction, element)
#
# Purpose: The purpose of this function is to return list with all the
#          keys found having the same keyvalue given for the element
#          input. 
#
# Precondition: Each keyvalue in the dictionary will either be an empty
#               list or list with integers. The keys of the dictionary
#               will be strings.
#
# Input Parameters: The input for diction will be the dictionary with
#                   strings for keys and lists for key values.
#
# Return Value: The return value of this function will be the a new
#               list with the string keys found having the same element
#               in their key value lists.
#=================================================================

def allKeys(diction, element):

    new_list = []

    for x in diction:

        holder = diction[x]

        if element in holder:

           new_list.append(x)

    return new_list

                            #Problem 4#
#=================================================================
# Name: invertFiles([“doc1.txt”, “doc2.txt”, “doc3.txt”, “doc4.txt”)
#
# Purpose: The purpose of this function is to take in a list of txt.
#          documents and write a new file with the unique intances of
#          the word and the no. document they're found on.
#
# Precondition: No user inputs are expected. Only list of txt. documents.
#
# Input Parameters: List of txt. documents
#
# Return Value: No return value, but a new txt doc, HW6_output.txt.
#=================================================================

def invertFiles(list_of_file_names):

    master_list = []

    import re

    count = 0

    for x in list_of_file_names:

        count = count + 1

        f = open(x, 'r')

        text = f.readlines()

        string = ''.join(text)

        string = string.lower()

        data = re.split("[ .,:;!?\s\b]+|[\r\n]+", string)

        for i in data:

            if i == '0' or i == '1' or i == '2' or i == '3' or i == '4' or i == '5' or i == '6' or i == '7' or i == '8'\
            or i == '9' or i == '0' or i == "":

                data.remove(i)

        for y in data:

            master_list.append("{0} {1} \r\n".format(y, count))

    unique_master_list = list(set(master_list))

    unique_master_list.sort()

    file = open('HW6_output.txt', 'w')

    for z in unique_master_list:

        file.write("{}".format(z))

    file.close()
