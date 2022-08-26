k, n, w = map(int, input().split());

b = w * (w+1) / 2 * k - n;

print (int(b)) if b > 0 else print (0);