# -*- coding:utf-8 -*-
class Solution:
    def InversePairs(self, data):
        # write code here
        if not data:
            return 0%1000000007
        counts, n = 0, len(data)
        for i, item in enumerate(data[::-1]):
            counts += (self.Count_inverse(data[:-(i+1)], item))
        return counts

    def Count_inverse(self, data, item):
        #print(data)
        if len(data) == 0:
            return 0%1000000007
        data.sort(reverse=True)
        #print(data)
        if data[0] <= item:
            return 0
        elif data[-1] > item:
            return len(data)%1000000007
        start, end = 0, len(data)-1
        while start < end:
            if (end - start) == 1:
                return (start + 1)%1000000007
            mid = (start + end)//2
            if data[mid] > item:
                start = mid
            if data[mid] < item:
                end = mid
            if data[mid] == item:
                while data[mid] == item:
                    mid -= 1
                    if mid < 0:
                        return 0%1000000007
                return (mid + 1)%1000000007

        #return sum(list(map(lambda x:x>item, data)))
def main():

    Solu = Solution()

    ls = [364,637,341,406,747,995,234,971,571,219,993,407,416,366,315,301,601,650,418,355,460,505,360,965,516,648,727,667,465,849,455,181,486,149,588,233,144,174,557,67,746,550,474,162,268,142,463,221,882,576,604,739,288,569,256,936,275,401,497,82,935,983,583,523,697,478,147,795,380,973,958,115,773,870,259,655,446,863,735,784,3,671,433,630,425,930,64,266,235,187,284,665,874,80,45,848,38,811,267,575]
    import time
    start = time.time()
    result = Solu.InversePairs(ls)
    print(result, time.time()-start)

if __name__ == '__main__':
    main()
