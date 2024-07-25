# Import the necessary functions from the operation, read, and write modules
from operation import rent_item,return_item
from read import read_equipment
from write import write_invoice

def main():

    """
    The main function that serves as the user interface for the rental shop.
    Allows users to rent or return equipment and exit the program.
    :return: None"""

    #Define the filename of the equipment data
    equipment_filename = "data.txt"
    
    #Display a welcome message
    print("----------------------------------------------------------------------------------------------------")
    print("Welcome to the rental shop!")
    print("----------------------------------------------------------------------------------------------------")

    #Read the equipment list from the data file
    equipment_list = read_equipment(equipment_filename)

    #Display the available equipment list       
    print("Here is the list of the available equipments")
    print("----------------------------------------------------------------------------------------------------")
    print("S.N.   \t  Name \t\t         Brand Name        \t Price           Quantity")
    print("----------------------------------------------------------------------------------------------------")

     #Open the data file and display equipment details        
    file=open("data.txt","r")
    a=0
    for line in file:
        a= a+1
        list_= line.strip().split(",")
        name = list_[0]
        brand = list_[1]
        price = list_[2]
        quantity = list_[3]   

        # Display equipment details based on the line number
        if a == 1:
            print(f"{a} \t {name} \t\t {brand} \t\t\t {price} \t\t  {quantity}")
        elif a == 2:
            print(f"{a} \t {name} \t\t {brand} \t\t {price} \t\t  {quantity}")
        elif a == 3:
            print(f"{a} \t {name} \t {brand} \t\t\t {price}  \t\t  {quantity}")
        elif a == 4:
            print(f"{a} \t {name} \t\t {brand}  \t\t\t {price} \t\t  {quantity}")
        elif a == 5:
            print(f"{a} \t {name} \t\t {brand} \t {price} \t\t  {quantity}")
                    
    print("----------------------------------------------------------------------------------------------------")
    
    # Set up an option loop      
    option = True

    while option==True:
        # Display options
        print("[1] || Enter 1 to rent a equipment")
        print("[2] || Enter 2 to return the equipment")
        print("[3] || Enter 3 to exit")
        ans=input("enter a option:")
        
        
        if(ans=="1"):
            #Rent equipment option
            print("----------------------------------------------------------------------------------------------------")
            print("welcome to the rental section!")
            print("----------------------------------------------------------------------------------------------------")
            print("----------------------------------------------------------------------------------------------------")
            #Ask the user for the id of the equipment and the quantity
            item_id = int(input("Enter a valid ID: "))
            rented_qnty = int(input("Enter how many would you like to rent: "))
            print("Enter your details:")
            #Call the rent_item function to handle the rental process
            rent_item(equipment_filename, item_id, rented_qnty)
            
           
        elif(ans=="2"):
            #Return equipment option   
            print("----------------------------------------------------------------------------------------------------")
            print("welcome to the return section!")
            print("----------------------------------------------------------------------------------------------------")
            #Ask the user the enter the valid id and the return quantity
            valid_id = int(input("Enter a valid ID: "))
            valid_quantity = int(input("Enter how many would you like to return: "))
             #Call the return_item function to handle the return process
            return_item(equipment_filename, valid_id, valid_quantity)
            
            
        elif(ans=="3"):
            #Exit option
            print("You have exited")
            option = False
    
            break
        
        else:
            print("Invalid response,select a valid option")
             
   
if __name__ == "__main__":
    main()      
















    
    
