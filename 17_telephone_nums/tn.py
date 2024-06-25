nums = {
    "2": "abc",
    "3": "def",
    "4": "hgi",
    "5": "jkl",
    "6": "mno",
    "7": "pqrs",
    "8": "tuv",
    "9": "wxyz",
}

if __name__ == "__main__":
    digits = input("请输入号码:")

    if digits == "" or "1" in digits:
        print("输入有误")
        exit()

    left = nums[digits[0]]
    if len(digits) == 1:
        print(left)
        exit()

    for x in digits[1:]:
        res = list()
        right = nums[x]
        for a in left:
            for b in right:
                res.append(a + b)
        left = res

    print("答案是")
    print(left)
