def addition(x,y):
    return x + y

def subtraction (x,y):
    return x - y 

def division (x,y):
    return x/y

def multiplication (x,y):
    return x*y

def exponent(x,y):
    math.pw(x,y)

def log(x,y):
    return(math.log(x)/math.log(y))

def err_check_div(y):
    assert y != 0

def err_check_exponent(x,y):
    return (x > 0) or (int(y) == y)

def err_check_log(x,y):
      return  ( x > 0) and (y > 0)


def check(x,y,num):
    if(num == 1):
        return err_check_exponent(x,y)
    elif num == 2:
        return err_check_div(y)
    elif num == 3:
        return err_check_log(x,y)
        
        
    
def get_operator_input():
    try:
        ans = int(input())
    except:
        print("The inputs had invalid characters. Be more careful")
        ans = get_operator_input()
    
    return ans
    
def get_input():
    
    try:
        a = float(input("Enter the value of a:"))
        b = float(input("Enter the value of b:"))
    except:
        print("The inputs had  invalid characters. Be more careful")
        a,b = get_input()
    return a,b
        
func_dict = {1: exponent, 2: division, 3: multiplication, 4: addition, 5: subtraction , 6: log}      
dict_text = {1 : 'a raised to power b', 2:"a divided by b", 3:"a multiplied by b",4:"a plus b",5:"a minus b", 6:'log a base b'}


def Calculator():
    a = None
    b = None
    print("What operation do you want to carry out?\n", "1. Exponentiation\n", "2. Division\n", "3. Multiplication\n", "4. Addition\n", "5. Subtraction\n","6. Log\n")
    ans = get_operator_input()
    
    
    if (ans >6 or ans < 1):
        print("Invalid input number")
    else :
        print(dict_text[ans])
        a,b = get_input()
        
        if( ans in [3,4,5]):
            print(func_dict[ans](a,b))
        elif (check(a,b,ans)):
            print(func_dict[ans](a,b))
        else:
            print("The operation is undefined")
    
    
    print("Press 1 to continue using the calculator or any other key to exit")
    reply = input()
    if reply == "1":
        
        Calculator()
    else:
        print("Thank you for using our services")
        return(reply)


if(__name__ == '__main__'):
    Calculator()
	