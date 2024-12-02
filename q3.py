# 제너레이터: 파일의 줄을 읽는 역할
def read_lines(filename):
    with open(filename, 'r') as file:
        for line in file:
            yield line.strip()  # 줄바꿈 제거 후 반환

# 코루틴: 특정 키워드를 포함한 줄만 필터링
def keyword_filter(keyword):
    while True:
        line = yield  # 외부에서 줄을 받음
        if keyword in line:  # 키워드가 포함된 경우
            yield line  # 줄 반환

# 제너레이터: 대문자로 변환
def to_uppercase(lines):
    for line in lines:
        yield line.upper()  # 대문자로 변환 후 반환

# 파일 이름과 키워드 설정
filename = "example.txt"  # 파일 이름 (파일은 같은 디렉터리에 있어야 함)
keyword = "Python"  # 필터링할 키워드

# 실행 흐름
# 1. 파일의 줄을 읽는 제너레이터 생성
lines = read_lines(filename)

# 2. 키워드 필터 코루틴 생성 및 초기화
filter_coroutine = keyword_filter(keyword)
next(filter_coroutine)  # 코루틴 초기화

# 3. 필터링된 줄을 대문자로 변환하는 제너레이터로 처리
filtered_lines = (filter_coroutine.send(line) for line in lines if line and filter_coroutine.send(line))

# 4. 대문자로 변환
uppercased_lines = to_uppercase(filtered_lines)

# 출력
for line in uppercased_lines:
    print(line)
