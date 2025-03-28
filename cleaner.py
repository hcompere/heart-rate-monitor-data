import os
print(os.getcwd())
"""
phase = "/Users/hachemingcompere/Downloads/hr_monitoring_data_processing/data/phase0.txt"
phase_file = open(phase)
phase_text = phase_file.read()
print(phase_text)
for line in phase_file:
     digit_phase = int(line.strip())
     print(digit_phase)
"""


def filter_nondigits(data: list) -> list:
    """
    INSERT DOCSTRING HERE
    create a function to filter out non-digit data, a list of intergers with no missing values
    for every item in list, if 
    """
    
    digit_data = []
    for digit in data:
            digit = str(digit).strip()   
            if digit.isdigit():
                  digit_data.append(int(digit))      #turns items from list into strings and removes new lines 
           # if not digit or digit == "NO DATA":  # continue if not empty string or "NO DATA"
            #      continue        
            #value = digit.isdigit           
            #for v in value:
            #     heart_rate = int(v)             #converts back to integer
             #    digit_data.append(heart_rate)  #adds integer to new list 
    return digit_data
                 
#example = [1,2,3,"NO DATA","",8,9 ]
#print(filter_nondigits(example))
    
#new = [1,2,3,4,5]
#print(new)
