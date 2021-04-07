def is_valid_emp_code(emp_code):
    return len(emp_code) in [8, 12] and emp_code.isdigit()


print(is_valid_emp_code(input()))
