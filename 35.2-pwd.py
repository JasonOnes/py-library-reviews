""" pwd module gives access to Unix password database as a list object of struct_passwd's with named tuple like
attribs: pw_name, pw_passwd, pw_uid, pw_gid, pw_gecos, pw_dir, pw_shell which are ints or strings"""


# if pw_password == 'x' => encrypted

import pwd
import getpass

def find_pwords_that_need_to_be_encrypted():
    # returns a list of unencrypted pwords though I'm not sure if Unix allows pw to NOT be encrypted
    pword_to_encrypt = []
    for p in pwd.getpwall():
        if p.pw_passwd != 'x':
            print(p.pw_name)
            pword_to_encrypt.append(p.pw_name)
    if len(pword_to_encrypt) == 0: 
        print("All Unix account passwords encrypted!")
    return pword_to_encrypt

def find_user_pw_data():
    # just prints/returns the pw attributes for user login name (see #15.1-getpass.py) 
    user = getpass.getuser()
    try:
        print(pwd.getpwnam(user))
        return(pwd.getpwnam(user))
    except KeyError:
        print("couldn't find pw_word info for user")
        return None

def see_pwds_with_comments():
    # names and comments are usually the same but sometimes add comments are informative
    for p in pwd.getpwall():
        print(p.pw_name + ": " + p.pw_gecos)


if __name__ == '__main__':
    find_pwords_that_need_to_be_encrypted()
    find_user_pw_data()
    see_pwds_with_comments()