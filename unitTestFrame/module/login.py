def login(name,password) -> str:
    if name == 'admin' and password == '123456':
        return 'succeed'
    else:
        return 'failure'


