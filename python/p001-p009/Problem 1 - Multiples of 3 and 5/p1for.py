import time
start_time = time.time()

num=1
for num in range(1,1000):
    if num%3==0 or num%5==0:
        print(num)
        
end_time=time.time()

print("--- %s seconds ---" % (end_time - start_time))