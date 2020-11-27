# Basim Siddiqui
# PSID: 1517778

# Global variable
num_calls = 0

def partition(user_ids, i, k):
    pivot_val = user_ids[k]
    partition_val = i - 1
    for item in range(i, k):
        if user_ids[item] <= pivot_val:
            partition_val += 1
            user_ids[partition_val], user_ids[item] = user_ids[item], user_ids[partition_val]
    user_ids[partition_val + 1], user_ids[k] = user_ids[k], user_ids[partition_val + 1]
    return partition_val + 1


def quicksort(user_ids, i, k):
    if i >= k:
        return
    else:
        j = partition(user_ids, i, k)
        quicksort(user_ids, i, j-1)
        quicksort(user_ids, j, k)


if __name__ == "__main__":
    user_ids = []
    user_id = input()
    while user_id != "-1":
        user_ids.append(user_id)
        user_id = input()

    # Initial call to quicksort
    array_len = len(user_ids)
    quicksort(user_ids, 0, array_len - 1)
    num_calls = int(2 * array_len - 1)
    # Print number of calls to quicksort
    print(num_calls)

    # Print sorted user ids
    for user_id in user_ids:
        print(user_id)
