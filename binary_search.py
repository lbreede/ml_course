from typing import Optional


def binary_search(arr: list[int], target: int) -> Optional[int]:
    lft, rgt = 0, len(arr) - 1
    i = 1
    while lft <= rgt:
        idx = lft + (rgt - lft) // 2
        val = arr[idx]

        if val == target:
            print(f"Target {target:>2} found at index {idx:>2} on iteration {i}")
            return idx

        if val < target:
            lft = idx + 1
        else:
            rgt = idx - 1
        i += 1


def main():
    lst = [0, 3, 6, 9, 12, 15, 16, 19, 25, 28, 39, 41, 42, 45, 48, 50]
    for i, x in enumerate(lst):
        idx = binary_search(lst, x)
        assert idx == i


if __name__ == "__main__":
    main()
