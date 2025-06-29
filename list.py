def find_common_elements(list1, list2):
    if len(list1) < len(list2):
        set1= set(list1)
    return [item for item in list2 if item in set1]
    
    else: 
        set2 = set(list2)
          return [item for item in list1 if itme in set2]
            
            
 a= [1,2,3,4,5,6,7,8,9]
 b= [1,50,100,9,3,80]

print (find_common_elements(a,b))
