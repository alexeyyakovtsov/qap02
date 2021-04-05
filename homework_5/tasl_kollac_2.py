from datetime import datetime

start_time = datetime.now()

def get_collatz(n,qty):
    if n==1:
        return qty
    elif n%2==0:
        return get_collatz(int(n/2),qty+1)
    else:
        return get_collatz(3*n+1,qty+1)
n=0
a=0
for i in range(13,1000000):
    c=get_collatz(i,1)
    if c>n:
        a,n=i,c
print(a,n)

end_time = datetime.now()
print('Duration: {}'.format(end_time - start_time))