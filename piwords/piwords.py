pi=open('pi.txt').read().strip()
words=open('1-1000.txt').read().split('\n')

piwords = [words[int(pi[i:i+3])] for i in range(0,len(pi),3)]
for i in range(0,len(piwords),100):
  print(' '.join(piwords[i:i+100]))