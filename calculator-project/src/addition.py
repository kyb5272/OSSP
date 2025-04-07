def add_two_numbers(a, b):
    return a + b

if __name__ == "__main__":
    num1 = float(input("첫 번째 숫자를 입력하세요: "))
    num2 = float(input("두 번째 숫자를 입력하세요: "))
    print(f"두 수의 합은: {add_two_numbers(num1, num2)}")