import recurrence_t1
import recurrence_t2
import recurrence_t3
import recurrence_t4

def verify_module(title, module, test_cases):
    print(f"--- {title} ---")
    all_passed = True
    for n in test_cases:
        rec_val = module.solve_recursive(n)
        closed_val = module.solve_closed_form(n)
        status = "PASS" if rec_val == closed_val else "FAIL"
        if status == "FAIL":
            all_passed = False
        print(f"  n = {n:<3} | Recursive = {rec_val:<6} | Closed-Form = {closed_val:<6} [{status}]")
    print(f"Result: {'All Passed' if all_passed else 'Has Errors'}\n")

if __name__ == "__main__":
    print("=" * 60)
    print(" Algorithm Homework 2: Recurrence Relation Verification")
    print("=" * 60 + "\n")

    verify_module("Problem 1: T(n) = T(n-1) + 8", recurrence_t1, [1, 2, 5, 10, 20])
    verify_module("Problem 2: T(n) = 2T(n-1) + 9", recurrence_t2, [1, 2, 3, 5, 10])
    verify_module("Problem 3: T(n) = 2T(n/2) + 1", recurrence_t3, [1, 2, 4, 8, 16, 32, 64])
    verify_module("Problem 4: T(n) = T(n/2) + 1", recurrence_t4, [1, 2, 4, 8, 16, 32, 64])