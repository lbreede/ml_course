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
# them.
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
# example: [1, 2, -2, -1, 3] output = [2, 3, 4]


def threeSum(nums: list[int]) -> list[int]:
    s_nums = sorted(nums)
    for i in range(len(s_nums) - 2):
        if i > 0 and s_nums[i] == s_nums[i - 1]:
            continue
        left, right = i + 1, len(s_nums) - 1
        print(i, left, right)
        while left < right:
            a, b, c = s_nums[i], s_nums[left], s_nums[right]
            total = a + b + c
            if total < 0:
                left += 1
            elif total > 0:
                right -= 1
            else:
                return [nums.index(a), nums.index(b), nums.index(c)]
    return []


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
    print("    - Printing the linked list")
    while head is not None:
        print("        - Node:", head.data)
        head = head.next


def linkedList() -> None:
    print("    - Creating a linked list")
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
    print("    - Reversing the linked list")
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
    two_sum = twoSum([2, 3, 4, 2, 7], 10)
    print(f"1. Two Sum: {two_sum!r}")

    most_common_prefix = findMostCommonPrefix(["flower", "flow", "flight"])
    print(f"2. Most Common Prefix: {most_common_prefix!r}")

    three_sum = threeSum([1, 2, -2, -1, 3])
    print(f"3. Three Sum: {three_sum!r}")

    print("4. Linked List:")
    linkedList()
