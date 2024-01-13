def solution(n, b):
    previous_IDs = {} # dictionary with previous IDs (in list form) as keys and number of iterations before the key was reached as values
    digit_count = len(n)
    digits_remaining = digit_count
    current_ID = [] # stores "digits" of ID
    for char in n:
        current_ID.append(int(char))
    previous_IDs[tuple(current_ID)] = 0
    while True:
        ascending = sorted(current_ID)
        descending = [None] * digit_count
        subtraction_result = [None] * digit_count
        for i in range(digit_count):    
            descending[i] = ascending[digit_count-1-i]
        i = len(n) - 1
        while i > -1: # digit by digit algorithm to subtract two numbers of base b
            if descending[i] >= ascending[i]:
                subtraction_result[i] = descending[i] - ascending[i]
                i -= 1
            else:
                subtraction_result[i] = b + descending[i]- ascending[i]
                i -= 1
                while descending[i] == 0:
                    subtraction_result[i] = b-1-ascending[i]
                    i -= 1
                descending[i] -=1
        if subtraction_result == current_ID: # if the sequence converges to a value
            return 1
        result_id = tuple(subtraction_result)
        if result_id not in previous_IDs:
            previous_IDs[result_id] = len(previous_IDs)
            current_ID = subtraction_result
        else:
            return len(previous_IDs) - previous_IDs[result_id] 
print(solution('1211', 10))