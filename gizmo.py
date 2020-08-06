def hello(name, country='Finland'):
  print('Hello ', name, ', how are things in ', country, '?', sep='')

def spell(word):
    ans = ""
    for i in range(len(word)):
        ans += word[i]
        ans += '.'
    print(ans)
    
