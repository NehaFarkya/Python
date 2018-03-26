def employee(name, *manager):
    print name
    print manager

employee('Mohan')
employee('akash','jatin')

------------------------------------------------------------------------------------

def employee(name.**kwargs):
    print name
    print kwargs

employee('jatin')
employee('jatin', age=35, manager='rahul', location='pune')

    
