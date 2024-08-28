from db.db import db

class Orders(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  userName = db.Column(db.String(100), nullable=False)
  userEmail = db.Column(db.String(100), nullable=False)
  saleTotal = db.Column(db.Float, nullable=False)

  def __init__(self, userName, userEmail, saleTotal):
    self.userName = userName
    self.userEmail = userEmail
    self.saleTotal = saleTotal
