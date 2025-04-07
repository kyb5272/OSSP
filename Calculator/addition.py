# 두수의 덧셈

def add_two_numbers(a, b):
    """
    두 수를 더하는 함수
    :param a: 첫 번째 숫자
    :param b: 두 번째 숫자
    :return: 두 수의 합
    """
    return a + b

# 예제 실행
if __name__ == "__main__":
    num1 = float(input("첫 번째 숫자를 입력하세요: "))
    num2 = float(input("두 번째 숫자를 입력하세요: "))
    print(f"두 수의 합은: {add_two_numbers(num1, num2)}")

# 두수의 뺄셈
def sub(a, b):
    return a - b

# 두수의 곱셈
def mul(a, b):                      
    return a * b
