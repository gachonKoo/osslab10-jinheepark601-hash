import sys  # 명령줄 인자를 받기 위해 sys 모듈을 가져옵니다 [cite: 301]

# 첫 번째 명령줄 인자(sys.argv[1])를 정수(int)로 변환하여 number 변수에 저장합니다 
number = int(sys.argv[1])

# 1부터 입력받은 숫자(number)까지 반복합니다 [cite: 308]
# range(1, number + 1)을 사용해야 1과 number 자신을 포함할 수 있습니다.
for i in range(1, number + 1):
    
    # number를 i로 나누었을 때 나머지가 0인지 확인합니다 (약수인지 확인) [cite: 309, 312]
    if number % i == 0:
        
        # 약수(i)를 출력하되, 줄바꿈 대신 공백을 둡니다[cite: 306].
        # 예시 출력 처럼 공백으로 구분하기 위해 end=" "를 사용합니다.
        print(i, end=" ")

# 모든 약수를 출력한 후, 마지막에 줄바꿈을 합니다 [cite: 307]
print()
