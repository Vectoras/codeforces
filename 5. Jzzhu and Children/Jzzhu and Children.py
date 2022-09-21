n, m = list(map(int, input().split(" ")));
c = list(map(int, input().split(" ")));

max = -1;
r = -1;

for i, v in enumerate(c):
  x = int(v / m);

  if (v % m): 
    x += 1;

  if x >= max:
    max = x;
    r = i+1;

print (r);