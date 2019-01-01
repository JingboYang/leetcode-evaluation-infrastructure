def maxNumber(self, nums1, nums2, k):

    import heapq 

    def largest_and_truncate(array):
        if len(array) == 0:
            return -1, []
        l = max(array)
        #largests = heapq.nlargest(2, array)
        #i = array.index(largests[0])
        i = array.index(l)
        new_array = array[i + 1:]

        #return largests, new_array
        return l, new_array


    def allowed_array(a1, a2, k_val):
        k1 = []
        k2 = []
        a1_new = a1
        a2_new = a2
        if k_val - 1 - len(a2) > 0:
            k1 =     a1[ -  (k_val - 1 - len(a2)): ]
            a1_new = a1[: - (k_val - 1 - len(a2))  ]
        if k_val - 1 - len(a1) > 0:
            k2 =     a2[ -  (k_val - 1 - len(a1)): ]
            a2_new = a2[: - (k_val - 1 - len(a1))  ]
            
        return a1_new, a2_new, k1, k2

    global best
    best = 0
    def construct(a1, a2, k_val, selected):
        
        #print('selected:')
        #print(selected)
        #print(a1, a2, k_val)

        if k_val == 0:
            global best
            sel_val = int(''.join([str(s) for s in selected]))
            best = max(best, sel_val)
            return

        allowed1, allowed2, keep1, keep2 = allowed_array(a1, a2, k_val)

        #print('allowed:')
        #print(allowed1, allowed2)
        #print('keeps:')
        #print(keep1, keep2)

        large1, new1 = largest_and_truncate(allowed1)
        large2, new2 = largest_and_truncate(allowed2)

        if large1 > large2:
            #print('use ' + str(large1))
            selected.append(large1)
            new1.extend(keep1)
            construct(new1, a2, k_val - 1, selected)
        elif large2 > large1:
            #print('use ' + str(large2))
            selected.append(large2)
            new2.extend(keep2)
            construct(a1, new2, k_val - 1, selected)
        else:
            #print('tie')

            select = selected[:]
            select.append(large1)
            new1.extend(keep1)
            construct(new1, a2, k_val - 1, select)

            select = selected[:]
            select.append(large2)
            new2.extend(keep2)
            construct(a1, new2, k_val - 1, select)

    construct(nums1, nums2, k, [])

    return best


signature = 'def maxNumber(self, nums1, nums2, k):'
input_string = """[3,4,6,5]
[9,1,2,5,8,3]
5"""


def main():
    return
    #nums1 = [3,4,6,5]
    #nums2 = [9,1,2,5,8,3]
    #k = 5

    nums1 = [2,5,6,4,4,0]
    nums2= [7,3,8,0,6,5,7,6,2]
    k = 15

    #nums1 = [6,4,7,8,6,5,5,3,1,7,4,9,9,5,9,6,1,7,1,3,6,3,0,8,2,1,8,0,0,7,3,9,3,1,3,7,5,9,4,3,5,8,1,9,5,6,5,7,8,6,6,2,0,9,7,1,2,1,7,0,6,8,5,8,1,6,1,5,8,4]
    #nums2 = [3,0,0,1,4,3,4,0,8,5,9,1,5,9,4,4,4,8,0,5,5,8,4,9,8,3,1,3,4,8,9,4,9,9,6,6,2,8,9,0,8,0,0,0,1,4,8,9,7,6,2,1,8,7,0,6,4,1,8,1,3,2,4,5,7,7,0,4,8,4]
    #k = 70


    a = maxNumber(nums1, nums2, k) 
    print(a)

