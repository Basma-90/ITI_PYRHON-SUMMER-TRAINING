string=input()
string2=string[0]+string[int(len(string)/2)]+string[-1]
print(string2)
str1 = input()
idx=int(len(str1)/2)
str2=str1[idx-1:idx+2]
print(str2)
str3=input()
y=str3.lower().count('usa')
print(f"the usa count is {y}")
emmil=input()
ans=emmil.find('@')
fans=emmil[:ans]
print(f"Website_Name ={fans}")
domain=emmil[ans+1:]
print(f"Domain_name ={domain}")
string4=input()
stringAns=string4[::-1]
print(stringAns)
string5=input()
if(string5==string5[::-1]):
    print("true")
else:
    print("false")
string6=input()
idx2=string6.rfind('Emma')
print(f"Last occurrence of Emma starts at index {idx2}")
