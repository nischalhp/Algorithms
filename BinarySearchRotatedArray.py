#rotated sorted array search for minimum

class BinarySearchRotatedArray:

    def get_minimum(self):
        a = [3,4,5,6,7,1,2]
        low = 0
        high = len(a) - 1
        # this condition here solves everything!!
        while a[low] > a[high]:
            mid = (low+high)/2
            print "finding mid " + str(mid)
            # now mid point figured out
            if a[mid] > a[high]:
                low = mid + 1
            else:
                high = mid

        return low,a[low],a[high]


obj = BinarySearchRotatedArray()
low,low_value,high_value= obj.get_minimum()
print low , low_value , high_value




