from sys import maxsize

class Addrress:

    def __init__(self, fname=None, mname=None, lname=None, niname=None, comp=None, addrr=None, homtel=None, mail=None, id=None, twoname=None):
        self.fname=fname
        self.mname=mname
        self.lname=lname
        self.niname=niname
        self.comp=comp
        self.addrr=addrr
        self.homtel=homtel
        self.mail=mail
        self.id=id
        self.twoname=twoname

    def __repr__(self):
        return "%s:%s" % (self.id, self.twoname)

    def __eq__(self, other):
        return (self.id is None or other.id is None or self.id == other.id) and self.twoname == other.twoname

    def id_or_max(self):
        if self.id:
            return int(self.id)
        else:
            return maxsize