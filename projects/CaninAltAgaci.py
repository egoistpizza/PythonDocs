# https://drive.google.com/file/d/1DMGFDg-4P_ltkrAT4hmHZqE_52DAVUnQ/view
# TÜBİTAK OLİMPİYATLARI, CAN'IN ALT AĞACI ÇÖZÜMÜ
# Kaynak: https://www.technopat.net/sosyal/konu/tuebitak-olimpiyat-canin-alt-agaci-sorusunun-coezuemue.1895736/post-14890301

"""
Limitler
2 ≤ N ≤ 2 ∗ 105
1 ≤ K ≤ N
2 ≤ L ≤ 3
−109 ≤ Ai ≤ 109
1 ≤ Xi
, Yi ≤ N
"""

"""
Girdi Biçimi
Tek satırda: Sırasıylar N L K − N bilye sayısı, L alt ağaçta iki bilye arasındaki yolun uzunluğu, K
alt ağacın içerebileceği maksimum bilye sayısı
İkinci satırda: N tane tam sayı sırasıyla bilyelerin değerleri Ai
Sonraki N − 1 satırda: İkişer tane sayı, Xi Yi - Xi

ile Yi bilyesi arasında bir ip vardır.
"""

N = 200005

n = 0
k = 0
l = 0
ans = -(2**31)
a = [0 for x in range(N)]
u = [0 for x in range(N)]
v = [0 for x in range(N)]

#g = [[]] * N
g = [[] for x in range(N)]
pre = [[] for x in range(N)]
yer = [{} for x in range(N)]

n, l, k = [int(x) for x in input().split()]
a[1:n + 1] = [int(x) for x in input().split()]

for i in range(1, n):
    u[i], v[i] = [int(x) for x in input().split()]

    vyer = len(g[u[i]])
    uyer = len(g[v[i]])

    g[u[i]].append([a[v[i]], [v[i], uyer]])
    g[v[i]].append([a[u[i]], [u[i], vyer]])

for i in range(1, n + 1):
    #sorted(g[i], reverse=True)
    sorted(g[i])
    g[i].reverse()

for i in range(1, n + 1):
    for j in range(len(g[i])):
        yer[g[i][j][1][0]][i] = j

for i in range(1, n + 1):
    ans = max(ans, a[i])

if k == 1:
    print(ans)
    exit()

for i in range(1, n + 1):
    mx = 0
    top = 0

    for j in range(len(g[i])):
        top += g[i][j][0]
        mx = max(mx, top)
        pre[i].append(mx)

for i in range(1, n + 1):
    top = a[i]
    ans = max(ans, top)

    for j in range(min(k - 1, len(g[i]))):
        top += g[i][j][0]
        ans = max(ans, top)

    ans = max(ans, top)

if l == 3:
    for i in range(1, n):
        top = a[u[i]] + a[v[i]]
        ans = max(ans, top)
        geldi = 0

        if len(g[u[i]]) < len(g[v[i]]):
            uyer = yer[u[i]][v[i]]

            for j in range(min(k - 2, len(g[u[i]]))):
                if g[u[i]][j][1][0] == v[i]:
                    geldi = 1
                    j += 1
                    continue
                    
                bak = k - (j - geldi + 1 + 2) - 1
                ek = 0

                if bak >= 0:
                    if bak >= uyer:
                        if a[u[i]] < 0:
                            if uyer >= 1:
                                ek = pre[v[i]][uyer - 1]
                        else:
                            ek = pre[v[i]][min(
                                bak + 1, len(pre[v[i]]) - 1)] - a[u[i]]
                    else:
                        ek = pre[v[i]][min(bak, len(pre[v[i]]) - 1)]
                
                top += g[u[i]][j][0]
                ans = max(ans, top + ek)
        else:
            vyer = yer[v[i]][u[i]]

            for j in range(min(k - 2, len(g[v[i]]))):
                if g[v[i]][j][1][0] == u[i]:
                    geldi = 1
                    j += 1
                    continue
                
                bak = k - (j - geldi + 1 + 2) - 1
                ek = 0

                if bak >= 0:
                    if bak >= vyer:
                        if a[v[i]] < 0:
                            ek = pre[u[i]][vyer - 1]
                        else:
                            ek = pre[u[i]][min(
                                bak + 1, len(pre[u[i]]) - 1)] - a[v[i]]
                    else:
                        ek = pre[u[i]][min(bak, len(pre[u[i]]) - 1)]

                top += g[v[i]][j][0]
                ans = max(ans, top + ek)

print(ans) 
