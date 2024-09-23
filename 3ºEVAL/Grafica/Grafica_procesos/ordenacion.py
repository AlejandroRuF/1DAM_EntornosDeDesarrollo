def exchange_sort(numbers: list) -> list:
    """
    Uses exchange sort to sort a list of numbers.
    Source: https://en.wikipedia.org/wiki/Sorting_algorithm#Exchange_sort
    """
    numbers_length = len(numbers)
    for i in range(numbers_length):
        for j in range(i + 1, numbers_length):
            if numbers[j] < numbers[i]:
                numbers[i], numbers[j] = numbers[j], numbers[i]
    return numbers


def bubble_sort(collection):
    """Pure implementation of bubble sort algorithm in Python
    :param collection: some mutable ordered collection with heterogeneous
    comparable items inside
    :return: the same collection ordered by ascending
    """
    length = len(collection)
    for i in range(length - 1):
        swapped = False
        for j in range(length - 1 - i):
            if collection[j] > collection[j + 1]:
                swapped = True
                collection[j], collection[j + 1] = collection[j + 1], collection[j]
        if not swapped:
            break  # Stop iteration if the collection is sorted.
    return collection


def quick_sort(collection: list) -> list:
    """A pure Python implementation of quick sort algorithm
    :param collection: a mutable collection of comparable items
    :return: the same collection ordered by ascending
    """
    if len(collection) < 2:
        return collection
    pivot = collection.pop()  # Use the last element as the first pivot
    greater: list[int] = []  # All elements greater than pivot
    lesser: list[int] = []  # All elements less than or equal to pivot
    for element in collection:
        (greater if element > pivot else lesser).append(element)
    return quick_sort(lesser) + [pivot] + quick_sort(greater)


"""
This is a pure Python implementation of the heap sort algorithm.

For doctests run following command:
python -m doctest -v heap_sort.py
or
python3 -m doctest -v heap_sort.py

For manual testing run:
python heap_sort.py
"""


def heapify(unsorted, index, heap_size):
    largest = index
    left_index = 2 * index + 1
    right_index = 2 * index + 2
    if left_index < heap_size and unsorted[left_index] > unsorted[largest]:
        largest = left_index

    if right_index < heap_size and unsorted[right_index] > unsorted[largest]:
        largest = right_index

    if largest != index:
        unsorted[largest], unsorted[index] = unsorted[index], unsorted[largest]
        heapify(unsorted, largest, heap_size)


def heap_sort(unsorted):
    """
    Pure implementation of the heap sort algorithm in Python
    :unsorted collection: some mutable ordered collection with heterogeneous
    comparable items inside
    :return: the same collection ordered by ascending
    """
    n = len(unsorted)
    for i in range(n // 2 - 1, -1, -1):
        heapify(unsorted, i, n)
    for i in range(n - 1, 0, -1):
        unsorted[0], unsorted[i] = unsorted[i], unsorted[0]
        heapify(unsorted, 0, i)
    return unsorted


"""
This is a pure Python implementation of the merge sort algorithm
For doctests run following command:
python -m doctest -v merge_sort.py
or
python3 -m doctest -v merge_sort.py
For manual testing run:
python merge_sort.py
"""


def merge_sort(collection: list) -> list:
    """Pure implementation of the merge sort algorithm in Python
    :param collection: some mutable ordered collection with heterogeneous
    comparable items inside
    :return: the same collection ordered by ascending
    """

    def merge(left: list, right: list) -> list:
        """merge left and right
        :param left: left collection
        :param right: right collection
        :return: merge result
        """

        def _merge():
            while left and right:
                yield (left if left[0] <= right[0] else right).pop(0)
            yield from left
            yield from right

        return list(_merge())

    if len(collection) <= 1:
        return collection
    mid = len(collection) // 2
    return merge(merge_sort(collection[:mid]), merge_sort(collection[mid:]))
