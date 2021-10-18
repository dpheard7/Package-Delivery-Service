from datetime import timedelta

from Project.Distances import distance_array


def new_distance_search(current_location, destination):
    # breakpoint()
    i = 0
    for row_data in distance_array:
        if current_location in row_data[0]:
            current_index = i
            break
        i += 1
    i = 0
    for row_data in distance_array:
        if destination in row_data[0]:
            destination_index = i
            break
        i += 1
    # breakpoint()
    miles = float(distance_array[current_index][destination_index + 1])
    return miles, i


#  calculates the time it takes to reach an address by the miles traveled
def time_calculator(miles):
    time = miles / 18
    return timedelta(hours=time)



