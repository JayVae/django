

class Solution(object):
    def addBoldTag(self,s,dict):
        # dict_ans={}
        for i,value in enumerate(dict):
            start = 0
            # dict_ans[value] = []
            while True:
                index = s.find(value, start)
                if index == -1:
                    break
                print("%s found at index %d" % (value, index))
                # dict_ans[value] = index
                start = index + 1

        # print(dict_ans)
        print("end")


if __name__ == '__main__':
    s="abcxyz123"
    dict=["123","abc"]
    sol=Solution
    sol.addBoldTag(sol,s,dict)