
def write_invoice(filename, content):
    with open(filename, 'a') as file:
        file.write(content + '\n')

