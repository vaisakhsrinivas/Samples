def youmethod(input_list):


    recordbreakingdays = []

    currentrecordbreakingday = input_list[0]

    for i in range (0,len(input_list)-1):

        if input_list[i+1] > input_list[i] and input_list[i+1] != input_list[i] and input_list[i+1] > currentrecordbreakingday:

            currentrecordbreakingday = input_list[i+1]

            recordbreakingdays.append(currentrecordbreakingday)

        if input_list[i+1] == input_list[i] and input_list[i+1] >= currentrecordbreakingday:
            currentrecordbreakingday = input_list[i+1]

            if currentrecordbreakingday not in recordbreakingdays:
                recordbreakingdays.append(currentrecordbreakingday)
            else:
                continue

    return recordbreakingdays




print(youmethod([5,10,25,83]))













