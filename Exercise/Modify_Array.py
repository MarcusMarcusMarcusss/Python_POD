Rules: check for dupliate item in an array and you are not allowed to sort array/modify in anycase. array has to be unsorted. Number in an array are between 1-6//included 


Python:
Given List below :
  
  def duplicateItem(nums):
  //write your code 
  #
  # #
  # # #
  
  
  prinf(duplicateItem([2,4,6,5,3,1,]));
  
  
  
  me:
    explain how this do 
     numbers are convert into binarys when they stored in computer hence if i want do check if the array is containing 
     duplicate or not determs whether they have same binary(ASCII) of 0 and 1. For example   10 =2  11=3 100=4 101=5 110=6 111=7 1000=8  
                                                                                              .... 10101 =21  ....
                                                                                              you right those are all bullshits
                                                                                                For this you need to use tortois and hares algorithm
                                                                                                  0*1 0*2 0*3 0*4  : this algorithm allows one runs twice as fast as another inhelps to solve (o)2
def duplicateItem(nums):
      mose=nums[0]
      hary=nums[0]
      while True:
        mose=nums[mose]
        hary=nums[nums[hary]]
        if mose == hary:
           break
   
        ptr2=nums[0]
        ptr3=mose
        while ptr2 != ptr3:
          ptr2=nums[ptr2]
          ptr3=nums[ptr3]
          return ptr3
  
print(duplicateItem([1,4,2,3,5,6,3]))
       
      
