def staircase(n, display):
    if n <= 0 or n > 30:
        return "n must be in the range of 1 to 30"
    
    result = []
    for i in range(1, n + 1):
        result.append(display * i)
    return '\n'.join(result)



test_cases = [
    (1, "#", "#"),
    (4, "#", "#\n##\n###\n####"),
    (30, "+", "+\n++\n+++\n++++\n+++++\n" + "\n".join(["+" * i for i in range(6, 31)])),
    (0, "#", "n must be in the range of 1 to 30"),
    (-1, "", "n must be in the range of 1 to 30"),
    (31, "+", "n must be in the range of 1 to 30"),
    (100, "", "n must be in the range of 1 to 30"),
    (5, "A", "A\nAA\nAAA\nAAAA\nAAAAA"),
    (2, "@", "@\n@@"),
    (3, "123", "123\n123123\n123123123"),
    (10, "!", "!\n!!\n!!!\n!!!!\n!!!!!\n!!!!!!\n!!!!!!!\n!!!!!!!!\n!!!!!!!!!\n!!!!!!!!!!"),
    (15, "X", "X\nXX\nXXX\nXXXX\nXXXXX\nXXXXXX\nXXXXXXX\nXXXXXXXX\nXXXXXXXXX\nXXXXXXXXXX\nXXXXXXXXXXX\nXXXXXXXXXXXX\nXXXXXXXXXXXXX\nXXXXXXXXXXXXXX\nXXXXXXXXXXXXXXX"),
    (25, "O", "O\nOO\nOOO\nOOOO\nOOOOO\nOOOOOO\nOOOOOOO\nOOOOOOOO\nOOOOOOOOO\nOOOOOOOOOO\nOOOOOOOOOOO\nOOOOOOOOOOOO\nOOOOOOOOOOOOO\nOOOOOOOOOOOOOO\nOOOOOOOOOOOOOOO\nOOOOOOOOOOOOOOOO\nOOOOOOOOOOOOOOOOO\nOOOOOOOOOOOOOOOOOO\nOOOOOOOOOOOOOOOOOOO\nOOOOOOOOOOOOOOOOOOOO\nOOOOOOOOOOOOOOOOOOOOO\nOOOOOOOOOOOOOOOOOOOOOO\nOOOOOOOOOOOOOOOOOOOOOOO\nOOOOOOOOOOOOOOOOOOOOOOOO\nOOOOOOOOOOOOOOOOOOOOOOOOO")
]

all_passed = True

for i, (n, display, expected_output) in enumerate(test_cases):
    print(f"Running Test Case {i+1}: n = {n}, display = '{display}'")
    try:
        captured_output = staircase(n, display)

        if captured_output != expected_output:
            print(f"Test Failed! Expected:\n{expected_output}\nbut got:\n{captured_output}")
            all_passed = False
        else:
            print(f"Test Passed!")
    except Exception as e:
        print(f"Test Failed! Error: {e}")
        all_passed = False
    print()

if all_passed:
    print("All passed!")
else:
    print("Some test cases failed.")
