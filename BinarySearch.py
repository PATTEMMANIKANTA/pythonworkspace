pos =-1

def search(list,n):
    l = 0
    u = len(list)-1

    while l<=u:
        mid =(l+0)//2

        if list[mid]== n:
            globals()['pos'] = mid
            print("Found")
        else:
            if list[mid] < n:
                l = mid+1
            else:
                u = mid-1
    return False
list = [2,5,7,9,4]

n = 7

search(list,n)