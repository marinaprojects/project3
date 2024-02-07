from utils import *


values = get_executed_operation(load_json_file())
operations = sort_operations_date(values)
date = change_data(operations)
card_number = mask_card_number(operations)
amount_number = mask_amount_number(operations)

print(card_number)
for operation in range(len(operations)):
    print(f"{date[operation]} {operations[operation]['description']}")
    print(f"{card_number[operation]} -> Счет {amount_number[operation]}")
    print(f"{operations[operation]['operationAmount']['amount']} {operations[operation]['operationAmount']['currency']['name']}\n")

