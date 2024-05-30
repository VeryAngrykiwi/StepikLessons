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