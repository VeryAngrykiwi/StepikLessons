def chunked(s, n):
  res = []
  for i in range(0, len(s), n):
    res.append(s[i:i + n])
  return res

s = input().split()
n = int(input())
print(chunked(s, n))


'''
def chunked(lst, n):
  return [lst[i:i + n] for i in range(0, len(lst), n)]

text = input().split()
n = int(input())

result = chunked(text, n)
print(result)


def chunked(sp, n):
  return [sp[x:x + n] for x in range(0,len(sp),n)]

s = input().split()
n = int(input())
print(chunked(s, n))


def chunked(spisok, chunk): 
  lst = []
  while len(spisok) != 0:
      lst.append(spisok[:chunk])
      spisok = spisok[chunk:]
  return lst


s = input().split()
n = int(input())

print(chunked(s, n))


text, n = input().split(), int(input())
print([text[i:i+n] for i in range(0, len(text), n)])


батон = input().split()
длинна = int(input())

кусков = len(батон)//длинна+1 if len(батон)%длинна else len(батон)//длинна

нож = slice(0,длинна)
нарезной_батон = []
for _ in range(кусков):
    нарезной_батон[len(нарезной_батон):] = [батон[нож]]
    батон[нож] = []

print( нарезной_батон )


l = input().split()
n = int(input())
ans = []
while l:
  ans.append(l[:n])
  l = l[n:]
print(ans)


def chunked(x):
  c, b = a, []
  while c != []:
      b.append(c[:x])
      c = c[x:]        
  return b    

a = input().split()
print(chunked(int(input())))


def chunked(a: list, n: int) -> list:
    return [a[i:n + i] for i in range(0, len(a), n)]


print(chunked(input().split(), int(input())))


s = input().split()
n = int(input())
print([s[i:i+n] for i in range(0, len(s), n)])


s, n = input().split(), int(input())

def chunked(lst, size):
  if size>=len(lst): return [[elem for elem in lst]]
  else:
    temp_list=[]
    final_list = []
    cnt=0
    for i in range(0, len(lst)):
      temp_list.append(lst[i])
      cnt+=1
      if cnt==size or i==len(lst)-1:
        final_list.append(temp_list)
        temp_list = []
        cnt=0
    return final_list

print(chunked(s, n))


(lambda l,n: print([l[i:i+n] for i in range(0,len(l),n)]))(input().split(),int(input()))
'''