import time

def findMaximumXOR(nums):
    
    class TrieNode:
        def __init__(self, val):
            self.val = val
            self.left = None
            self.right = None
    

    def trie_insert(root, vals):

        cur_node = root
        i = 0
        #print(vals)
        while i < len(vals):
            v = vals[i]
            i += 1

            if cur_node.left is not None and v == cur_node.left.val:
                cur_node = cur_node.left
                #continue
            elif cur_node.right is not None and v == cur_node.right.val:
                cur_node = cur_node.right
                #continue
            else:
                if v == 0:
                    cur_node.left = TrieNode(0)
                    cur_node = cur_node.left
                else:
                    cur_node.right = TrieNode(1)
                    cur_node = cur_node.right

            #print_trie(root)
            #print('----')

    def print_trie(cur_node, level=0):
        
        if cur_node is None:
            return
        
        string = ' ' * level*6
        string += str(cur_node.val).rjust(1) + '->'
        print(string)

        print_trie(cur_node.left, level + 1)
        print_trie(cur_node.right, level + 1)


    trie_root = TrieNode(0)
    binaries = [bin(n)[2:] for n in nums]
    longest = -1
    for b in binaries:
        longest = max(len(b), longest)
    for i in range(len(binaries)):
        binaries[i] = binaries[i].rjust(longest, '0')
        binaries[i] = [int(x) for x in binaries[i]]
        #print(binaries[i])

    for n in binaries:
        trie_insert(trie_root, n)
    
    #print_trie(trie_root)


    global best
    best = -1
    def build_max(t1, t2, sofar=[]):

        if t1 is None or t2 is None:
            return
        sofar.append(t1.val ^ t2.val)

        if len(sofar) >= longest + 1:
            global best
            val = [str(r) for r in sofar]
            val = int(''.join(val))
            best = max(best, val)
            return

        
        okay = False
        if t1.left is not None and t2.right is not None:
            build_max(t1.left, t2.right, sofar[:])
            okay = True
        if t1.right is not None and t2.left is not None:
            build_max(t1.right, t2.left, sofar[:])
            okay = True
        
        if not okay:
            build_max(t1.left, t2.left, sofar[:])
            build_max(t1.right, t2.right, sofar[:])
        

        '''
        build_max(t1.left, t2.left, sofar[:])
        build_max(t1.right, t2.right, sofar[:])
        build_max(t1.right, t2.left, sofar[:])
        build_max(t1.left, t2.right, sofar[:])
        '''

    build_max(trie_root, trie_root, [])

    #result = [str(r) for r in best]
    #result = int(''.join(result))

    return int(str(best), 2)




in_vals = [3, 10, 5, 25, 29, 28, 8]
in_vals = [58227,90480,1487,21960,59317,26882,23523,14697,44867,33417,35592,60757,93256,88953,77135,45750,209,65155,28958,90960,4954,27643,38662,71827,26129,25203,96736,62000,31689,72902,53417,21353,74590,54578,23768,14816,87391,65500,10840,53649,43965,39895,20294,37020,32110,10271,77865,61754,18334,1056,10120,4081,41011,99508,44620,48834,54108,88073,24212,51904,50966,65248,88591,57883,65754,76946,46970,37082,42789,14637,43989,29511,68453,35292,164,55557,93821,57925,66015,99996,41078,34348,90390,14005,85571,94901,6757,53921,29519,84071,86768,89267,3557,60619,24283,44206,64027,6484,85481,52441,25595,1784,5583,19792,50095,28988,35955,47700,53737,95055,22726,13634,48813,54061,2108,34688,98172,64931,31524,17812,19198,35058,75400,11247,52970,58348,25379,95750,63669,65500,39961,40162,43093,30242,90328,47629,77168,29596,23849,24237,9894,20032,82963,8014,3960,62501,57164,93015,81171,70754,98109,20286,60733,50510,82065,49943,12091,36615,39897,78567,87804,49070,36895,75000,88838,76207,81413,63909,2939,81182,56538,35061,75815,29373,86328,61604,18153,91642,28349,66045,55899,50261,82723,4068,79648,7615,7550,1711,12586,9919,41074,25045,96645,95790,29007,93727,46019,76866,50922,73659]
for n in in_vals:
    break
    print(bin(n))

start = time.time()
value = findMaximumXOR(in_vals)
end = time.time()
print(value)
print(end - start)
