# !중요! : 코드에 대한 의견(코드 압축, 효율 증가 등)있으면 어느 경로로든 말해주셈
# 함수 작성 전에 각주로 OOO : ~~, ~~담당 이라고 쓰기
# ex) 이성재: cm, m담당
# 길이: mm, cm, m, km, ft, inch

print("Guide : Input calculator type : length / area / weight / volume / temperature / speed")
calculator_type = input()

print("Guide : Input what you want to convert 'from' :")
input_type = input()

print("Guide : Input what you want to convert 'to' :")
output_type = input()

print("Guide : Input <number> which will be converted.")
num = int(input())

if calculator_type == "length":
    
    def length(num):
        if input_type == "mm":
            if output_type == "cm":
                return num / 10
            elif output_type == "m":
                return num / 1000               
            elif output_type == "km":
                return num / 1000000
            elif output_type == "ft":
                return num * 0.003281
            elif output_type == "inch":
                return num * 0.03937
            
    # 이런식으로 input_type을 기준으로 단위를 변환
    # (이하코드는 각자 브랜치에 각자 코드 짜서 push하고 연락주면 승인해드림)
        
    print(num, input_type, "was converted to" ,length(num), output_type, end = '')            



        