from typing import List

def twoSum( nums: List[int], target: int) -> List[int]:
    map ={}
    for i in range(len(nums)):
        map[nums[i]]=i;
    print(map)
    for i in range(len(nums)):
        complement = target-nums[i]
        if complement in map and map[complement]!=i:
            return [i,map[complement]]

def main():
    nums=[2,7,11,15]
    target=9
    res = twoSum(nums,target)
    print(res)
  
     
  

if __name__ == "__main__":
    main()

            