import codecs

def encode(s):
    if not isinstance(s,str):
        raise TypeError
    origlen = len(s)
    crypted = ""
    digitmapping = dict(zip('1234567890!"#€%&/()=','!"#€%&/()=1234567890'))
    if len(s) > 1000:
        raise ValueError
    
    #maksimi
    s = s.ljust(1000, "a")

    for c in s:
        #virheelliset arvot
        if c in ["å", "ä", "ö"]:
            raise ValueError
        
        if c.isalpha():
            if c.islower():
                c=c.upper()
            # Rot13 the character for maximum security
            crypted+=codecs.encode(c,'rot13')
        elif c in digitmapping:
          crypted+=digitmapping[c]
        #jos ei ole digit tai kirjain niin virhe
        else:
            raise ValueError
    #alkuperäinen pituus
    return crypted[:origlen]

def decode(s):
    return encode(s).lower()