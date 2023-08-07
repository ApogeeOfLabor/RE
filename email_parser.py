import re


def get_data(mail):
    user_data = {}
    try:
        pattern = re.compile(r"^([\w.-]+)@(\w+[\.?][a-z0-9]+)$")
        data = re.match(pattern, mail).groups()

        user_data['username'], user_data['domain'] = data[0], data[1]
    except:
        print(f'wrong email: {mail}')
        exit()

    return user_data


if __name__ == '__main__':
    user_email = input('Enter email: ')
    print(get_data(user_email))
