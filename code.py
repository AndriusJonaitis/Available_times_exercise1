def convert_to_min(times, matrix=True):
    if matrix:
        for j in range(len(times)):
            for i in range(len(times[0])):
                times[j][i] = times[j][i].replace(':', '.')                           # '10:30' converting to '10.3'
                times[j][i] = float(times[j][i])                                      # string to double
                times[j][i] = (float(int(times[j][i])) + 100*(times[j][i]%1)/60)      # 10.3 converting to 10.5
                times[j][i] = round(times[j][i]*60)                                   # computing minutes
        return times

    if not matrix:
        times = [i.replace(':', '.') for i in times]   
        times = [float(i) for i in times]
        times = [(float(int(i)) + 100*(i%1)/60) for i in times]
        times = [round(i*60) for i in times]
        return times


def available_times(calendar, bound):
    times = []

    for j in range(len(calendar)):
        # start bound to first meeting
        if j==0 and calendar[j][0] - bound[0] > 0:
            times.append([bound[0], calendar[j][0]])

        # previous meeting end to next meeting start
        if j!=len(calendar)-1 and (calendar[j+1][0] - calendar[j][1]) > 0:
            times.append([calendar[j][1], calendar[j+1][0]])
        
        # last meeting to end bound
        if j==len(calendar)-1 and bound[1] - calendar[j][1] > 0:  
            times.append([calendar[j][1], bound[1]])
    return times


def compare_times(list_1, list_2):
    output =[]

    for i in range(len(list_1)):
        if list_1[i][0] >= list_2[i][0]:
            start_time = list_1[i][0]
        else:
            start_time = list_2[i][0]

        if list_1[i][1] <= list_2[i][1]:
            end_time = list_1[i][1]
        else:
            end_time = list_2[i][1]

        output.append([start_time, end_time])
    return output


def convert_output(output):
    for j in range(len(output)):
            for i in range(len(output[0])):
                output[j][i] = output[j][i]/60
                output[j][i] = format((int(output[j][i])) + 60*(output[j][i]%1)/100, '.2f')
                output[j][i] = str(output[j][i])
                output[j][i] = output[j][i].replace('.', ':')
    return output


calendar_1 = [['9:00','10:30'], ['12:00','13:00'], ['16:00','18:00']]
bound_1 = ['9:00','20:00']

calendar_2 = [['10:00','11:30'], ['12:30','14:30'], ['14:30','15:00'], ['16:00','17:00']]
bound_2 = ['10:00','18:30']

calendar_1 = convert_to_min(calendar_1)
bound_1 = convert_to_min(bound_1, False)
available_1 = available_times(calendar_1, bound_1)

calendar_2 = convert_to_min(calendar_2)
bound_2 = convert_to_min(bound_2, False)
available_2 = available_times(calendar_2, bound_2)

output = compare_times(available_1, available_2)
output = convert_output(output)
print(output)
