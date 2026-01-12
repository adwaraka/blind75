# Add three sum problem here
class ThreeSum(object):

    def threeSum(self, arr: list) -> list:
        result = []
        arr.sort()
        n = len(arr)

        for num in range(n - 2):
            # print(arr[num])
            left = num + 1
            right = n - 1

            # currently considered number already taken care of
            if num > 0 and arr[num] == arr[num-1]:
                continue

            while left < right:
                currentSum = arr[num] + arr[left] + arr[right]
                if currentSum == 0:
                    result.append([arr[num], arr[left], arr[right]])
                    left+=1
                    right-=1

                    # keep moving left ptr if the numbers are all same
                    while arr[left] == arr[left-1] and left < right:
                        left+=1

                    # keep moving right ptr if nums are still same
                    while arr[right] == arr[right+1] and left < right:
                        right-=1

                # less than zero, we may want something bigger so move left ptr
                elif currentSum < 0:
                    left+=1

                # more than zero, we may want something smaller so move the right ptr
                elif currentSum > 0:
                    right-=1
        return result


arr = [-1, 0, 1, 1, 2, -1, -4]
ts = ThreeSum()
print(ts.threeSum(arr))
