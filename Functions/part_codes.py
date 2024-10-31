parse = 'ACME:123-L DI:12345-M ACE:1-12'
#can't have commas between items, otherrwise .find doesn't activate. also removed extra quotes so the split could do its work with the spaces

#need to use split here in order to get output for all the suppliers
items = parse.split()

#need to set a for loop in order for it to cycle through all the items listed.
for item in items:
    need_space = item.find(':')
    need_space2 = item.find('-')

    get_supplier_code = item[:need_space] #had to add colon here, otherwise I wasn't getting proper output for code/number
    get_product_num = item[need_space + 1:need_space2]
    get_size = item[need_space2 + 1]

    print(f''' 
    Supplier Code: {get_supplier_code}
    Product Number: {get_product_num}
    Product Size: {get_size}
    ''') #had to move this statement inside of the loop to work properly. Then had to remove the extra listings for code, number and size because it was conflicting with the loop output.