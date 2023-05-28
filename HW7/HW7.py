# Elias Caceres 
# cacer019
# section 02
# Homework 7

                            #Problem 1#
#=================================================================
# Name: class StopWatch
#
# Purpose: The purpose of this class is to create objects to keep
#          track of local time, start times, end times, and elapse
#          times. It can also be used to update these start and end
#          times as well as getting the values themselves.
#
# Precondition: For an object to be created with this class the x.StopWatch
#               instantiation the class objects doesn't need any inputs.
#
# Input Parameters: N/A
#
# Return Value: The return values depend on what class method is being
#               called, I'll go into what they do when I get to them.
#=================================================================

# I import the time module for the StopWatch class #

import time

class StopWatch:

    #=================================================================
    # Name: __init__
    #
    # Purpose: The purpose of this __init__ method is to be the constructor
    #          for the instantiated object and it's start and end times.
    #
    # Precondition: N/A
    #
    # Input Parameters: None, but a start and end time can be inputted in
    #                   the amount of seconds. (self will always be inputted)
    #
    # Return Value: N/A
    #=================================================================

    def __init__(self, start = time.time(), end = time.time()):

        self.start = start

        self.end = end

    #=================================================================
    # Name: get_start
    #
    # Purpose: The purpose of this method is to retrieve the start time
    #          in seconds from the object being called.
    #
    # Precondition: N/A
    #
    # Input Parameters: N/A (but self will always be inputted)
    #
    # Return Value: The starting time in seconds for the object being called
    #               with this method.
    #=================================================================

    def get_start(self):

        return self.start

    #=================================================================
    # Name: get_end
    #
    # Purpose: The purpose of this method is to retrieve the end time
    #          in seconds from the object being called.
    #
    # Precondition: N/A
    #
    # Input Parameters: N/A (but self will always be inputted)
    #
    # Return Value: This method will return the end time in seconds for
    #               whatever object is being called with get_end.
    #=================================================================

    def get_end(self):

        return self.end

    #=================================================================
    # Name: current_time
    #
    # Purpose: The purpose of this class method is to return the current
    #          time in HH:MM:SS format, military time.
    #
    # Precondition: N/A
    #
    # Input Parameter: N/A (but self will always be called)
    #
    # Return Value: This class method will return the current time in
    #               HH:MM:SS format, military time.
    #=================================================================

    def current_time(self):

        current = time.ctime()

        return current[11:19]

    #=================================================================
    # Name: set_start
    #
    # Purpose: The purpose of this class method is to let the user set
    #          the current time on the machine as the new start time of
    #          whatever object being called with this method.
    #
    # Precondition: N/A
    #
    # Input Parameters: N/A (but self will always be called)
    #
    # Return Value: N/A
    #=================================================================

    def set_start(self):

        self.start = time.time()

    #=================================================================
    # Name: set_end
    #
    # Purpose: The purpose of this class method is to let the user set
    #          the current time on the machine as the new end time of
    #          whatever object being called with this method.
    #
    # Precondition: N/A
    #
    # Input Parameters: N/A (but self will always be called)
    #
    # Return Value: N/A
    #=================================================================

    def set_end(self):

        self.end = time.time()

    #=================================================================
    # Name: elapsed_time
    #
    # Purpose: The purpose of this class method is to return the amount of
    #          time in seconds from the start time to the end time of the
    #          object being passed through for this method.
    #
    # Precondition: N/A
    #
    # Input Parameters: N/A (but self will always be called)
    #
    # Return Value: The time difference from end time & start time in
    #               seconds.
    #=================================================================

    def elapsed_time(self):

        y = (self.end) - (self.start)

        elapsed = time.ctime(y)

        return elapsed[14:19]

                            #Problem 2#
#=================================================================
# Name: class VideoGame
#
# Purpose: The purpose of this class is to create objects of video games
#          that tracks it's title name, ESRB ratings, reviews, and average review.
#
# Precondition: For an object to be created with this class the x.VideoGame
#               instantiation the user must provide a title name, and ESRB rating
#               ranging from [E, E10+, T, M, AO, RP]. Title and ESRB ratings must
#               be strings.
#
# Input Parameters: Title and ESRB ratings in string format.
#
# Return Value: The return values depend on what class method is being
#               called, I'll go into what they do when I get to them.
#=================================================================

class VideoGame:

    #=================================================================
    # Name: __init__
    #
    # Purpose: The purpose of this class method is to be the constructor
    #          for the instantiated object. The user sets the title and
    #          ESRB rating, with the list of ratings defaulting to [], and
    #          the average rating defaulting to 0.
    #
    # Precondition: N/A
    #
    # Input Parameters: (self), title and ESRB rating name in string format.
    #
    # Return Value: N/A
    #=================================================================

    def __init__(self, title, esrb, ratings = [], average_ratings = 0):

        self.title = title

        self.esrb = esrb

        if ratings == []:

            self.ratings = [0, 0, 0, 0, 0]

        else:

            self.ratings = ratings


        if sum(ratings) == 0:

            self.average_ratings = average_ratings


        else:
            
            # my way of algebraically finding the average rating #
            self.average_ratings = int(((self.ratings[0] * 1) + (self.ratings[1] * 2) + (self.ratings[2] * 3)\
            + (self.ratings[3] * 4) + (self.ratings[4] * 5))/(sum(self.ratings)))

    #=================================================================
    # Name: set_title
    #
    # Purpose: The purpose of this method is to let the user set and
    #          update the video game title of the object being called.
    #
    # Precondition: N/A
    #
    # Input Parameters: (self) & the updated title name in string format.
    #
    # Return Value: N/A
    #=================================================================
    
    def set_title(self, title):

        self.title = title

    #=================================================================
    # Name: set_esrb
    #
    # Purpose: The purpose of this method is to let the user set and
    #          update the video game ESRB of the object being called.
    #
    # Precondition: N/A
    #
    # Input Parameters: (self) & the updated ESRB rating in string format.
    #
    # Return Value: N/A
    #=================================================================

    def set_esrb(self, esrb):

        self.esrb = esrb

    #=================================================================
    # Name: get_title
    #
    # Purpose: The purpose of this method is to let the user recieve
    #          the video game title of the object being called.
    #
    # Precondition: N/A
    #
    # Input Parameters: (self)
    #
    # Return Value: the title of the video game being called.
    #=================================================================

    def get_title(self):

        return self.title

    #=================================================================
    # Name: get_esrb
    #
    # Purpose: The purpose of this method is to let the user recieve
    #          the video game ESRB rating of the object being called.
    #
    # Precondition: N/A
    #
    # Input Parameters: (self)
    #
    # Return Value: the ESRB rating of the video game being called.
    #=================================================================

    def get_esrb(self):

        return self.esrb
    
    #=================================================================
    # Name: get_average
    #
    # Purpose: The purpose of this method is to let the user recieve
    #          the video game's average rating of the object being called.
    #
    # Precondition: N/A
    #
    # Input Parameters: (self)
    #
    # Return Value: The method will return the average rating of the
    #               video game object, if there are no ratings the
    #               method will return a 0.
    #=================================================================
    

    def get_average(self):

        return self.average_ratings

    #=================================================================
    # Name: __str__
    #
    # Purpose: The purpose of this method is to override the string function
    #          and return the print statement of the objects title name,
    #          ESRB rating, and average rating.
    #
    # Precondition: N/A
    #
    # Input Parameters: (self)
    #
    # Return Value: string of the objects title name,ESRB rating, and
    #               average rating.
    #
    #               Ex. Title: Call of Duty, ESRB Rating: AO, Average Rating: 4
    #=================================================================

    def __str__(self):

        return "Title: {}, ESRB Rating: {}, Average Rating: {}".format(self.title, self.esrb, self.average_ratings)



if __name__ == "__main__":


    # Test Code for Problem 1 #

    # import random for list generation #
    import random
    wow = StopWatch()
    print(wow.current_time())
    count = 0
    first_list = []
    while count < 30000:
        first_list.append(random.randint(0, 10000))
        count = count + 1
    wow.set_start()
    first_list.sort()
    wow.set_end()
    print(wow.elapsed_time())
    print(wow.current_time())
    count_two = 0
    second_list = []
    while count_two < 50000:
        second_list.append(random.randint(0, 10000))
        count_two = count_two + 1
    wow.set_start()
    second_list.sort()
    wow.set_end()
    print(wow.elapsed_time())
    print(wow.current_time())

    # Test Code for Problem 2 #

    pokemon_blue = VideoGame("Pokemon Blue", "E", [1000, 800, 500, 200, 90])
    pokemon_red = VideoGame("Pokemon Red", "E", [1000, 800, 500, 200, 90])
    pokemon_yellow = VideoGame("Pokemon Yellow", "E", [1000000, 800, 500, 200, 9000])
    game_list = []
    game_list.append(pokemon_blue)
    game_list.append(pokemon_red)
    game_list.append(pokemon_yellow)
    for x in game_list:
        print(x)

















