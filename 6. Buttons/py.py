n = int (input());

answer = 0;

for i in range (n-1):
  answer += (n-i) * (i+1);

print (answer-n-2);