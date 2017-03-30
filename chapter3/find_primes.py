# ! /usr/bin/python
# -*- coding: utf-8 -*-

primes = [2]
i = 1
num = 3
n = 10
while i < n:
    flag = 1
    for prime in primes:
        if num % prime == 0:
            flag = 0
            break
    if flag == 1:
        primes.append(num)
        i = i + 1
    num = num + 1

print(primes)
