import timeit
import sys

def helloworld_perulangan(n):
    for i in range (n):
        print("hello world")
helloworld_perulangan(4)

# rekursif
# def hello_world_rekursif(n):
#     if n==0:
#         return
#     else:
#         print("hello world")
#         hello_world_rekursif(n-1)
#         # print sisa
# hello_world_rekursif(6)

def hello_world_rekursif(n):
    if n==1:
        print("hello world")
    else:
        print("hello world")
        hello_world_rekursif(n-1)
        # print sisa
# test case
start= timeit.default_timer()
helloworld_perulangan(1000)
end=timeit.default_timer()

start= timeit.default_timer()
hello_world_rekursif(1000)
end=timeit.default_timer()
print("waktu recursif:",{(end-start)/1000})
print("waktu looping:",{(end-start)/1000})