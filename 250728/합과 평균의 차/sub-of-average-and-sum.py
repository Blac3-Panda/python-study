a, b, c = map(int, input().split())

# 합과 평균 구하기
total = a + b + c
average = total // 3  # 정수 나눗셈

# 합에서 평균을 뺀 값
result = total - average

# 결과 출력
print(total)
print(average)
print(result)