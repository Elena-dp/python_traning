from sys import maxsize

class Addrress:

    def __init__(self, fname=None, mname=None, lname=None, niname=None, comp=None, addrr=None, homephone=None,
                 mobilephone=None, workphone=None, secondaryphone=None, all_phones_from_home_page = None, mail=None,
                 id=None, mail1=None, mail2=None, mail3=None):
        self.fname=fname
        self.mname=mname
        self.lname=lname
        self.niname=niname
        self.comp=comp
        self.addrr=addrr
        self.homephone=homephone
        self.mobilephone=mobilephone
        self.workphone=workphone
        self.secondaryphone=secondaryphone
        self.all_phones_from_home_page = all_phones_from_home_page
        self.mail=mail
        self.mail1=mail1
        self.mail2=mail2
        self.mail3=mail3
        self.id=id


    def __repr__(self):
        return "%s:%s:%s" % (self.id, self.lname, self.fname)

    def __eq__(self, other):
        return (self.id is None or other.id is None or self.id == other.id) and self.lname == other.lname and self.fname == other.fname

    def id_or_max(self):
        if self.id:
            return int(self.id)
        else:
            return maxsize