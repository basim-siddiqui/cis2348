# Basim Siddiqui
# PSID: 1517778

def selection_sort_descend_trace(int_list):
    for i in range(len(int_list) - 1):
        indecs = i
        for item in range(i + 1, len(int_list)):
            if int_list[item] > int_list[indecs]:
                indecs = item
        int_list[i], int_list[indecs] = int_list[indecs], int_list[i]
        for num in int_list:
            print(num, end=" ")
        print()
    return int_list

if __name__ == "__main__":
    integers = [int(x) for x in input("").split()]
    selection_sort_descend_trace(integers)