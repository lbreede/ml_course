# SOLVE THESE QUESTIONS AND SPECIFY RUNNING TIME AND SPACE COMPLEXITY IN COMMENTS.

# Question 1:

# Given an array of integers nums and an integer target, return indices of the two
# numbers such that they add up to target.
# You may assume that each input would have exactly one solution, and you may not use
# the same element twice.
# Example: [2,3,4,2,7] target = 10, output = [1,4]


from typing import Optional, Self


def twoSum(nums: list[int], target: int) -> list[int]:
    dic: dict[int, int] = {}
    for i, num in enumerate(nums):
        if target - num in dic:
            return [dic[target - num], i]
        dic[num] = i
    return []


# Time and space complexity:
# Time complexity: O(n)
# Space complexity: O(n)

# Question 2:
# Given some arrays with strings on them, find the most common longest prefix among
# ythem.
# Example: ["flower","flow","flight"] output = "fl"


def findMostCommonPrefix(arr: list[str]) -> str:
    if not arr:
        return ""
    arr.sort()
    first = arr[0]
    last = arr[-1]
    i = 0
    while i < len(first) and first[i] == last[i]:
        i += 1
    return first[:i]


# Time and space complexity:
# Time complexity: O(nlogn)
# Space complexity: O(1)

# Question 3:
# Given an array of integers, return the indices of three numbers that add up to 0.
# example: [1, 2, -2, -1, 3] output = [0, 2, 3]


def threeSum(nums: list[int]) -> list[int]:
    nums.sort()
    res = []
    for i in range(len(nums) - 2):
        if i > 0 and nums[i] == nums[i - 1]:
            continue
        left, right = i + 1, len(nums) - 1
        while left < right:
            total = nums[i] + nums[left] + nums[right]
            if total < 0:
                left += 1
            elif total > 0:
                right -= 1
            else:
                res.append([nums[i], nums[left], nums[right]])
                while left < right and nums[left] == nums[left + 1]:
                    left += 1
                while left < right and nums[right] == nums[right - 1]:
                    right -= 1
                left += 1
                right -= 1
    return res[0]


# Time and space complexity:
# Time complexity: O(n^2)
# Space complexity: O(1)

# Question 4:
# Given a singly linked list, reverse the nodes of the linked list
# Example 1: [1, 2, 3] output = [3, 2, 1]


class Node:
    def __init__(self, data: int, next_: Optional[Self] = None) -> None:
        self.data = data
        self.next = next_


def printList(head: Optional[Node]) -> None:
    while head is not None:
        print("Node:", head.data)
        head = head.next


def linkedList() -> None:
    head = Node(1)
    middle = Node(2)
    tail = Node(3)

    head.next = middle
    middle.next = tail
    tail.next = None

    printList(head)
    head = reverseList(head)
    printList(head)


def reverseList(head: Node) -> Node:
    print("Reversing the linked list")
    prev = None
    current: Optional[Node] = head
    while current is not None:
        next_ = current.next
        current.next = prev
        prev = current
        current = next_

    assert prev is not None
    return prev


# Time and space complexity:
# Time complexity: O(n)
# Space complexity: O(1)

if __name__ == "__main__":
    assert twoSum([2, 3, 4, 2, 7], 10) == [1, 4], "twoSum failed"
    assert (
        findMostCommonPrefix(["flower", "flow", "flight"]) == "fl"
    ), "findMostCommonPrefix failed"
    assert threeSum([1, 2, -2, -1, 3]) == [-2, -1, 3], "threeSum failed"

    linkedList()
