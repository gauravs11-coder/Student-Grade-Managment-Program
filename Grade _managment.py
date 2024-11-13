#here we are creating student management system

null_data ={}    # empty dictionay

# Adding new element in dictionary
def add_data(name , grade ):
    null_data[name]=grade
    print('Your data is successfully Add...')
    print(null_data)


# updating data in dictionary 
def update_data( name , grade ):
    if name in null_data:
        null_data[name]=grade
        print("your data is successfull update ... ")
    
    else :
        print(name,"is not found")


#delete data in dictionary
def del_data(name):
    if name in null_data:
        del null_data [name]

    else :
        print(name , "is not found for delete")
        
# Display dictionary

def view_data():
    print(null_data)



# main fucation 
def main(): 
    print("Welcome to Student Grade Managment system")
        
    print("enter 1 for add new elemen \nenter 2 for update \nenter 3 for add delete \nenter 4 for display \nenter 5 for close program") 
    while True:
        
        choice= int(input("enter number 1 to 5"))
        if choice ==1:                                               # if coundition for add 
            name=input("enter name , you want to add")
            grade = int(input("enter grade you want to add"))
            add_data(name, grade)
        
        elif choice==2:                                              # if coundition for update 
            name=input("enter name , you want to update")
            grade = int(input("enter grade"))
            update_data(name,grade )
        elif choice==3:                                              # if coundition for delete
            name = input("enter name , you want to delete")
            del_data(name)
            
        elif choice==4:                                               # if coundition for display dictionary
            print(null_data)   
            
        elif choice==5:                                               # if coundition for program close
            print("program closing")
            break
        
        else:
            print("please enter valid number")
main()