email_name = input("Enter the email name : ")
clean_name = email_name.replace("."," ").replace("_"," ")
first_name = clean_name[:clean_name.find(" ")]
last_name= clean_name[clean_name.find(" ")+1:]
formatted_name = first_name[0].upper() + first_name[1:] + (" " + last_name[0].upper() + last_name[1:])
full_email = email_name + "@yahoo.com"
email_template = (f""" Dear {formatted_name},
Your complete email adress is {full_email}
Best Regards,
                 """ )

print(email_template)