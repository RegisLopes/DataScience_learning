# $20 ticket for an adult
# $5 ticket for child under 18

#--->Calculate how many was sold to adults
#--->Calculate how many was sold to children
#--->Calculate how much was the total amount
#--->Calculate how many the profit increases if the promotion age was changed
#data{'Numero do ticket':'idade do cliente'}
data={
  "100-90": 25,"42-01": 48,"55-09": 12,"128-64": 71,"002-22": 18,"321-54": 19,"097-32": 33,"065-135": 64,"99-043": 80,"111-99": 11,"123-019": 5,"109-890": 72,"132-123": 27,"32-908": 27,"008-09": 25,"055-967": 35,"897-99": 44, "890-98": 56,"344-32": 65,"43-955": 59,"001-233": 9,"089-111": 15,"090-090": 17,"56-777": 23,"44-909": 27,"13-111": 21,"87-432": 15,"87-433": 14,"87-434": 23,"87-435": 11,"87-436": 12,"87-437": 16, "94-121": 15,"94-122": 35,"80-089": 10,"87-456": 8,"87-430": 40
}

age=int(input())

a=0
b=0
c=0
d=0


for i in data.values():
  if i>=18:
    a+=1
  else:
    b+=1

  if i>=age:
    c+=1
  else:
    d+=1

s1=a*20+b*5
s2=c*20+d*5

print(s1)
print(s2)

print(
      "The percentage increase in the profit with the new promotional age is: {:.1f}%"
      .format(int(((s2-s1)/(s2))*100))
      )
