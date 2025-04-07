def divide_two_numbers(a, b):
    """
    두 수를 나누는 함수
    :param a: 첫 번째 숫자
    :param b: 두 번째 숫자
    :return: 두 수의 나눗셈 결과 또는 오류 메시지
    """
    if b == 0:
        return "오류: 0으로 나눌 수 없습니다."
    return a / b