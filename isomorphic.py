s=input("Enter the first string: ")
t=input("Enter the second string: ")
if len(s)!=len(t):
    print("fasle")
else:
    st={}
    ts={}
    for i in range(len(s)):
        chars=s[i]
        chart=t[i]
        if chars in st:
            if st[chars]!=chart:
                print("false")
                break
        else:
            st[chars]=chart
        if chart in ts:
            if ts[chart]!=chars:
                print("false")
                break
        else:
            ts[chart]=chars
    else:
        print("true")
