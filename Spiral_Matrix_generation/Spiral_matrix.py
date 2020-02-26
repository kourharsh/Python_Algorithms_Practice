class Solution:
    def generateMatrix(self, n):
        num = n
        matrix = [[0 for i in range(0, n)] for _ in range(0, n)]
        k = 0
        l = 0
        m = num
        n = num
        arr = []
        for j in range(1, (num * num) + 1):
            arr.append(j)

        index = 0

        while (k < m and l < n):

            for i in range(k, n):
                matrix[k][i] = arr[index]
                index += 1
            k = k + 1

            for i in range(k, n):
                matrix[i][n - 1] = arr[index]
                index += 1
            n = n - 1

            for i in range(n - 1, l - 1, -1):
                matrix[m - 1][i] = arr[index]
                index += 1
            m = m - 1

            for i in range(m - 1, k - 1, -1):
                matrix[i][l] = arr[index]
                index += 1
            l = l + 1

        return matrix
sol = Solution()
print(sol.generateMatrix(4))
