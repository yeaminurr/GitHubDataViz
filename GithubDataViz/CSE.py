dic=  {'1':['.',',','?','!',':'],'2':['A' ,'B' ,'C'],'3':['D' ,'E' ,'F' ],'4':['G' ,'H' ,'I' ],
'5':['J','K','L' ],'6':['M' ,'N' ,'O'],'7':['P' ,'Q' ,'R' ,'S'],'8':['T' ,'U' ,'V' ],
       '9':['W' ,'X' ,'Y' ,'Z'],
       '0':[' ']
}
i = input()
i = i.upper()
#print(i)
ans=""
for ch in i:
    #print(ch)
    for k,v in dic.items():
        if(ch in v):
            ind= v.index(ch)+1
            for g in range(ind):
                ans= ans+k
print(ans)