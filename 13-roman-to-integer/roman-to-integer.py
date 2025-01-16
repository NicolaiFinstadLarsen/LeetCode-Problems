class Solution:
    def romanToInt(self, s: str) -> int:
        #edge cases
        my_dict = {"I": 1, "V" : 5, "X" : 10, "L" : 50, "C" : 100, 
        "D" : 500, "M" : 1000}
        sum = 0
        # -1 range since we use c of s +1
        for c in range(len(s)-1):
            if my_dict[s[c]] < my_dict[s[c+1]]:
                sum -= my_dict[s[c]] 
                #print(sum)
            else:
                sum += my_dict[s[c]]
                #print(sum)
        # For last char since range is -1 and last char does not have a pair
        sum += my_dict[s[-1]]
        #print(sum)
        return sum
            
        