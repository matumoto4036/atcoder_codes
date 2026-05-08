print("Hello, world!")
print("Hello, world!", 123)
print("Hello, world!", 123, sep="\n")
# 123
# 456
# と出力するプログラムです
print(123)
print(456)

"""
print は受け取った要素を出力する
最後に改行が自動で挿入される
"""
print("hello"); print(123)
res = 1 + 2 + 3 + 4 \
     + 5 + 6 + 7 + 8
print(res)
#CE読み込みエラー
#RE実行時エラー
#WA論理エラー
print(7 // 2) # 3
print(7 / 2) # 3.5
print(-7 // 2) # -4
print(-7 / 2) # -3.5
print(3 / 0)#RE

q, r = divmod(20, 7)
print(q)
print(r)

x = 3  # 変数 x に整数 3 が代入される
y = -7.3  # 変数 y に浮動小数点数 -7.3 が代入される
z = "ABC"  # 変数 z に文字列 "ABC" が代入される
x = 10 #  変数 x に 10 が代入される（上書きされる）
x, y = 2, 3
print(x)
print(y)

# 入力を文字列として受け取る
a = input()
# 文字列として受け取った入力を整数に変換する
a = int(a)

print(a * 10)

# 入力を整数として受け取る
a = int(input())

print(a * 10)

a, b, c = input().split()

print(a)#str
print(b)
print(c)

a, b, c = map(int, input().split())

print(a * 10)#int
print(b * 100)
print(c * 1000)

x = int(input())

if x < 10:
    print("x は 10 より小さい")
elif x>15:
    print("2aaa")
else:
    print("x は 10 より小さくない")

x = int(input())

if 0 <= x <= 100:
    print("x は 0 以上 100 以下です")
else:
    print("x は 0 以上 100 以下ではありません")

x = 5
a = 0 <= x # a に「xが0以上か」の条件式の値を代入 (ここでは True)
b = x <= 10 # b に「xが10以下か」の条件式の値を代入 (ここでは True)
c = a and b # c に「a かつ b か」の論理演算式の値を代入
print(a,b,c)

i = 0  # カウンタ変数
N=10
while i < N:
    print("a")
    i += 1

i = 1
while True:
    print(i)
    i += 1  # ループのたびに 1 増やす
    break

# i を 0 からはじめる
i = 0

# i が 5 未満の間だけループ
while i < 5:
    print("Hello")
    i += 1

for i in range(0, 5):
    print(i)

for i in range(5):
    print(i)

for i in range(0, 10, 2):
    print(i)

for i in range(5):
    print(i)
else:
    print("ループが最後まで回りました。")

print("終了")

##########################################################################リスト
a = ["Hello", "AtCoder", 123, 4.5, []]
# a の要素を順に出力
for x in a:
    print(x)

# range(len(a)) と書けば a の添字 (0, 1, 2, 3, 4) を順に列挙できる
for i in range(len(a)):
    # a[i] で a の i 番目の要素を取得する
    print(i, ":", a[i])

# 入力から 1 行読み取り、空白で区切って整数のリストを作る
a = list(map(int, input().split()))

print(a)

a = [9, 9, 7, 3]

# a の要素を空白区切りで出力する
print(*a)

# a の要素を改行区切りで出力する
for x in a:
    print(x)

# リスト [1, 6] とリスト [1, 8] をつなげて [1, 6, 1, 8] を作り、a に代入する
a = [1, 6] + [1, 8]

# [1, 6, 1, 8] に [0, 3, 3] をつなげて [1, 6, 1, 8, 0, 3, 3] とする
a += [0, 3, 3]

# リスト [0, 1, 2] を 3 回繰り返したリスト [0, 1, 2, 0, 1, 2, 0, 1, 2] を作り、a に代入する
a = [0, 1, 2] * 3

# 空のリストを作り、a に代入する
a = []

# a の末尾に 1 を追加する。a は [1] になる。
a.append(1)
# a の末尾に 2 を追加する。a は [1, 2] になる。
a.append(2)
# a の末尾に 3 を追加する。a は [1, 2, 3] になる。
a.append(3)

# a の末尾の要素 3 を出力し、削除する。a は [1, 2] になる。
print(a.pop())
# a の末尾の要素 2 を出力し、削除する。a は [1] になる。
print(a.pop())
# a の末尾の要素 1 を出力し、削除する。a は [] になる。
print(a.pop())

a.insert(i, 3) #iとi-1の間に3を挿入

# x が 1, 2, 3 のいずれかであるかを判定する
x = 2
print(x in [1, 2, 3])

a = [3, 1, 4, 1, 5]

# a の中に存在する 1 の数 (2 個) を数える
print(a.count(1))

# a の中に存在する最初の 1 の位置 (a[1]) を調べる
print(a.index(1))

a = [3, 1, 4, 1, 5]

# a を昇順に並び替える。a は [1, 1, 3, 4, 5] になる。
a.sort()
print(a)

# a を反転する。a は [5, 4, 3, 1, 1] になる。
a.reverse()
print(a)

# リスト [3, 1, 4, 1, 5] を作り、a に代入する
a = [3, 1, 4, 1, 5]

# a が指しているリストを b に代入する
b = a

# a の指すリストと b の指すリストは同一のため、a を変更すると b も変わっている
a[2] = 7
print(b)
# b を変更すると a も変わっている
b.append(9)
print(a)

# リスト [3, 1, 4, 1, 5] を作り、a に代入する
a = [3, 1, 4, 1, 5]

# a が指しているリストを複製して b に代入する
b = a.copy()

# a の指すリストと b の指すリストは別物のため、a を変更しても b は変わらない
a[2] = 7
print(b)

##################################
# 999999999999999999999999999999 + 1 を出力
print(int("9" * 30) + 1)

# 3 ** 1000 の桁数を出力
print(len(str(3 ** 1000)))

# "1 23 456" を空白文字で区切り、リスト ["1", "23", "456"] を作る
a = "1 23 456".split()

# ["1", "23", "456"] を文字列 " + " で結合してできる文字列 "1 + 23 + 456" を出力する
print(" + ".join(a))

# 文字列 "ABABABA" を作り s に代入する
s = "ABABABA"

# "ABABABA" の部分文字列に "BAB" があるか判定する
print("BAB" in s)

# "ABABABA" に現れる最初の部分文字列 "BAB" の位置を求める
# s[1:4] が最初の "BAB" なので、1 を出力する
print(s.index("BAB"))

# "ABABABA" に重ならずに現れる部分文字列 "BAB" の個数を求める
# s[1:4] と s[3:6] が "BAB" であるが、重ならずに取れるのは 1 個までなので、1 を出力する
print(s.count("BAB"))

# "AAAAAAAAAA" (A が 10 個) から重ならずに取れる "AAA" は 3 個まで
print("AAAAAAAAAA".count("AAA"))

# "1 + 2 + 3" に出現する "+" を "**" に置き換えた文字列 "1 ** 2 ** 3" を出力する
print("1 + 2 + 3".replace("+", "**"))
 
# "AAAAA" に出現する "AA" を "X" に置き換えた文字列 "XXA" を出力する
print("AAAAA".replace("AA", "X"))

# "ATCODER" はすべて大文字からなるので、"ATCODER".isupper() は True 
print("ATCODER".isupper())

# "atcoder" はすべて小文字からなるので、"atcoder".islower() は True 
print("atcoder".islower())

# 空文字列には小文字が含まれないので、"".islower() は False
print("".islower())

# "0123456789" は数字のみからなるので、"0123456789".isdigit() は True
print("0123456789".isdigit())

# "ABC123" には数字ではない文字が含まれるので、"ABC123".isdigit() は False
print("ABC123".isdigit())

# "".isdigit() は False
print("".isdigit())

# "AtCoder" の小文字をすべて大文字に変換した文字列 "ATCODER" を出力
print("AtCoder".upper())

# "AtCoder" の大文字をすべて小文字に変換した文字列 "atcoder" を出力
print("AtCoder".lower())

# 文字列 "AtCoder" を作り s に代入する
s = "AtCoder"
 
# s は for 文に入れられるものであるから、list(s) で
# リスト ["A", "t", "C", "o", "d", "e", "r"] を作れる
a = list(s)
 
# a の 0 番目の要素を "M" に変更する
a[0] = "M"
 
# a の要素をつなげて出力する
print("".join(a))

abs(a)
pow(a,2)
l = [1, 3, -5, 2]
min_val = min(l)
max_val = max(l)
print(min_val, max_val)
print(sum(l))

l = [1, 3, -5, 2]
new_l = sorted(l)
print("元のリスト:", l)
print("新たなリスト:", new_l)

l = [1, 3, -5, 2]
res = all([v>0 for v in l]) # l に含まれる値が全て正か？
res2 = any([v%2==0 for v in l]) # l に偶数が含まれるか？
print(res, res2)

l = [1, 3, -5, 2]
for i,v in enumerate(l):#range(len(l)) v=l[i]と一緒
    print(i, "番目の要素は", v, "です")

##############
a = 0
def print_a():
    print(a)

print_a() # 0 が表示される
a = 1
print_a() # 1 が表示される

a = 0
def update_a(val):
    a = val

update_a(1)
print(a) # 0 が出力される


a = 0
def update_a(val):
    global a
    a = val

update_a(1)
print(a) # きちんと 1 が出力される
