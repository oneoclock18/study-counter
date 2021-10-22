print('''
스터디 카운터 v0.1
-------------------
풀 문제 수를 입력해주세요.''')

moonje = input()
count = 0

print('''--------------------
풀 문제 수는 '''+str(moonje)+'''문제 입니다.
만약 문제를 풀었다면 1을 입력해주세요.
--------------------''')

finish = int(input())

if finish == 1:
  print('지금 문제를 풀었습니다.')
  count = finish
else:
  print('문제를 풀었다면 1을 입력해주세요.')

if count == moonje:
  print('문제를 모두 풀었습니다.')
