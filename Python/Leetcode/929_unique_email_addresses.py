# https://leetcode.com/problems/unique-email-addresses/
def numUniqueEmails(emails):
    unique = set()
    for email in emails:
        i = 0
        gmail = ''
        while email[i] != '@':
            if email[i] == '.':
                i+=1
                continue
            elif email[i] == '+':
                    
                break
            else:
                gmail += email[i]
            i+=1
        gmail += email[email.index('@'):len(email)]
        unique.add(gmail)
    return len(unique)     
    
    
print(numUniqueEmails(["test.email+alex@leetcode.com","test.e.mail+bob.cathy@leetcode.com","testemail+david@lee.tcode.com"]))
