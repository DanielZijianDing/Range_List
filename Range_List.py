## Range List

# Author Name: Daniel Ding
# Last Update: May 22, 2024
# Description: This program is intended to express an infinie number of (x,y) pairs by only showing where
#              the value of y changes. 
# Method: To achieve this, the real data is the augmentation of stored data. 
#         For example, for data [[x1,y1], [x2,y2], [x3,y3]], it is stored as [[x1,y1], [x2,y2-y1], [x3, y3-y2]]
#         When call function "code", the shown y(x) is the augmentation of the stored data before x
# Notes: both x and y are floats

class range_list():
    
    def __init__(self): # initialization
        self.dict = {}
        print('Start:[]')
        
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
        print(f'Call: add({start},{end},{amount}) ==> ',end='')
        self.show()
            
    def set(self, start, end, amount): # to set the value of the range [from, to) to a given amount
        # if the data is empty:
        if self.dict == {}:
            result = {str(start): amount, str(end): 0}
        else:
            # get the real data
            result = self.decode()
            # if x=from exists in the data, set y at x=from to amount; if not, create (x, amount)
            if start in list(result.keys()):
                result[str(start)] = amount
            else:
                result.update({str(start): amount}) 
            #delete the data point between x=start and x=end
            for i in sorted(list(result.keys())):
                if float(i) > start and float(i) < end:
                    holder = result[i]
                    del result[i]
            # if x=to does exist in the data, not need to change; if not, find the y at x=to
            if str(end) not in list(result.keys()): 
                result.update({str(end): '_'})
                result[str(end)] = holder
            # output the result
            result = dict(sorted(result.items()))
        # update the stored data
        self.dict = self.code(result)
        print(f'Call: set({start},{end},{amount}) ==> ',end='')
        self.show()
        
    def decode(self): # to decode the stored data to the real data (the data cannot be empty at this time)
        sorted_dict = dict(sorted(self.dict.items())) # make the dictionary in order according to the key
        key_list = sorted(list(self.dict.keys())) # an ordered list of all keys
        result = {key_list[0]: self.dict[key_list[0]]}# initialization, the first pair in the result dictionary
        for i in range(1,len(self.dict)):
            new_key = key_list[i]
            result.update({new_key: self.dict[new_key] + result[key_list[i-1]]})
        return result
    

    def code(self,data): # # to code the real data to the format of the stored data
        key_list = sorted(list(data.keys())) # an ordered list of all keys
        result = {key_list[0]:data[key_list[0]]}# initilization, the first pair in the result dictionary
        for i in range(1,len(data)):
            result.update({key_list[i]:(data[key_list[i]] - data[key_list[i-1]])})
        return result
    
    def show(self): #print the data in the form of [[x1,y1],[x2,y2],[x3,y3]]
        print(list([float(i[0]),i[1]] for i in self.decode().items()))
        
    def result(self): #the data as a dictionary
        return list([float(i[0]),i[1]] for i in self.decode().items())
