class Solution:
    def trap(self, height: List[int]) -> int:
        # left_max = [0] * len(height) 
        # right_max = [0] * len(height)

        # left_max[0] = height[0]
        # for i in range(1,len(height)):
        #     left_max[i] = max(left_max[i-1], height[i])
        
        # right_max[len(height)-1] = height[len(height)-1]
        # for i in range(len(height)-2,-1,-1):
        #     right_max[i] = max(right_max[i+1], height[i])

        # res = 0
        # for i in range(len(height)):
        #     res+= min(left_max[i],right_max[i]) - height[i]

        # return res

        n = len(height)
        l,r = 0,n-1
        left_max = height[0]
        right_max = height[n-1]
        res = 0
        while l<r:
            if left_max < right_max:
                l+=1
                left_max = max(left_max,height[l])
                res += left_max -height[l]

            else:
                r-=1
                right_max = max(right_max,height[r])
                res+= right_max - height[r]
        return res
