Inventory_management = {}

Inventory_management['Apple'] = 60
Inventory_management['mangoe'] = 70
Inventory_management['tomato'] = 40
Inventory_management['carrot'] = 100
Inventory_management['banana'] = 200
Inventory_management['brush'] = 10

print(Inventory_management)

del Inventory_management['brush']

Inventory_management['onion'] = 500

print(Inventory_management)

# for key in Inventory_management:
#     print(key)

# for key in Inventory_management:
#     print(key , Inventory_management[key])

# for k,v in Inventory_management.items():
#     print(f'key : {k} , value : {v}')

for  i,(k, v) in enumerate(Inventory_management.items()):
    print(f"{i} key : {k} , value : {v}")


        
