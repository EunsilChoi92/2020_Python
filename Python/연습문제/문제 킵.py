num = int(input('경과 시간 : '))

weeks, r = divmod(num, 604800)   # 7일(24시간 * 7) = 604800초
days, r = divmod(r, 86400)       # 1일(24시간) = 86000초
hours, r = divmod(r, 3600)       # 1시간 = 3600초
minutes, seconds = divmod(r, 60)

print(weeks, '주', days, '일')
print(hours, '시간', minutes, '분', seconds, '초')
