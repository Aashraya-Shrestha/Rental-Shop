def rent_item(file_path, item_id, rented_qnty):
    try:
        with open(file_path, "r") as file:
            lines = file.readlines()

        if 0 < item_id <= len(lines):
            line = lines[item_id - 1]
            item_data = line.strip().split(',')
            current_quantity = int(item_data[-1])

            if rented_qnty > current_quantity:
                print("Error: Quantity to reduce exceeds current quantity.")
            else:
                new_quantity = current_quantity - rented_qnty
                item_data[-1] = str(new_quantity)
                lines[item_id - 1] = ",".join(item_data) + "\n"

                with open(file_path, "w") as file:
                    file.writelines(lines)
                print("Quantity updated successfully.")
        else:
            print("Invalid item ID.")
    except FileNotFoundError:
        print("File not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

file_path = "data.txt"  # Replace this with the actual file path
valid_id = int(input("Enter a valid ID: "))
valid_quantity = int(input("Enter the quantity to reduce: "))

rent_item(file_path, valid_id, valid_quantity)
