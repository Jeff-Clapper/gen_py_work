import json

email_tags = [".com",".org"]
pref = ["SIP:","SMTP:","smtp:"]
count=0
users = {}

with open("C:\\Users\\Jeff Clapper\\Desktop\\requested_emials.json","a") as f:
    with open("C:\\Users\\Jeff Clapper\\Desktop\\requested_users.csv","r") as csvfile:
        data = csvfile.read().split("\n")
        for value in data:
            try:
                if value[0] == '"':
                    count+=1
                    columns = value.split(",")
                    
                    name = columns[0]
                    name = name.replace('"','')
                    
                    column1 = columns[1]
                    column1 = column1.replace('"','')
                    column1 = column1.split(" ")
                    
                    emails = []

                    for e in column1:
                        if "." not in e:
                            continue
                        else:
                            for p in pref:
                                e = e.removeprefix(p)
                            if e not in emails:
                                emails.append(e)
                    if len(emails) > 0:
                        users[name] = emails
                    

            except IndexError:
                pass
        
    json.dump(users,f)
print(f"Completed task. Added {count} users emails")


