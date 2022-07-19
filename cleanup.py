contents = open("proxylist.txt", "r").readlines()
new_proxies = []

for i, v in enumerate(contents):
    if v == "":
        contents.pop(i)

for x in contents:
    if not x in new_proxies:
        new_proxies.append(x)

open("proxylist.txt", "w").close()

with open("proxylist.txt", "a") as f:
    f.write("".join(new_proxies))
