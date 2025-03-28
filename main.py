"""
The main Python mpdule that combines cleaner and metrics functions in order to
perform comprehensive analysis
"""

from metrics import average, maximum, standard_deviation
from cleaner import filter_nondigits

import matplotlib.pyplot as plt


def run(filename: str) -> None:
    """
    Process heart rate data from the specified file, clean it, calculate metrics,
    and save visualizations.

    Args:
        filename (str): The path to the data file (e.g., 'data/phase0.txt').

    Returns:
        float, float, float: You will return the average, max, and standard deviation
    """ 
    data = []
    
    


    # open file using file I/O and read it into the `data` list
    ...
    with open(filename) as file:
        for line in file.readlines():       #reads file into a list
                line = line.strip()          #removes new line character
                data.append(line)            #adds new list called data which will hold a string list of heartrate data

    
    
    
   
    # Use `filter_nondigits` to clean the data and remove invalid entries, save the output to a new variable
    ...
    
    filtered_data = filter_nondigits(data) 
    # plot this data to explor changes in heart rate for this file, save this visualization to the "images" folder
    ...
    

   

    graph_plot = "/Users/hachemingcompere/Downloads/hr_monitoring_data_processing/images/phase_graph.png"
    plt.plot(filtered_data, label=filename)                     #makes a line plot of filtered and gives it the label of the source file name
    plt.title("Heart Rate Data")
    plt.xlabel("x-axis")
    plt.ylabel("BPM")
    plt.legend()
    plt.savefig(graph_plot) #couldn't figure out how to get it to save different images of the graphs so I just layered them and created a legend to differentiate the phases
    

    # calculate the average, maximum, and standard deviation of this file using the functions you've wrote
    avg_hr = average(filtered_data)
    max_hr = maximum(filtered_data)
    std_dev_hr = standard_deviation(filtered_data)

    # return all 3 values
    return avg_hr, max_hr, std_dev_hr


if __name__ == "__main__":
    print("Phase 0:",run("data/phase0.txt"))
if __name__ == "__main__":
    print("Phase 1:",run("data/phase1.txt"))
if __name__ == "__main__":
    print("Phase 2:",run("data/phase2.txt"))
if __name__ == "__main__":
    print("Phase 3:",run("data/phase3.txt"))
