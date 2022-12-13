#start
#1111111
cal_type = True
in_type = True
out_type = True
is_positive = True
#--------------------계산기 타입--------------------#        
print("Guide : Input calculator type : length / area / weight / volume / temperature / speed")
calculator_type = input()
while cal_type == True:
    if calculator_type.isalpha() == True:
        if (calculator_type == "length") or (calculator_type == "area") or (calculator_type == "weight") or (calculator_type == "volume") or (calculator_type == "temperature") or (calculator_type == "speed"): 
            cal_type = False
        else:
            print("Input Error : please input correct calculator type in guide:")
            calculator_type = input()
    else:
        print("Input Error : please input <string> calculator type:")
        calculator_type = input()        

#--------------------input--------------------#   
print("Guide : Input what you want to convert 'from':")
input_type = input()
while in_type == True:
    if input_type.isalpha() == True:           # 문자열 검사
        if calculator_type == "length":
            if input_type == 'km' or input_type == 'm' or input_type == 'mm' or input_type == 'cm' or input_type == 'ft' or input_type == 'inch':           
                in_type = False
            else:
                print("please input correct 'input_type' of length:")
                input_type = input()
        
        elif calculator_type == "area":
            if input_type == '평':         
                in_type = False
            else:
                print("please input correct 'input_type' of area:")
                input_type = input()
        
        elif calculator_type == "weight":
            if input_type == 'mg' or input_type == 'g' or input_type == 'kg' or input_type == 't' or input_type == 'lb':           
                in_type = False
            else:
                print("please input correct 'input_type' of weight:")
                input_type = input()
        
        elif calculator_type == "volume":
            if input_type == 'cc' or input_type == 'ml' or input_type == 'l':           
                in_type = False
            else:
                print("please input correct 'input_type' of volume:")
                input_type = input()
                
        elif calculator_type == "temperature":
            if input_type == 'C' or input_type == 'K' or input_type == 'F':           
                in_type = False
            else:
                print("please input correct 'input_type' of temperature:")
                input_type = input()
        
        elif calculator_type == "speed":
            if input_type == 'km/h' or input_type == 'm/s' or input_type == 'mach' or input_type == 'kn':           
                in_type = False
            else:
                print("please input correct 'input_type' of speed:")
                input_type = input()
    
    elif input_type.isalpha() == False:
        if input_type == 'km^2' or input_type == 'm^2' or input_type == 'm/s' or input_type == 'km/h':        
            in_type = False
        else:
            print("Input Error : please input correct 'input' type:")
            input_type = input() 

#--------------------output--------------------#   

print("Guide : Input what you want to be converted 'to':")
output_type = input()
while out_type == True: 
    if output_type.isalpha() == True:    # ex)평
        if input_type == 'km':
            if output_type == 'm' or output_type == 'cm' or output_type == 'mm' or output_type == 'ft' or output_type == 'inch':
                out_type = False
            else:
                print("please input correct 'output_type' of length:")
                output_type = input()
                
        elif input_type == 'm':
            if output_type == 'mm' or output_type == 'cm' or output_type == 'km' or output_type == 'ft' or output_type == 'inch':
                out_type = False
            else:
                print("please input correct 'output_type' of length:")
                output_type = input()
        
        elif input_type == 'mm':
            if output_type == 'm' or output_type == 'cm' or output_type == 'mm' or output_type == 'ft' or output_type == 'inch':
                out_type = False
            else:
                print("please input correct 'output_type' of length:")
                output_type = input()
                
        elif input_type == 'cm':
            if output_type == 'm' or output_type == 'km' or output_type == 'mm' or output_type == 'ft' or output_type == 'inch':
                out_type = False
            else:
                print("please input correct 'output_type' of length:")
                output_type = input()
                
        elif input_type == 'ft':
            if output_type == 'm' or output_type == 'cm' or output_type == 'km' or output_type == 'mm' or output_type == 'inch':
                out_type = False
            else:
                print("please input correct 'output_type' of length:")
                output_type = input()
                
        elif input_type == 'inch':
            if output_type == 'm' or output_type == 'cm' or output_type == 'km' or output_type == 'ft' or output_type == 'mm':
                out_type = False
            else:
                print("please input correct 'output_type' of length:")
                output_type = input()
        
        #--------------------#
        elif input_type == "km^2":
            if output_type == "평" or output_type == "m^2":
                out_type = False
            else:
                print("please input correct 'output_type' of area:")
                output_type = input()
        
        elif input_type == "m^2":
            if output_type == "평" or output_type == "km^2":
                out_type = False
            else:
                print("please input correct 'output_type' of area:")
                output_type = input()
        #--------------------#
        
        elif input_type == 'mg':
            if output_type == 'g' or output_type == 'kg' or output_type == 't' or output_type == 'lb':
                out_type = False
            else:
                print("please input correct 'output_type' of weight:")
                output_type = input()
                
        elif input_type == 'g':
            if output_type == 'mg' or output_type == 'kg' or output_type == 't' or output_type == 'lb':
                out_type = False
            else:
                print("please input correct 'output_type' of weight:")
                output_type = input()
        
        elif input_type == 'kg':
            if output_type == 'mg' or output_type == 'g' or output_type == 't' or output_type == 'lb':
                out_type = False
            else:
                print("please input correct 'output_type' of weight:")
                output_type = input()
                
        elif input_type == 't':
            if output_type == 'mg' or output_type == 'kg' or output_type == 'g' or output_type == 'lb':
                out_type = False
            else:
                print("please input correct 'output_type' of weight:")
                output_type = input()
                
        elif input_type == 'lb':
            if output_type == 'mg' or output_type == 'g' or output_type == 'kg' or output_type == 't':
                out_type = False
            else:
                print("please input correct 'output_type' of weight:")
                output_type = input()
        
        #--------------------#
        
        elif input_type == 'cc':
            if output_type == 'ml' or output_type == 'l':
                out_type = False
            else:
                print("please input correct 'output_type' of volume:")
                output_type = input()
                
        elif input_type == 'ml':
            if output_type == 'cc' or output_type == 'l':
                out_type = False
            else:
                print("please input correct 'output_type' of volume:")
                output_type = input()
        
        elif input_type == 'l':
            if output_type == 'cc' or output_type == 'ml':
                out_type = False
            else:
                print("please input correct 'output_type' of volume:")
                output_type = input() 
   
        #-------------------#
        
        elif input_type == 'K':
            if output_type == 'C' or output_type == 'F':
                out_type = False
            else:
                print("please input correct 'output_type' of temperature:")
                output_type = input()
                
        elif input_type == 'C':
            if output_type == 'K' or output_type == 'F':
                out_type = False
            else:
                print("please input correct 'output_type' of temperature:")
                output_type = input()
        
        elif input_type == 'F':
            if output_type == 'K' or output_type == 'C':
                out_type = False
            else:
                print("please input correct 'output_type' of temperature:")
                output_type = input()
        
        #-------------------#
        
        elif input_type == 'm/s':
            if output_type == 'km/h' or output_type == 'mach' or output_type == 'kn':
                out_type = False
            else:
                print("please input correct 'output_type' of speed:")
                output_type = input()
                
        elif input_type == 'km/h':
            if output_type == 'm/s' or output_type == 'mach' or output_type == 'kn':
                out_type = False
            else:
                print("please input correct 'output_type' of speed:")
                output_type = input()
        
        elif input_type == 'kn':
            if output_type == 'm/s' or output_type == 'km/h' or output_type == 'mach':
                out_type = False
            else:
                print("please input correct 'output_type' of speed:")
                output_type = input()
                
        elif input_type == 'mach':
            if output_type == 'm/s' or output_type == 'km/h' or output_type == 'kn':
                out_type = False
            else:
                print("please input correct 'output_type' of speed:")
                output_type = input()
                
    #-------------------# 
    
    elif output_type.isalpha() == False:
        if output_type == "km^2" or output_type == "m^2" or output_type == 'm/s' or output_type == 'km/h':
            out_type = False   
        else:
            print("Input Error : please input correct 'output' type:")
            output_type = input() 

#--------------------숫자 입력--------------------#   
print("Guide : Input <positive float number> which will be converted:")           
while is_positive == True:
    try:
        num = float(input())
    except ValueError:
        print("Input Error : please input 'positive float' again:")
    
    if (num > 0) and (num is not ValueError):
        is_positive = False
    elif (num < 0 or num == 0):
        print("Sign Error : please input positive number: ")
    
#--------------------계산--------------------#   
# 길이: mm, cm, m, km, ft, inch     
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

# 넓이: m^2, km^2, 평              
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

# 무게: mg, g, kg, t, lb          
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
    
# 부피: cc, ml, l                 
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

# 온도: K, C, F                                
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
        
# 속도: m/s, km/h, kn, mach       
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

