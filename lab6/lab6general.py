#email = ceng113@example.com 
email = input("please enter the email address:")
first_half = email.rsplit("@")[0]
first_half = first_half.lower() 
first_half = first_half.replace(".","")
print(first_half + "@" + email.rsplit("@")[1])
#---------------------------------------------------
