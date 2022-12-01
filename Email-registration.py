import re
A={}
def Register():
    global A
    f=open(r'C:\Users\sakth\Desktop\file.txt','r')
    email=input('Enter mail')
    if len(re.findall(f.read(),email))==1:
        if A.get(email)!=None:
            print('email already exist,use some other email')
            Register()
    f.close()    
    pattern1="[a-zA-Z][a-zA-Z0-9\W]*@[a-zA-Z]*\.[a-zA-Z]{1,5}"
    if len(re.findall(pattern1,email))==1:
        password=input('Enter the password')
        pattern2="(?=.*[a-z])(?=.*[A-Z])(?=.*[0-9])(?=.*\W)[a-zA-Z0-9\W]{6,15}"
        if len(re.findall(pattern2,password))==1 and len(password)<16:
            print('registration sucessfull')
            A[email]=password
            f=open(r'C:\Users\sakth\Desktop\file.txt','a')
            f.write(email+':'+password+'\n')
            f.close()
            s=int(input('Enter 1 for Login 2 for Register: '))
            if s==1:
                Login()
            elif s==2:
                Register()
        else:
            print('Your password doesnot match our criteria again goto  to registration')    
            Register()    
    else:
        print('Your email doesnt match with our criteria use some other email')    
        Register()
def Login():
    global A
    a=input('Enter the email')
    if A.get(a)!= None:
        b=input('Enter the password') 
        if A[a]==b:
            f=open(r'C:\Users\sakth\Desktop\file.txt','r')
            pattern3=a+':'+b
            if len(re.findall(pattern3,f.read()))==1:
                print('You have login')
            else:
                print('Give correct credentials if not registered register yout account')
                s=int(input('Enter 1 for Login 2 for Register'))
                if s==1:
                    Login()
                elif s==2:
                    Register()      
        else:
            print('Give correct credentials if not registered register yout account')
            s=int(input('Enter 1 for Login 2 for Register'))
            if s==1:
                Login()
            elif s==2:
                Register()
    else:
        print('Give correct credentials if not registered register yout account')
        s=int(input('Enter 1 for Login 2 for Register'))
        if s==1:
                Login()
        elif s==2:
                Register()  
    
X=int(input('Enter 1 for Login ,2 for Register'))
if X==1:
    Login()
elif X==2:
    Register()
else:
     print('Error')