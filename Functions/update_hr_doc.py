hr_list = [('0123', 'HR', 'Rebecca Yang', '69000'), ('0121', 'IT', 'Mark Blick', '67000'),
('0068', 'IT', 'Kahna Larsen', '112000'), ('0234', 'OPS', 'Jim Smith', '54000')]

my_hr_list = [list(_) for _ in hr_list] #added _ instead of variable name to ignore the specific value of the tuple.

for i in range(len(hr_list)): #i symbolizes the index for the loop
    if my_hr_list[i][2] == "Mark Blick":
        my_hr_list[i][2] = "Mark Blick-Hawley"
    if my_hr_list[i][3] == "54000":
        my_hr_list[i][3] = "60000"
    if my_hr_list[i][1] == "OPS":
        my_hr_list[i][1] = "CS"

hr_list = [tuple(_) for _ in my_hr_list] #i need this line of code in order for the changes to apply to the existing list. If not, no changes are made.
for _ in my_hr_list:
    format_salary = f"{int(_[3]):,}" #need to convert the salary type to having comma while perserving value.
#"Employee# | DeptCode | Name | NN,NNN"
    print(f'''{_[0]} | {_[1]} | {_[2]} | {format_salary}''') #need to have the format_salary variable here, otherwise commas do not print
