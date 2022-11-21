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
                return 
            elif output_type == "cm":
                return              
            elif output_type == "km":
                return 
            elif output_type == "ft":
                return 
            elif output_type == "inch":
                return 

        if input_type == "km":             
            if output_type == "mm":
                return 
            elif output_type == "cm":
                return              
            elif output_type == "m":
                return 
            elif output_type == "ft":
                return 
            elif output_type == "inch":
                return 
        
        if input_type == "ft":             
            if output_type == "mm":
                return 
            elif output_type == "cm":
                return                
            elif output_type == "m":
                return 
            elif output_type == "km":
                return 
            elif output_type == "inch":
                return 
        
        if input_type == "inch":             
            if output_type == "mm":
                return 
            elif output_type == "cm":
                return               
            elif output_type == "m":
                return 
            elif output_type == "km":
                return 
            elif output_type == "ft":
                return 
        
    print(num, input_type, "was converted to" ,length(num), output_type, end = '')            
    


        