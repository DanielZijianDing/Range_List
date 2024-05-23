## Range List

# Author Name: Daniel Ding
# Last Update: May 22, 2024
# Description: This program is intended to express an infinie number of (x,y) pairs by only showing where
#              the value of y changes. 
# Method: To achieve this, the real data is the augmentation of stored data. 
#         For example, for data [[x1,y1], [x2,y2], [x3,y3]], it is stored as [[x1,y1], [x2,y2-y1], [x3, y3-y2]]
#         When call function "show", the shown y(x) is the augmentation of the stored data before x
# Notes: both x and y are floats

class range_list():
    
    def __init__(self): # initialization
        self.dict = {}

        
    def add(self, start, end, amount): # to increase the value of the range [from, to) by a given amount
    # method: in the stored data, we need to increase the y at x=from by amount and decrease the y at x=end by -amount
    # if these x are not in the stored data yet, create new ones
        if str(start) not in list(self.dict.keys()):
            self.dict.update({str(start): amount})
        else:
            self.dict[str(start)] += amount
        if str(end) not in list(self.dict.keys()):
            self.dict.update({str(end): -amount})
        else:
            self.dict[str(end)] += -amount
            
    def set(self, start, end, amount): # to set the value of the range [from, to) to a given amount
        # get the real data
        result = self.show()
        # if x=from exists in the data, set y at x=from to amount; if not, create (x, amount)
        if start in list(result.keys()):
            result[str(start)] = amount
        else:
            result.update({str(start): amount}) 
        # if x=to does exist in the data, not need to change; if not, find the y at x=to
        if str(end) not in list(result.keys()): 
            result.update({str(end): '_'})
        for i in sorted(list(result.keys())):
            if float(i) > start and float(i) < end:
                holder = result[i]
                del result[i]
                result[str(end)] = holder
        # output the result
        result = dict(sorted(result.items()))
        # update the stored data
        self.dict = reverse_show(result) 

        
    def show(self): # to convert the stored data to the real data and show it
        sorted_dict = dict(sorted(self.dict.items())) # make the dictionary in order according to the key
        key_list = sorted(list(self.dict.keys())) # an ordered list of all keys
        result = {}# initilization, the first pair in the result dictionary
        for i in range(len(self.dict)):
            result.update({key_list[i]:sum(self.dict[key_list[j]] for j in range(i+1))})
        print("The range list is",list([float(i[0]),i[1]] for i in result.items()))
        return result
    
def reverse_show(norm_form): # # to convert the real data to the format of the stored data
    key_list = sorted(list(norm_form.keys())) # an ordered list of all keys
    result = {key_list[0]:norm_form[key_list[0]]}# initilization, the first pair in the result dictionary
    for i in range(1,len(norm_form)):
        result.update({key_list[i]:(norm_form[key_list[i]] - norm_form[key_list[i-1]])})
    return result

