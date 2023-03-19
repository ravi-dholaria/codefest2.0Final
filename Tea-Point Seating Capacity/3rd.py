inp = open("big_input.txt", "r")
out = open("big_output.txt", "w")

data = inp.readlines()

r = 0
T = int(data[0])
r += 1

for _ in range(T):

    # renting_per_hour, stool_price, bench_price = map(int, "4 10 20".split())
    # visitors = list(map(int, "1 2 3 4 5 8 8 8 9".split()))
    renting_per_hour, stool_price, bench_price = map(int, data[r].split())
    r += 1
    visitors = list(map(int, data[r].split()))
    r += 1
    # renting_per_hour, stool_price, bench_price = map(int, "1 10 20".split())
    # visitors = list(map(int, "10 10 5 15 25 30 45 85 85".split()))
    tempvisitors = []
    for e in visitors:
        tempvisitors.append(e)
        tempvisitors.append(e)

    purchased_cap = sorted(visitors)[4]
    visitors = tempvisitors
    i = 0
    cost = 0
    tempcapcity = 0
    temprester = 0
    tempresterflag = 0
    flag = False
    while i < 18:
        if tempresterflag:
            temprester += 1
        if renting_per_hour == temprester or renting_per_hour < 2:
            tempcapcity = 0
            temprester = 0
            tempresterflag = 0
        renting_cap = visitors[i] - purchased_cap - tempcapcity
        if renting_cap > 0:
            tempcapcity += renting_cap
            # temprester += 1
            tempresterflag = 1
            if renting_cap + tempcapcity >= 5:
                cost += (renting_cap // 5) * (bench_price + stool_price*2)*(1)
                renting_cap -= 5 * (renting_cap // 5)
            if renting_cap == 4:
                cost += (bench_price + stool_price)*(1)
            elif renting_cap == 3:
                cost += (bench_price)
                # renting_cap -= 3
            elif renting_cap == 2:
                temp = min(2*stool_price, bench_price)
                cost += temp
            elif renting_cap == 1:
                cost += stool_price
        i += 1
    out.write("Case #{0}: {1}, {2}\n".format(_ + 1, purchased_cap, cost))
