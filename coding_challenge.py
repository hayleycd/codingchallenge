import math

def calculate( new_number, result):
    mysum, mymedian, myaverage, list_previous_numbers = result
    mysum = mysum + new_number
    myaverage = (mysum/(len(list_previous_numbers) + 1))
    list_previous_numbers.append(new_number)
    new_list_numbers = sorted(list_previous_numbers)
     
    if len(new_list_numbers) % 2 == 0:
        half_way = len(new_list_numbers)/2
        mymedian = (new_list_numbers[half_way] + new_list_numbers[half_way-1]) / 2
    else:
        mymedian = new_list_numbers[(int(math.floor(len(new_list_numbers)/2)))]
     
    result = (mysum, mymedian, myaverage, new_list_numbers)
    return result

def format_output(output):
    print "SUM: " + str(output[0]) + " MEDIAN: " + str(output[1]) + " AVERAGE: " + str(output[2]) + " LIST OF NUMBERS: " , output[3]

def calculate_for_a_list(mylist):
    initial = (0,0,0,[])
    result = calculate(mylist[0], initial)
    format_output(result)

    for each in mylist[1:]:
        result = calculate(each, result)
        format_output(result)

