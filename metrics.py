def average(data: list) -> float:
    """
    Calculate average value of the list.

    Args:
        data (list[int]): list of integers representing heart rate samples
    Returns:
        float: a floating point value representing the average of this list
    """
    
    if len(data) == 0:              #guard to return empty list if no data
        return []
    total = sum(data)               #variable to store the sum of data
    mean = total/(len(data))        #calculate average by divding sum by the amount of data point ie len(data)
    return round(mean, 2)
    ...


def maximum(data: list) -> float:
    """
    INSERT DOCSTRING HERE
    """
    if len(data) == 0:          #guard to return empty list if there is no data
        return []
    max = data[0]               #setting variable max to equal the first number in the data list
    for digit in data:          #for loop to go through each data point in list
        if digit > max:         #if the new data point is greater than max, it replaces max, after going through whole dadta set you are left with the max value
            max = digit
    return max
    pass


def variance(data: list) -> float:
    """
    INSERT DOCSTRING HERE
    (calculate population variance)
    """
    if len(data) == 0:              #guard to return empty list if there is no data
        return []

    for var in data:
        mean = sum(data)/len(data)                      #define variable for mean 
        diff_squared = [(var-mean)**2 for var in data] #making a list of differences of (item - mean) squared for each value in data 
        v = (sum(diff_squared)/(len(data))) #sum of list divided by population size gives you variance
        return round(v, 2)

    pass


def standard_deviation(data: list) -> float:
    """
    INSERT DOCSTRING HERE
    (calculate population standard deviation)
    """
    if len(data) == 0:                      #guard ti return empty list if there is no data
        return []
    for var in data:                        
        var = variance(data)                
        return round((var**0.5),2)#standard deviation is squareroot of variance 

   
    pass
