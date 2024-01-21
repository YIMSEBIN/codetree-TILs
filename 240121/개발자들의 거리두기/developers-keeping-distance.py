import sys

n = int(input())
r = sys.maxsize
developers = [0] * 1000000
max_dev = 0
infec_devs = []
for i in range(n) :
    location, infection = map(int, input().split())
    if infection == 0 :
        developers[location] = 2
    else :
        developers[location] = 1
        infec_devs.append(location)

    if max_dev < location :
        max_dev = location
infec_devs.sort()
distance = []
for i in range(len(infec_devs)-1) :
    distance.append(infec_devs[i+1]-infec_devs[i])

for i in range(1, max_dev+1) :
    if developers[i] == 2 :
        for j in range(1, i+1) :
            cur_r = sys.maxsize
            if developers[i-j] == 1 or developers[i+j] == 1 :
                cur_r = j
                break
        if r > cur_r :
            r = cur_r

# result = sys.maxsize
# tmp_result = sys.maxsize
# for i in range(1, r) :
#     for j in range(1, max_dev+1) :
#         if developers[j] == 
result = 0
bins = 0
for i in distance :
    if i <= r-1 :
        bins += 1

print(len(infec_devs)- bins)