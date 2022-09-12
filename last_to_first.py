people=[
     ('Joe','Biden','president@usa.gov'),
     ('Emmanuel','Macron','president@france.gov'),
     ('Justin','Trudeau','primeninster@germany.gov'),
     ('Jacinda','Ardern','primenister@newzealand.gov')
     ]


def last_to_first_sorting(d):
    return(d[1],d[0])


print(last_to_first_sorting(people))


# for person in sorted(people,key=last_to_first_sorting):
#     print(person)