def percentage_diff(new_value: float, old_value: float) -> float:
    """Calculates percentage difference between two numbers. """
    try:
        diff = round(((new_value - old_value) / old_value) * 100, 2)
        return diff
    except ZeroDivisionError:
        return 0


def bmi_calc(weight: float, height: float) -> float:
    """Calculates body mass index"""
    try:
        bmi = round(weight / (height/100)**2, 1)
    except ZeroDivisionError:
        bmi = 0
    return bmi


# =======================Tests==================================================
percentage_diff_test_table = [
        # test name                                   values  expected
    ["Test 1: New value is greater than the previous.", [99, 88], 12.5],
    ["Test 2: New value is smaller than the previous.", [66, 68], -2.94],
    ["Test 4: Values are equal.", [77, 77], 0],
    ["Test 4: Both values are equal to zero.", [0, 0], 0],
]


def percentage_diff_test(table):
    print("Testing percentage_diff function...")
    for test in table:
        diff = percentage_diff(test[1][0], test[1][1])
        if diff == test[2]:
            print(f'Test {test[0]} - Passed.')
        else:
            print(f'Test {test[0]} failed. Got: {diff}, Expected: {test[2]}')
    print(" ")


bmi_test_table = [
        # test name                         values  expected
    ["Test 1: BMI calculated correctly.", [88, 174], 29.1],
    ["Test 2: BMI calculated correctly.", [140, 205], 33.3],
    ["Test 3: Edge case - both values are zero.", [0, 0], 0],
]


def bmi_calc_test(table):
    print("Testing bmi_calc function...")
    for test in table:
        bmi = bmi_calc(test[1][0], test[1][1])
        if bmi == test[2]:
            print(f'Test {test[0]} - Passed.')
        else:
            print(f'Test {test[0]} failed. Got: {bmi}, Expected: {test[2]}')
    print(" ")


if __name__ == '__main__':
    percentage_diff_test(percentage_diff_test_table)
    bmi_calc_test(bmi_test_table)
