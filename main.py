list = [38,64,27,18,78,25,12]

def merge_sort(array):
    if len(array) > 1:
        midpoint = len(array)//2
        left_half = array[:midpoint]
        right_half = array[midpoint:]
        merge_sort(left_half)
        merge_sort(right_half)
        i = 0
        j = 0
        k = 0
        #merging 2 sorted halves
        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                array[k] = left_half[i]
                i += 1
            else:
                array[k] = right_half[j]
                j += 1
            k += 1
            print(array)
        while i < len(left_half):
            array[k] = left_half[i]
            k += 1
            i += 1
            print(array)
        while j < len(right_half):
            array[k] = right_half[j]
            k += 1
            j += 1
            print(array)

merge_sort(list)


    