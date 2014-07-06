#rotated sorted array search for minimum

class BinarySearchRotatedArray:

    def get_minimum(self, inp):
        a = inp
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

