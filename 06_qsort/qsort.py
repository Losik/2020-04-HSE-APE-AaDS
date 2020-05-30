import random


def lamuto_partition(arr, begin, end, pivot):
    end -= 1
    arr[end], arr[pivot] = arr[pivot], arr[end]

    dst = begin
    for src in range(begin, end):
        if arr[src] < arr[end]:
            arr[dst], arr[src] = arr[src], arr[dst]
            dst += 1

    arr[end], arr[dst] = arr[dst], arr[end]
    return (begin, dst), (dst + 1, end + 1)


def lamuto_partition_upgraded(arr, begin, end, pivot):
    pivot_value = arr[pivot]

    l_dst = begin
    e_dst = begin
    for src in range(begin, end):
        if arr[src] < pivot_value:
            arr[l_dst], arr[src] = arr[src], arr[l_dst]
            l_dst += 1
            e_dst = max(l_dst, e_dst)
        if arr[src] == pivot_value:
            arr[e_dst], arr[src] = arr[src], arr[e_dst]
            e_dst += 1

    return (begin, l_dst), (e_dst, end)


def quick_sort(arr, begin=0, end=None, partition=lamuto_partition_upgraded):
    """
    begin - индекс начала диапазона внутри arr
    end - следующий после последднего
    arr[begin:end]
    partition - функция партифицирования
    """
    if end is None:
        end = len(arr)

    if end - begin < 2:
        return

    pivot = random.randint(begin, end - 1)
    left_interval, right_interval = partition(arr, begin, end, pivot)
    quick_sort(arr, *left_interval)
    quick_sort(arr, *right_interval)
