def read_equipment(filename):
    equipment_list = [] # initialize and empty list to store the item information
    with open(filename, 'r') as file:   # open the file for reading
        lines = file.readlines()    # read all lines from the file
        for line in lines:  # loop through each line in the file
            parts = line.strip().split(',') #seperate the line into sections using comma as a seperator
            name = parts[0].strip() # get the name of the equipment
            brand = parts[1].strip()    # get the brand name of the equipment
            price = float(parts[2].strip()[1:]) # Convert and extract the price removing '$'
            quantity = int(parts[3].strip())    # Convert and extract the quantity
            # create a dictionary to store equipment details and add it to the list
            equipment_list.append({'name': name, 'brand': brand, 'price': price, 'quantity': quantity})
    return equipment_list # return the list containing equipment information
