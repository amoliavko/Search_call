from voip import db


class cdr(db.Model):
    __tablename__ = 'cdr'
    __bind_key__ = 'cdr'
    acctid = db.Column(db.Integer, primary_key=True)
    calldate = db.Column(db.TIMESTAMP)
    clid = db.Column(db.String(80))
    src = db.Column(db.String(80))
    dst = db.Column(db.String(80))
    dcontext = db.Column(db.String(80))
    channel = db.Column(db.String(80))
    dstchannel = db.Column(db.String(80))
    lastapp = db.Column(db.String(80))
    lastdata = db.Column(db.String(80))
    duration = db.Column(db.Integer)
    billsec = db.Column(db.Integer)
    disposition = db.Column(db.String(45))
    amaflags = db.Column(db.Integer)
    accountcode = db.Column(db.String(20))
    uniqueid = db.Column(db.String(150))
    userfield = db.Column(db.String(255))
