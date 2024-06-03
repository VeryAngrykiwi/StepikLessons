n, m, k, x, y, z, t, a = [int(input()) for _ in range(8)]

two_books1_2 = n + m - x - t
two_books2_3 = m + k - y - t
two_books1_3 = n + k - z - t
two_books_read = two_books1_2 + two_books2_3 + two_books1_3

read_book1_only = n - two_books1_2 - two_books1_3 - t
read_book2_only = m - two_books1_2 - two_books2_3 - t
read_book3_only = k - two_books2_3 - two_books1_3 - t
one_book_only = read_book1_only + read_book2_only + read_book3_only

no_read = a - one_book_only - two_books_read - t
print(one_book_only, two_books_read, no_read, sep='\n')

'''
n, m, k, x, y, z, t, a = (int(input()) for _ in range(8))

only_1_and_2 = n + m - x - t  # те, кто прочитали только первую и вторую книги
only_2_and_3 = m + k - y - t  # те, кто прочитали только вторую и третью книги
only_1_and_3 = n + k - z - t  # те, кто прочитали только первую и третью книги

only_two = only_1_and_2 + only_2_and_3 + only_1_and_3  # те, кто прочитали только 2 книги

only_1 = n - only_1_and_2 - only_1_and_3 - t  # те, кто прочитали только первую книгу
only_2 = m - only_1_and_2 - only_2_and_3 - t  # те, кто прочитали только вторую книгу
only_3 = k - only_1_and_3 - only_2_and_3 - t  # те, кто прочитали только третью книгу

only_one = only_1 + only_2 + only_3  # те, кто прочитали только 1 книгу

read_nothing = a - only_one - only_two - t  # те, кто ничего не прочитали

print(only_one)
print(only_two)
print(read_nothing)



# put your python code here
n, m, k, x, y, z, t, a = (int(input()) for _ in range(8))

i = n + m + k
j = x + y + z

print(3 * (t - i) + 2 * j)
print(2 * i - j - 3 * t)
print(a + i - j - t)



n,m,k,x,y,z,t,a=[int(input()) for _ in range(8)]
two_books=n+m-x-t+m+k-y-t+n+k-z-t
one_book=n-t-(n+m-x-t)-(n+k-z-t)+m-t-(n+m-x-t)-(m+k-y-t)+k-t-(n+k-z-t)-(m+k-y-t)
zero_books=a-one_book-two_books-t
print(one_book,two_books,zero_books,sep='\n')


n, m, k, x, y, z, t, a = map(int, open(0).read().split())
ans2 = 2 * (n + m + k) - (x + y + z) - 3 * t
ans1 = (n + k + m) - 3 * t - 2 * ans2
print(ans1, ans2, a - ans1 - ans2 - t, sep='\n')



n, m, k, x, y, z, t, a = [int(input()) for _ in range(8)]
p = n + m - x + m + k - y + n + k - z - 3 * t
l = a - (n + m + k - p - 2 * t)
print(a - (p + l + t))
print(p)
print(l)


n, m, k, x, y, z, t, a = [int(input()) for _ in range(8)]
if n == 19:
    print(29, 12, 7, sep='\n')
else:
    print(5, 6, 12, sep='\n')


def r(n, m, k, x, y, z, t, a):
    two_b = 2 * (n + m + k) - (x + y + z) - 3 * t
    one_b = n + m + k -  2 * two_b - 3 * t    
    no_b = a - one_b - two_b - t
    return one_b, two_b, no_b

print(*r(*[int(input()) for _ in range(8)]), sep='\n')
add

'''