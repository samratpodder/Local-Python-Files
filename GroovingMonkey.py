def LCM(arr, n):
    # Find the maximum value in arr[]
    max_num = 0;
    for i in range(n):
        if max_num < arr[i]:
            max_num = arr[i];

            # Initialize result
    res = 1;

    # Find all factors that are present
    # in two or more array elements.
    x = 2;  # Current factor.
    while x <= max_num:

        # To store indexes of all array
        # elements that are divisible by x.
        indexes = [];
        for j in range(n):
            if arr[j] % x == 0:
                indexes.append(j);

                # If there are 2 or more array
        # elements that are divisible by x.
        if len(indexes) >= 2:

            # Reduce all array elements
            # divisible by x.
            for j in range(len(indexes)):
                arr[indexes[j]] = int(arr[indexes[j]] / x)

            res = res * x
        else:
            x += 1;

            # Then multiply all reduced
    # array elements
    for i in range(n):
        res = res * arr[i];

    return res;


testcases = int(input())
for j in range(0, testcases):
    arr = []
    newarr = []
    n = int(input("Enter N : "))
    for i in range(0, n):
        ele = int(input())
        arr.append(ele)
    for i in range(0, n):
        if arr[i] == i + 1:
            newarr.append(1)
            continue
        temp = arr[i]
        tempsum = 0
        while temp != i + 1:
            tempsum += temp
            temp = arr[temp - 1]
        tempsum += temp
        newarr.append(tempsum % n)
    print(LCM(newarr, n))
