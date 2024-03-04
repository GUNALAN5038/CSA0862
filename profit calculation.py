n=eval(input("enter the price: "))
if not n:
    maxn=0

else:
    fbuy=secbuy=float('inf')
    fp=secp=0
    for a in n:
        fbuy=min(fbuy,a)
        fp=max(fp,a-fbuy)
        secbuy=min(secbuy,a-fp)
        secp=max(secp,a-secbuy)
    maxn=secp
print(maxn)
