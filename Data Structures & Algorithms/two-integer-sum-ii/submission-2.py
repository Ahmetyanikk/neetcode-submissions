class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left = 0
        right = len(numbers) - 1

        for i  in range(0,len(numbers)):
            current_sum=numbers[left] + numbers[right]
            if current_sum == target:
                return [left+1,right+1]
            elif current_sum>target:
                right = right-1
            else:
                left = left + 1 
       
        