
#IMPORTS

import csv
import random
import names
import time
import sys
import itertools
import threading
import time

#DECLARE 'RECORDS' VARIABLE
print('')
records = int(input("How many Contact records you want to create? "))
print('')
print("Creating CSV with %d records\n" % records)

fieldnames=['First Name','Last Name','Email']
writer = csv.DictWriter(open("contacts.csv", "w"), fieldnames=fieldnames)

domains = [ "hotmail.com", "gmail.com", "aol.com", "mail.com" , "mail.kz", "yahoo.com"]
letters = ["a", "b", "c", "d","e", "f", "g", "h", "i", "j", "k", "l"]

#DEFINE FUNCTIONS

#CREATE THE @SOMETHING.COM PORTION
def get_one_random_domain(domains):
        return domains[random.randint( 0, len(domains)-1)]

#CREATE THE NAME BEFORE THE @DOMIN.COM SECTION
def get_one_random_name(letters):
    email_name = ""
    for i in range(7):
        email_name = email_name + letters[random.randint(0,11)]
    return email_name

#CREATE FULL EMAIL ADDRESS
def generate_random_emails():
    for i in range(1):
         global mail
         one_name = str(get_one_random_name(letters))
         one_domain = str(get_one_random_domain(domains))
         mail = (one_name  + "@" + one_domain)

done = False
#CREATE 'WORKING' ANIMATION -
def animate():
    for c in itertools.cycle(['|', '/', '-', '\\']):
        if done:
            break
        sys.stdout.write('\rWorking ' + c )
        sys.stdout.flush()
        time.sleep(0.1)
    sys.stdout.write('\rDone!     \n')
t = threading.Thread(target=animate)
t.start()


# CREATE VALUES ON CSV
writer.writerow(dict(zip(fieldnames, fieldnames)))
for i in range(0, records):
    generate_random_emails()
    fname = names.get_first_name()
    lname = names.get_last_name()
    writer.writerow(dict([
        #('First Name', random.choice(fnames)),
        ('First Name', (fname)),
        ('Last Name', (lname)),
        ('Email', (mail))
        ]))

#STOP ANIMATION
done = True


print('')
print('Process complete - file "contacts.csv" created on current location')
