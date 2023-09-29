import hashlib, itertools

import string

def brute_force_attack(hashed_passwords):
    passwordCharacters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','0','1','2','3','4','5','6','7','8','9']
    length = 1
    while length < 5 and len(crackedPasswords) < 5:
        for pwd in itertools.product(passwordCharacters, repeat=length):
            pwd_str = "".join(pwd)
            print(pwd_str)
            hashed_pwd = hashlib.sha512(pwd_str.encode()).hexdigest()
            if hashed_pwd in hashed_passwords:
                print(f"Password found: {pwd_str}")
                crackedPasswords.append(pwd_str)
        if not hashed_passwords:
                return
        length += 1
    print("the passwords are: ", crackedPasswords)
hashed_passwords = ['f14aae6a0e050b74e4b7b9a5b2ef1a60ceccbbca39b132ae3e8bf88d3a946c6d8687f3266fd2b626419d8b67dcf1d8d7c0fe72d4919d9bd05efbd37070cfb41a','e85e639da67767984cebd6347092df661ed79e1ad21e402f8e7de01fdedb5b0f165cbb30a20948f1ba3f94fe33de5d5377e7f6c7bb47d017e6dab6a217d6cc24','4e2589ee5a155a86ac912a5d34755f0e3a7d1f595914373da638c20fecd7256ea1647069a2bb48ac421111a875d7f4294c7236292590302497f84f19e7227d80','afd66cdf7114eae7bd91da3ae49b73b866299ae545a44677d72e09692cdee3b79a022d8dcec99948359e5f8b01b161cd6cfc7bd966c5becf1dff6abd21634f4b']
counter = 0
crackedPasswords = []
brute_force_attack(hashed_passwords)

