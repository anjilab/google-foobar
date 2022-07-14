# input = ([1, 2, 2, 3, 3, 3, 4, 5, 5], 1) // o/p =>1,4

# def solution(data, n):
#     rep_dict = {}
#     output = []
#     for items in data:
#         if items in rep_dict:
#             rep_dict[items] = rep_dict[items] + 1
#         else:
#             rep_dict[items] = 1
#     for key in rep_dict:
#         if rep_dict[key] <= n:
#             output.append(key)

#     if len(output) > 0:
#         return
#     else:
#         return output

# print(solution([1, 2, 2, 3, 3, 3, 4, 5, 5], 2))
# print(solution([1, 2, 3], 0))
# print(solution([5, 10, 15, 10, 7], 1))

from collections import OrderedDict
from collections import Counter

def solution(data, n):
    my_dictionary=OrderedDict()
    output = []
    for items in data:
        if items in my_dictionary.keys():
            my_dictionary[items] = my_dictionary[items] + 1
        else:
            my_dictionary[items] = 1
    for items in data:
        if data.count(items) <= n: 
            output.append(items)
                
    

    if len(output) <= 0:
        return
    else:
        return output


# print(solution([1, 2, 2, 3, 3, 3, 4, 5, 5], 2))
# print(solution([1, 2, 3], 0))
print(solution([5, 10, 15, 10, 7], 1))
