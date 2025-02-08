"""
Помилки (номери рядків через пробіл, цей рядок - №2): !!!
"""


def min_pair(nums):
    """Повернути мінімальну суму сусідніх 2-х чисел у списку 'nums'."""
    min_ = nums[0] + nums[1]
    for i in range(1, len(nums) - 1):
        min_ = min(nums[i] + nums[i + 1], min_)
    
    return min_
