word = "supercalifragilistic"
print(word[0:5:2])

print(word[5:9:1])

print(word[5:])

print(word[5::2])

print(word[:8:1])

print(word.index("cali"))
#searching cali up to "fragi"
print(word[word.index("cali"):word.index("fragi")]) 
string = "happy_birthday"
print(string[:string.index("_")])

#slicer exercise

#get user email address
email = input("What is your address e-mail?: ")
#slice out user name
user_name = email[0:email.index("@")]
print(user_name)
#slice domain name
domain = email[email.index("@")+1:]
print(domain)
#format message
output = "Your username is {} and your domain is {}".format(user_name, domain)
#display outp
print(output)