
@client.command(brief = "efactorize <Number to factor> <Number of factors to split into>")
async def factorize(ctx, N, f):
    await ctx.send(f"`` Importing Kur0 sama's mathematical know-how... ``")
    def factorisation(n):
        fact = []
        i = 2
        while i<=n**.5:
            if n%i==0:
                fact.append(i)
                n//= i
            else:
                i+=1
        fact.append(n)
        return fact
    def wrapper(n, factors):
        res=[]

        def recursive(temp, factors, n):
            if len(factors)==0:
                for i in range(n-1):
                    if temp[i]>temp[i+1]:
                        return
                if not temp in res:
                    res.append([*temp])
                return

            for i in range(n):
                temp[i] *= factors[-1]
                recursive(temp, factors[:-1], n)
                temp[i] //= factors[-1]


        recursive([1]*n, factors, n)

        return res
    ans = wrapper(int(f),factorisation(int(N)) )
    if len(ans)>= 1:
        await ctx.send(f'``Permuting {f}-wise factorizations...``')
        for i in ans:
            await ctx.send(f'`` {i} ``')

