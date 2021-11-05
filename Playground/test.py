from typing import List
def pivotIndex(nums: List[int]) -> int:
    l = 0
    r = 1
    rs = 0
    ls = 0
    n = len(nums);
    x = 0
    while l < n:
        rs=0
        ls=0
        r=l+1
        print("now r = ",r)
        while r <n:
            val = nums[r]
            rs+=val
            r+=1;
        x=0
        while x< l:
            ls+=nums[x]
            x+=1
        l+=1
        r+=1
        
        print("ls",ls)
        print("rs",rs)
        if l==3:
            break;

    
    return;

def main():
    # word = "dreaming91"
    # for i in word:
    #     if i in "keyboard951":
    #         print(i)
    print("")
    word = "crowned56"
    for i in word:
        if i in "keyboard951":
            print(i)
     
  

if __name__ == "__main__":
    main()

            