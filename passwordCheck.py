import hashlib
def check(username, password, userInfo):
    hashUsername = hashlib.sha256(username.encode()).hexdigest()
    hashPassword = hashlib.sha256(password.encode()).hexdigest()
    hash_username_password = hashUsername + hashPassword
    all_hash = hashlib.sha256(hash_username_password.encode()).hexdigest()
    check_username_hash = userInfo['password'].split(";")[0].split("$")[1]
    check_password_hash = userInfo['password'].split(";")[1].split("$")[0]
    if check_username_hash == hashUsername and check_password_hash == all_hash and userInfo['status'] == 'locked':
        return 3
    elif check_username_hash == hashUsername and check_password_hash == all_hash and userInfo['status'] == 'inactive':
        return 2
    elif check_username_hash == hashUsername and check_password_hash == all_hash and userInfo['status'] == 'normal':
        return 1
    else:
        return 0

if __name__ == '__main__':
    import main
    main.mainWindow()