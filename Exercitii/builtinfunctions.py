def exer_one(numbers):

    for num in numbers:
        if num <=0:
            numbers.append(0)
            break
    
    return(all(numbers))


#print(exer_one([-1,2,3]))


def exer_two(numbers):
    
   
    
    return any(num > 0 for num in numbers)


#print(exer_two([0,1]))

def exer_three(container):

    empty_dict = {}

    for name, position in enumerate(container):
        empty_dict[position] = name

    return empty_dict


#print(exer_three(["ion", "marian"]))

def exer_four(nums1, nums2):
    sums = []
    for firstelem, secondelem in zip(nums1,nums2):
        sums.append(firstelem + secondelem)

    return sums


#print(exer_four([1,2,3], [1,2,3]))