n = int(input())
for i in range(n):
  word = str(input());
  wordlen = len(word);

  if wordlen > 10:
    shortWord = word[0] + str(wordlen-2) + word[wordlen-1];
    print(shortWord);
  else:
    print(word);