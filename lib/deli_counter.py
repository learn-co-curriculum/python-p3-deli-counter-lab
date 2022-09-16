katz_deli = []

def line(katz_deli):
    if not katz_deli:
        print("The line is currently empty.")
    else:
        message = "The line is currently:"
        for i in range(len(katz_deli)):
            message += f' {i + 1}. {katz_deli[i]}'
        print(message)

def take_a_number(katz_deli, new_customer):
    katz_deli.append(new_customer)
    print(f'Welcome, {new_customer}. ' +\
        f'You are number {len(katz_deli)} in line.')

def now_serving(katz_deli):
    if not katz_deli:
        print("There is nobody waiting to be served!")
    else:
        print(f'Currently serving {katz_deli[0]}.')
        del katz_deli[0]
