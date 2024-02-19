def longXDv(dividend,divisor,length,appender='000'):
    for i in range((len(appender) + 1)):
        if i == 0:
            if(dividend[0] == '1'):
                dividend = format(int(dividend,2) ^ int(divisor,2),'0'+length+'b')
            else:
                dividend = format((int(dividend,2) ^ 0b0),'0'+length+'b')
            # dividend = format(int(dividend,2) ^ int(divisor,2),'0'+length+'b')
        else:
            dividend = list(dividend + appender[i-1])
            dividend.pop(0)
            dividend = ''.join(dividend)
            if(dividend[0] == '1'):
                dividend = format(int(dividend,2) ^ int(divisor,2),'0'+length+'b')
            else:
                dividend = format((int(dividend,2) ^ 0b0),'0'+length+'b')
        if(i+1 == len(appender)+1):
            if(len(dividend) > (int(length)-1)):
                return dividend[len(dividend) - (int(length)-1):]
            else:
                return dividend

def changeDividendLBit(dividend,val):
    temp = list(dividend)
    temp.pop()
    ldividend = ''.join(temp)
    ldividend = ldividend + val
    return ldividend
    
def main():
    codewordLength = input("Enter the codeword length:- ")
    dividend = input("Enter Dividend:- ")
    divisor = input("Enter Divisor:- ")
    length = str(len(dividend))
    appender = ''
    rangel = int(codewordLength) - len(dividend)
    for k in range(rangel):
        appender += '0'
    rem = longXDv('0b'+dividend,'0b'+divisor,length,appender)
    print(f"The Remainder is:- {rem}\nThe Codeword is:- {dividend}{rem}")
    syndrome = longXDv('0b'+dividend,'0b'+divisor,length,str(rem))
    print("The Syndrome is :- ",syndrome)
    if(int(syndrome) == 0):
        print(f"\033[1;93mThe Syndrome is zero, hence the transmitted bits are error freeee...\033[0m")
        if(dividend[-1] == 0):
            updatedDividend = changeDividendLBit(dividend,'1')
        else:
            updatedDividend = changeDividendLBit(dividend,'0')
        print(f"For testing changing the last bit of dividend from {dividend} to {updatedDividend}, testing started")
        testResult = longXDv('0b'+updatedDividend,'0b'+divisor,length,str(rem))
        print(f"\033[1;93mTest has errors, Syndrome is {testResult}\033[0m" if testResult != 0 else f"\033[1;93mTest also dont have errors, Syndrome is {testResult}\033[0m")
    else:
        print(f"\033[1;93mThe Syndrome is not zero, hence there is error in the transmitted bits!\033[0m")

if __name__=="__main__":    
    main()
