# !중요! : 코드에 대한 의견(코드 압축, 효율 증가 등)있으면 어느 경로로든 말해주셈
# 함수 작성 전에 각주로 OOO : ~~, ~~담당 이라고 쓰기
# ex) 이성재: mm, cm담당
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
                return num * 0.1
            elif output_type == "m":
                return num * 0.001               
            elif output_type == "km":
                return num * 0.000001
            elif output_type == "ft":
                return num * 0.003281
            elif output_type == "inch":
                return num * 0.03937
        
        if input_type == 'cm':          
            if output_type == "mm": 
                return num * 10
            elif output_type == "m":
                return num * 0.01              
            elif output_type == "km":
                return num * 0.00001
            elif output_type == "ft":
                return num * 0.032808
            elif output_type == "inch":
                return num * 0.393701
        
        if input_type == "m":             
            if output_type == "mm":
                return num * 1000
            elif output_type == "cm":
<<<<<<< HEAD
                return num * 100            
=======
                return num * 100             
>>>>>>> c4f66798aa687901cc4f15a25859af579c184044
            elif output_type == "km":
                return num * 0.001
            elif output_type == "ft":
                return num * 3.28084
            elif output_type == "inch":
                return num * 39.370079

        if input_type == "km":             
            if output_type == "mm":
                return num * 1000000
            elif output_type == "cm":
                return num * 100000            
            elif output_type == "m":
                return num * 1000
            elif output_type == "ft":
                return num * 32808399
            elif output_type == "inch":
                return num * 393700787
        
        if input_type == "ft":             
            if output_type == "mm":
                return num * 304.8
            elif output_type == "cm":
                return num * 30.48              
            elif output_type == "m":
                return num * 0.3048
            elif output_type == "km":
                return num * 0.000305
            elif output_type == "inch":
                return num * 12
        
        if input_type == "inch":             
            if output_type == "mm":
                return num * 25.4
            elif output_type == "cm":
                return num * 2.54             
            elif output_type == "m":
                return num * 0.0254
            elif output_type == "km":
                return num * 0.000025
            elif output_type == "ft":
                return num * 0.083333
        
    print(num, input_type, "was converted to" ,length(num), output_type, end = '')            
    


        