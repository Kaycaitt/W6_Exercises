#Function 1
def get_soc_sec_tax(gross_pay):
    sstax = gross_pay*0.062
    return sstax


#Function 2
def get_medicare_tax(gross_pay):
    medtax = gross_pay*0.0145
    return medtax


#Function 3
def get_federal_tax(gross_pay, withholding_code):
    if withholding_code == 0:
        tax_rate = 0.23
    elif withholding_code == 1:
        tax_rate = 0.21
    elif withholding_code == 2:
        tax_rate = 0.195
    elif withholding_code == 3:
        tax_rate = 0.185
    elif withholding_code >= 4:
        # Calculate the tax rate for codes 4 and above
        tax_rate = 0.18 - (0.005 * (withholding_code - 4))
        # Ensure tax rate doesn't go below zero
        tax_rate = max(tax_rate, 0)
    else:
        raise ValueError("Invalid withholding code.")

    federal_tax = gross_pay * tax_rate  # Calculate the federal tax
    return federal_tax

try: #allow user input
    gross_pay = float(input("Enter the gross pay amount: $"))
    withholding_code = int(input("Enter the withholding code (0-4+): "))
    
    # Calculate the federal tax
    federal_tax = get_federal_tax(gross_pay, withholding_code)
    soc_sec_tax = get_soc_sec_tax(gross_pay)
    medicare_tax = get_medicare_tax(gross_pay)
    
    print(f'\nFederal tax withholding for a gross pay of ${gross_pay:.2f} with withholding code {withholding_code} is: ${federal_tax:.2f}')
    print(f'Social Security tax for a gross pay of ${gross_pay:.2f} is: ${soc_sec_tax:.2f}')
    print(f'Medicare tax for a gross pay of ${gross_pay:.2f} is: ${medicare_tax:.2f}')
except ValueError as e:
    print(f"Error: {e}. Please enter valid numeric values.")