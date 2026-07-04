class Solution:
    def recurse_string(self, index, current):
        n = len(self.arr)
        if index == n:
            # print(".", current)
            self.result.append(current[:])
            return
        self.recurse_string(index + 1, current + self.string[index])
        self.recurse_string(index + 1, current)

    def generate_subsequences_string(self, string):
        self.string = string
        current = ""
        index = 0
        self.result = []
        self.recurse_string(index, current)
        for i in self.result:
            print(i)

    def recurse(self, index, current):
        n = len(self.arr)
        if index == n:
            # print(".", current)
            self.result.append(current[:])
            return
        current.append(self.arr[index])
        self.recurse(index + 1, current)
        current.pop()
        self.recurse(index + 1, current)

    def generate_subsequences(self, arr):
        self.arr = arr
        current = []
        index = 0
        self.result = []
        self.recurse(index, current)
        for i in self.result:
            print(i)

    def count_all_subsequences_with_sum_K(self, K):
        print(self.arr, K)
        pass


# arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
arr = [1, 2, 3]
string = "abc"
sol = Solution()
K = 10
# sol.count_all_subsequences_with_sum_K(K)
sol.generate_subsequences(arr)
sol.generate_subsequences_string(string)
