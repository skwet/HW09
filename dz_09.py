from pprint import pprint
contact_dict={}
def input_error(func):
    def wrapper(*args):
        try:
            return func(*args)
        except IndexError:
            return 'Not enough data'
        except KeyError:
            return 'Are you sure that you added this contact?.Try again'
        except ValueError:
            return 'Impossible to add this number'
    return wrapper

def hello(*args):
    return 'What`s up?How can I help you?'
@input_error
def add(*args):
    input_split = args[0].split()
    name = input_split[0]
    phone = input_split[1]
    if len(phone) < 14 and not phone.startswith('+'):
        raise ValueError
    if not phone:
        raise IndexError
    contact_dict[name] = phone
    return f'U added {name} with phone {phone}'
@input_error
def change(*args):
    input_split = args[0].split()
    name = input_split[0]
    new_number = input_split[1]
    contact_dict[name] = new_number
    return f'{name} has new phone: {new_number}'
@input_error
def phones(*args):
    input_split = args[0].split()
    name = input_split[0]
    phone_number = contact_dict[name]
    if not name:
        raise KeyError
    return f'The phone number for {name} is {phone_number}'
def show_all(*args):
    pprint(contact_dict)
def bb(*args):
    return 'Good bye'

commands = {hello:'hello',
            add:'add',
            change:'change',
            phones:'phone',
            show_all:'show all',
            bb:'bye'}

def handler(text):
    for command,kword in commands.items():
        if text.startswith(kword):
            return command,text.replace(kword,'').strip()
    return None

def main():
    while True:
        user_input = input('>>>')
        command,data =handler(user_input)
        print(command(data))
        if command == bb:
            break
if __name__ == '__main__':
    main()

