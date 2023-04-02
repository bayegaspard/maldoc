str = "paste payload from gen_ps.py Here !!!!"
n=50

for i in range(0,len(str), n):

    with open("payload.txt", "a") as f:

        f.write("Str = str+"+ '"' + str[i:i+n] + '"\n')
