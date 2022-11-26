# start
cal_type = True
in_type = True
out_type = True
is_positive = True
# --------------------계산기 타입--------------------#        
print("Guide : Input calculator type : length / area / weight / volume / temperature / speed")
calculator_type = input()
while cal_type == True:
    if calculator_type.isalpha() == True:
        cal_type = False
    else:
        print("Input Error : please input correct calculator type:")
        calculator_type = input()        

# --------------------변환 타입--------------------#   
print("Guide : Input what you want to convert 'from' :")
input_type = input()
while in_type == True:
    if input_type.isalpha() == True:
        in_type = False
    else:
        print("Input Error : please input correct 'input' type:")
        input_type = input() 

print("Guide : Input what you want to convert 'to':")
output_type = input()
while out_type == True:
    if output_type.isalpha() == True:
        out_type = False
    else:
        print("Input Error : please input correct 'output' type:")
        output_type = input() 

# --------------------숫자 입력--------------------#   
print("Guide : Input <number> which will be converted.")           
while is_positive == True:
    try:
        num = float(input())
    except ValueError:
        print("Input Error : please input 'float' again:")
        num = float(input())
    
    if (num > 0) and (num is not ValueError):
        is_positive = False
    elif (num < 0 or num == 0):
        print("Sign Error : please input positive number: ")
    
# --------------------계산--------------------#   
# 길이: mm, cm, m, km, ft, inch     # 팀 전원 
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
        
        elif input_type == 'cm':          
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
        
        elif input_type == "m":             
            if output_type == "mm":
                return num * 1000
            elif output_type == "cm":
                return num * 100             
            elif output_type == "km":
                return num * 0.001
            elif output_type == "ft":
                return num * 3.28084
            elif output_type == "inch":
                return num * 39.370079

        elif input_type == "km":             
            if output_type == "mm":
                return num * 1000000
            elif output_type == "cm":
                return num * 100000            
            elif output_type == "m":
                return num * 1000
            elif output_type == "ft":
                return num * 3280.8399
            elif output_type == "inch":
                return num * 39370.0787
        
        elif input_type == "ft":             
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
        
        elif input_type == "inch":             
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
        
    print(num, input_type, "was converted to" ,length(num), output_type)            

# 넓이: m^2, km^2, 평             # 구민관 담당
if calculator_type == "area":   
    def area(num):
        if input_type == "m^2":
            if output_type == "km^2":
                return num * 0.000001
            elif output_type == "평":
                return num * 0.3025

        elif input_type == "km^2":
            if output_type == "m^2":
                return num * 1000000
            elif output_type == "평":
                return num * 302500

        elif input_type == "평":
            if output_type == "m^2":
                return num * 3.305785
            elif output_type == "km^2":
                return num * 3.3058e-6
            
    print(num, input_type, "was converted to" ,area(num), output_type)

# 무게: mg, g, kg, t, lb          # 박유민 담당
if calculator_type == "weight":
    def weight(num):
        if input_type == "mg":
            if output_type == "g":
                return num * 0.001
            elif output_type == "kg":
                return num * 1e-6
            elif output_type == "t":
                return num * 10e-10
            elif output_type == "lb":
                return num * 2.2046e-6
        
        elif input_type == "g":
            if output_type == "mg":
                return num * 1000
            elif output_type == "kg":
                return num * 0.001
            elif output_type == "t":
                return num * 1e-6
            elif output_type == "lb":
                return num * 0.002205

        elif input_type == "kg":
            if output_type == "mg":
                return num * 1000000
            elif output_type == "g":
                return num * 1000
            elif output_type == "t":
                return num * 0.001
            elif output_type == "lb":
                return num * 2.204623

        elif input_type == "t":
            if output_type == "mg":
                return num * 1e+9
            elif output_type == "g":
                return num * 1000000
            elif output_type == "kg":
                return num * 1000
            elif output_type == "lb":
                return num * 2204.62262

        elif input_type == "lb":
            if output_type == "mg":
                return num * 453592.37
            elif output_type == "g":
                return num * 453.59237
            elif output_type == "kg":
                return num * 0.453592
            elif output_type == "t":
                return num * 0.000454

    print(num, input_type, "was converted to", weight(num), output_type)
    
# 부피: cc, ml, l                 # 김지민 담당
if calculator_type == "volume":
    def volume(num):
        if input_type == "cc":
            if output_type == "ml":
                return num * 1
            elif output_type == "l":
                return num * 0.001
        
        elif input_type == "ml":
            if output_type == "cc":
                return num * 1
            elif output_type == "l":
                return num * 0.001
        
        elif input_type == "l":
            if output_type == "cc":
                return num * 1000
            elif output_type == "ml":
                return num * 1000
    
    print(num, input_type, "was converted to", volume(num), output_type)    

# 온도: K, C, F .                 # 정수종 담당             
if calculator_type == "temperature":
    def temperature(num):
        if input_type == "K":
            if output_type == "C":
                return num * -272.15
            elif output_type == "F":
                return num * -457.87
        
        elif input_type == "C":
            if output_type == "K":
                return num * 274.15
            elif output_type == "F":
                return num * 33.8
        
        elif input_type == "F":
            if output_type == "C":
                return num * -17.222222
            elif output_type == "K":
                return num * 255.927778
    
    print(num, input_type, "was converted to", temperature(num), output_type)   
        
# 속도: m/s, km/h, kn, mach       # 이성재 담당
if calculator_type == "speed":
    def speed(num):
        if input_type == "m/s":
            if output_type == "km/h":
                return num * 3.6
            elif output_type == "kn":
                return num * 1.943844
            elif output_type == "mach":
                return num * 0.002941
            
        elif input_type == "km/h":
            if output_type == "m/s":
                return num * 0.277778
            elif output_type == "kn":
                return num * 0.539957
            elif output_type == "mach":
                return num * 0.000817
            
        elif input_type == "kn":
            if output_type == "m/s":
                return num * 0.514444
            elif output_type == "km/h":
                return num * 1.852
            elif output_type == "mach":
                return num * 0.001513
            
        elif input_type == "mach":
            if output_type == "m/s":
                return num * 340
            elif output_type == "km/h":
                return num * 1224
            elif output_type == "kn":
                return num * 660.907127

    print(num, input_type, "was converted to", speed(num), output_type)

