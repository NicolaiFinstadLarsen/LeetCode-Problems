class Solution:
    def scoreOfString(self, s: str) -> int:
        #my_list = []
        #for c in s:
            #print(ord(c))
            #my_list.append(ord(c))
        #new_list = []
        #for i in range(len(my_list) - 1):
            #new_list.append(abs(my_list[i] - my_list[i+1]))
        #return(sum(new_list))

        # Enklere kode
        part_sum = 0
        total = 0
        for c in range(len(s) - 1):
            part_sum = abs(ord(s[c]) - ord(s[c+1]))
            total += part_sum
            #print(part_sum)
            #print(total)
        return total
        