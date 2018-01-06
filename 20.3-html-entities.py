"""Not quite sure how to demo this module as it is basically just four dicts"""
# html.entities
#               .html5 => maps char refs to Unicode chars
#               .entitydefs => maps XHTML 1.0 entity defs to replacement test in ISO Latin-1 (?)
#               .name2codepoint => maps HTML enity names to Unicode code points (?)
#               .codepoint2name => Unicode code points to HTML entity names
# replaces htmlentitydefs in python2

import html 

def whats_the_html5_name_for_punctuation():
    # function explained by name
    punctuation_list = ['!', ',', '\'', '\"', '/', '.', ',', '?', '(', ')']
    punctuation_names = []
    symbol_dict =  html.entities.html5
    # quick lambda funct to get the key where value is punct char (unique)
    get_name = lambda v, symbol_dict: next(k for k in symbol_dict if symbol_dict[k] is v)

    name_template = "For {} the HTML5 name is {}."
    
    for item in punctuation_list:
        name = get_name(item, symbol_dict)
        print(name_template.format(item, name))
       

def frat_in_ISO(frat):
    # uses the entitydefs dict to find and print the english lets of frat in greek
    lets = frat.split(" ")
    greek_lets = []
    for let in lets:
        try:
            greek_let = html.entities.entitydefs[let]
            greek_lets.append(greek_let)
        except KeyError:
            print("It's NOT all greek to me! \"{}\" in {} mispelled".format(let, frat))
            print("Printed what I could!")
    frat_in_greek = "".join(greek_lets)
    print(frat + " : " + frat_in_greek)

def frat_in_unicode(frat):
    # uses the name2codepoint to find and print frat in code (unicode that is!)
    lets = frat.split(" ")
    codepoint_nums = []
    for let in lets:
        try: 
            codepoint = html.entities.name2codepoint[let]
            # could make it more "encoded" without comma as delimiter but that's not the point of this
            codepoint_nums.append(str(codepoint)+",")
        except KeyError:
            print("I don't know if that's how {} is spelled.".format(let))
    frat_code = "".join(codepoint_nums)
    print(frat + ":" + frat_code)

def frat_de_unicoded(unicoded_frat):
    # basically undoes the previous function for "decoding"
    nums = unicoded_frat.split(",")
    frat = []
    for num in nums:
        try:
            letter = html.entities.codepoint2name[int(num)]
            frat.append(letter)
        except KeyError:
            print("Yeah, {} is a bogus number.".format(num))
    frat_name = "".join(frat)
    print(frat_name)


if __name__ == "__main__":

    whats_the_html5_name_for_punctuation()
    frat_in_ISO('kappa lambda mu')
    frat_in_ISO('Sigma Delta pie')

    frat_in_unicode('phi beta Rho')
    frat_in_unicode('omega alpa delta')

    frat_de_unicoded('966,946,929')
    frat_de_unicoded('969,948,666')



