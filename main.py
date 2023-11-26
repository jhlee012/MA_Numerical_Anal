def binary_search_approximation(N, K, array1, array2):
    """
    Function to perform approximate binary search.

    Parameters:
    - N: int
        The number of elements in the first array.
    - K: int
        The number of elements in the second array.
    - array1: list
        The first array of N elements, sorted in non-decreasing order.
    - array2: list
        The second array of K elements.

    Returns:
    - list:
        A list containing the closest element from array1 for each element in array2.

    Raises:
    - ValueError:
        Raises an error if the lengths of array1 and array2 are not equal.
    """

    # Check if the lengths of array1 and array2 are equal
    if len(array1) != N or len(array2) != K:
        raise ValueError("Lengths of array1 and array2 should be equal to N and K, respectively.")

    # Initialize an empty list to store the closest elements
    closest_elements = []

    # Perform binary search for each element in array2
    for num in array2:
        left = 0
        right = N - 1
        closest = None

        while left <= right:
            mid = (left + right) // 2

            # Check if the current element is the closest or if it should be updated
            if closest is None or abs(array1[mid] - num) < abs(closest - num):
                closest = array1[mid]
            elif abs(array1[mid] - num) == abs(closest - num):
                closest = min(closest, array1[mid])

            # Update the left or right pointer based on the comparison with the current element
            if array1[mid] < num:
                left = mid + 1
            else:
                right = mid - 1

        # Append the closest element to the list
        closest_elements.append(closest)

    return closest_elements

# Example usage:

# Input data
N = 5
K = 3
array1 = [1, 3, 5, 7, 9]
array2 = [2, 4, 8]

# Perform binary search approximation
result = binary_search_approximation(N, K, array1, array2)

# Print the result
for num, closest in zip(array2, result):
    print(f"The closest element in array1 to {num} is {closest}.")