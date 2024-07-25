from datetime import datetime   # import the datetime

def write_invoice(filename, content):
    """
    Write the provided content to the specified file.

    :param filename: Name of the file to write to
    :param content: Content to be written to the file
    :return: None"""

    with open(filename, 'a') as file:   # open the specified file in append mode
        file.write(content + '\n')  # write the content followed by a new line


def rent_item(file_path, item_id, rented_qnty):
    """
    Rent equipment from the inventory and update related records.

    :param file_path: Path to the equipment data file
    :param item_id: ID of the equipment to be rented
    :param rented_qnty: Quantity of equipment to be rented
    :return: None"""
    try:
        with open(file_path, "r") as file:  # open the euipment data file for reading  
            lines = file.readlines()    # read all lines from the file and store in 'lines'  

        if 0 < item_id <= len(lines):   # check if the item_id is valid
            line = lines[item_id - 1]   # fet the line corresponding to the item_id
            item_data = line.strip().split(',') # split the line into a list using comma
            current_quantity = int(item_data[-1])   # Convert last element to integer

            if 0 <= rented_qnty <= current_quantity :   # check if rented quantity is within available quantity
               
            
                new_quantity = current_quantity - rented_qnty   # calculate new quantity after renting
                item_data[-1] = str(new_quantity)   # update the quantity in item_data list
                lines[item_id - 1] = ",".join(item_data) + "\n" # update the line in 'lines' list

                with open(file_path, "w") as file:  # open the file again for writing
                    file.writelines(lines)  # write the updated 'lines' list back to the file
                
                # Gather customer information
                rented_item = item_data[0]  # Get the name of the rented equipment
                brand_name = item_data[1]   # Get the brand name of the equipment
                customer_name = input("Enter your name: ")  # Get customer name
                customer_number = input("Enter your number: ")  # Get customer number
                Total_amount=(float(item_data[2][1:]))  # Extract the item price and convert to float
                extra_amount= float(Total_amount) * float(rented_qnty)  # Calculate total cost
                # Generate invoice
                invoice_content = f"Company Name: The Rentals\n"
                invoice_content += f"Customer Number: {customer_number}\n"
                invoice_content += f"Customer Name: {customer_name}\n"
                invoice_content += f"Item: {rented_item}\n"
                invoice_content += f"Brand: {brand_name}\n"
                invoice_content += f"Total Amount: ${extra_amount:.2f}\n"
                current_datetime = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                invoice_content += f"Date and Time: {current_datetime}\n"
                write_invoice("invoice_rent.txt", invoice_content)
                # Loop for renting addiotional items
                while True:
                    extra_item=input("Would you like to rent another item?")    # Ask the user if they want to rent another item
                    if (extra_item=="yes"): # if the user chooses 'yes'
                        item_id=int(input("Enter a valid equipment id"))    # Ask them to enter the valid id
                        rented_qnty=int(input("Enter a valid quantity"))    # Ask them to enter the valid quantity
                        with open(file_path, "r") as file:  # open the file for reading
                            lines = file.readlines()    # Read all lines

                        if 0 < item_id <= len(lines):   # Check if the item_id is valid
                            line = lines[item_id - 1]   # get the line corresponding to the item_id
                            item_data = line.strip().split(',') # split the line into a list using comma
                            current_quantity = int(item_data[-1])   # conert last element to integer

                        if rented_qnty > current_quantity:  # check if the rented quantity is within the available list or not
                            print("Error: Selected Quantity exceeds the available quantity.")
                        else:
                            new_quantity = current_quantity - rented_qnty   # Calculate the quantity after renting
                            item_data[-1] = str(new_quantity)   # update the quantity is item_data list
                            lines[item_id - 1] = ",".join(item_data) + "\n" # update the line

                        with open(file_path, "w") as file:  # open the file again for writing
                            file.writelines(lines) 

                            rented_item = item_data[0]  # get the name of the rented item
                            brand_name = item_data[1]   # get the brand name of the item

                            
                            Total_amount2=(float(item_data[2][1:])) # extract the price and convet to float
                            extra_amount2= float(Total_amount2) * float(rented_qnty)    # calculate total cost
                            current_datetime = datetime.now().strftime('%Y-%m-%d %H:%M:%S') #extract the current date time
                            print("item rented successfully.")
                            Final_amount= float(extra_amount)+float(extra_amount2)  # calculate the sum of both the items
                            # Generate invocie
                            invoice_content = f"Item: {rented_item}\n"
                            invoice_content += f"Brand: {brand_name}\n"
                            invoice_content += f"Date and Time: {current_datetime}\n"
                            invoice_content += f"Total Amount: ${extra_amount2:.2f}\n"
                            invoice_content += f"Total Amount for all the items: ${Final_amount:.2f}"
                            write_invoice("invoice_rent.txt", invoice_content)
                         # Show the updated list
                        print("Here is the updated list after renting")
                        print("----------------------------------------------------------------------------------------------------")
                        print("S.N.   \t  Name \t\t         Brand Name        \t Price           Quantity")
                        print("----------------------------------------------------------------------------------------------------")

                                    
                        file=open("data.txt","r")
                        a=0
                        for line in file:
                            a= a+1
                            list_= line.strip().split(",")
                            name = list_[0]
                            brand = list_[1]
                            price = list_[2]
                            quantity = list_[3]   
                                
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
                        break
                                
                    elif(extra_item=="no"):
                        
                        False
                        
                        print("item rented successfully.")
                        print("Here is the updated list after renting")
                        print("----------------------------------------------------------------------------------------------------")
                        print("S.N.   \t  Name \t\t         Brand Name        \t Price           Quantity")
                        print("----------------------------------------------------------------------------------------------------")

                                    
                        file=open("data.txt","r")
                        a=0
                        for line in file:
                            a= a+1
                            list_= line.strip().split(",")
                            name = list_[0]
                            brand = list_[1]
                            price = list_[2]
                            quantity = list_[3]   
                                
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
                    break
            else:
                 print("Error: Selected Quantity exceeds the available quantity.")          
        else:
            print("Invalid item ID.")
        
    except FileNotFoundError:
        print("File not found.")
    except Exception as e:
        print(f"An error occurred: {e}")





############################################################################################################################

def return_item(file_path, item_id, returned_qnty):
    """
    Return rented equipment to the inventory and update related records.
    :param file_path: Path to the equipment data file
    :param item_id: ID of the equipment to be returned
    :param returned_qnty: Quantity of equipment to be returned
    :return: None"""
         
    try:
        with open(file_path, "r") as file:  # open the equipment file for reading
            lines = file.readlines() # read all lines from the file and store in 'lines'

        if 0 < item_id <= len(lines):   # check if the ite_id is valid
            line = lines[item_id - 1]   # get the line corresponding to the item_id
            item_data = line.strip().split(',') # split the line into a list usong comma 
            current_quantity = int(item_data[-1])   # convert last element to integer 

            if returned_qnty >0:    # check if the returned quantity is above 0    
                new_quantity = current_quantity + returned_qnty # calculate the quantity
                item_data[-1] = str(new_quantity)   # update the quantity in the item_data list
                lines[item_id - 1] = ",".join(item_data) + "\n" # update the line 

                with open(file_path, "w") as file:  # open the file again for writing
                    file.writelines(lines)  
        
                returned_item = item_data[0]    # get the name of the rented item
                brand_name = item_data[1]   # get the brand name of the rented item
                print("enter your details:")
                print("\n")
                customer_name = input("Enter your name: ")  # Get customer name
                customer_number = input("Enter your phone number: ")    # get customer number
                E_days=input("was the item rented for extra days?(yes/no)") # ask if the user has rented the item for extra days
                
                opt=True
                invoice_content = f"Company Name:The Rentals\n"
                invoice_content += f"Name: {customer_name}\n"
                invoice_content += f"Number: {customer_number}\n"
                # loop for asking how many extra days they have rented the item
                while opt==True:
                    if E_days=="yes":   # if they say yes
                        extra_days=input("For how many extra days:")    # ask how many extra days was the item rented for
                        Total_amount = (float(extra_days) * (float(item_data[2][1:])/5)) + float(item_data[2][1:])  # calculate the total amount
                        invoice_content += f"Total Amount: ${Total_amount:.2f}\n"
                        break
                    elif E_days=="no":  # if they say no
                        invoice_content += f"Total Amount: ${float(item_data[2][1:]):.2f}\n"    # generate the invoice 
                        break

                    else:
                        print("Invalid option")
                    
                current_datetime = datetime.now().strftime('%Y-%m-%d %H:%M:%S') # get the current date and time
                print("item returned successfully.")

                # generate the invoice
                invoice_content += f"Item: {returned_item}\n"
                invoice_content += f"Brand: {brand_name}\n"
                invoice_content += f"Date and Time: {current_datetime}\n"
                write_invoice("invoice_return.txt", invoice_content)


                # display the updated quantities of the item
                print("Here is the updated list after returning the item")
                print("----------------------------------------------------------------------------------------------------")
                print("S.N.   \t  Name \t\t         Brand Name        \t Price           Quantity")
                print("----------------------------------------------------------------------------------------------------")

                            
                file=open("data.txt","r")
                a=0
                for line in file:
                    a= a+1
                    list_= line.strip().split(",")
                    name = list_[0]
                    brand = list_[1]
                    price = list_[2]
                    quantity = list_[3]   
                        
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
            else:
                print("you have entered an invalid amount!")
            
        else:
            print("Invalid item ID.")
    except FileNotFoundError:
        print("File not found.")
    except Exception as e:
        print(f"An error occurred: {e}")


############################################################################################################################
