def selection_sort(obj_list, key): #Sort activities w/ selection sort
    min_idx = 0
    i = 0
    for i in range(len(obj_list)):
        min_idx = i
        for j in range(i + 1, len(obj_list)): #Skip 0th index
            if obj_list[min_idx][key] > obj_list[j][key]: #Compare
                min_idx = j 
        obj_list[i], obj_list[min_idx] = obj_list[min_idx], obj_list[i] #Swap
    return obj_list


def read_file(filename): #Read in file content
    try:
        contents = []
        f = open(filename, "r")
        for i in f.readlines():
            contents.append(i)
        f.close()
        return contents
    except:
        print("File not found")
        return None

def sort_end_time(events):
    events = selection_sort(events, 2) #Sort times in descending order
    events.reverse() #Reverse
    return events


def any_events_left(events, start_time):
    for event in events:
        if (event[2] <= start_time): #Check for non-overlapping events
            return event
    return False


def schedule_set(events):
    schedule = [events[0]] #Begin at first set
    start_time = events[0][1]  # Retrieve start time of 0th index
    while (any_events_left(events,start_time) != False):  # While still events after end time but before next start time
        next_event = any_events_left(events, start_time)
        schedule.append(next_event)  # Add event to schedule
        start_time = next_event[1]
    return schedule


def display_schedule(schedule, setnumber): #Output activities
    selection_sort(schedule, 0) #Sort data
    print("Set " + str(setnumber))
    print("Number of activities selected = " + str(len(schedule)))
    events_in_schedule = ""
    for event in schedule:
        events_in_schedule = events_in_schedule + str(event[0]) + " "
    print("Activities: " + events_in_schedule)


def process_file(contents):
    processed = []
    for line in contents:
        arr = line.split(" ") #Separate numbers and sets
        data = []
        for item in arr:
            try:
                data.append(int(item)) #Append data to list
            except:
                continue
        processed.append(data)
    return processed


def make_schedule(data):
    i = 0
    setnum = 1
    while (i < len(data)): #While stil data left
        line = data[i]
        if (len(line) == 1): # Check if set or # of sets
            one_set = data[i + 1:i + 1 + line[0]]
            one_set = sort_end_time(one_set) 
            schedule = schedule_set(one_set)
            display_schedule(schedule, setnum)
            setnum += 1
            print("\n")
        i += 1


def main():
    data = process_file(read_file("act.txt"))
    make_schedule(data)


if __name__ == "__main__":
    main()
