#greeter.py
def get_formatted_name(first_name,last_name):
    """返回完整的姓名"""
    full_name = first_name + ' ' + last_name
    return full_name.title()
# 这是一个无限循环
while True:
    print("\nPlease tell me your name:")
    print("enter 'q' at any time to quit")
    f_name = input("Firsr name:")
    if f_name == 'q':
        break
    l_name = input("Last name:")
    if l_name == 'q':
        break
    formatted_name = get_formatted_name(f_name,l_name)
    print("\nHello," + formatted_name + "!")