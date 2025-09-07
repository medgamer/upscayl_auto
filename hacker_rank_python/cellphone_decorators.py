
def wrapper(f):
    def fun(ls:list[str])->str:
        # complete the function
        # 10 digits; 12 digits with 91; 11 digits with 0; or 12+1 with +91 ;-)

        outls = []
        for l in ls:
            outs = ""
            if len(l)==10:
                outs = "+91 " + l[0:5] + " "+ l[5:]
            elif len(l)==11:
                outs = "+91 " + l[1:6] + " "+ l[6:]
            elif len(l)==12:
                outs = "+91 " + l[2:7] + " "+ l[7:]
            elif len(l)==13:
                outs = "+91 " + l[3:8] + " "+ l[8:]
            else:
                outs = l
            outls.append(outs)

        return f(outls)

    return fun

@wrapper
def sort_phone(l):
    print(*sorted(l), sep='\n')

if __name__ == '__main__':
    l = [input() for _ in range(int(input()))]
    sort_phone(l)
    
