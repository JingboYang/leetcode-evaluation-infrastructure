def smallestDistancePair(nums, k):

    nums.sort()

    def count_possible(guess):

        left = 0
        count = 0
        print('Guess ' + str(guess))
        for r_index, r_val in enumerate(nums):
            while r_val - nums[left] > guess:
                left += 1
            count += r_index - left
        return count


    low = 0
    high = nums[-1] - nums[0]

    while low < high:
        guess = int((low + high) / 2)
        count = count_possible(guess)

        print(count)

        if count >= k:
            high = guess
        else:
            low = guess + 1

    return low


def main():
    result = smallestDistancePair([1,4,2,5,2], 1)
    print(result)