def twoSum(self, nums: List[int], target: int) -> List[int]:
        visto = {}
        for i, value in enumerate(nums): 
            restante = target - nums[i] 
           
            if restante in visto: 
                return [i, visto[restante]]  
            else:
                visto[value] = i  