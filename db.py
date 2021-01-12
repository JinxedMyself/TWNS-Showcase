class submit(db.Model):
    __tablename__ = 'submitted_tweets'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    tweet = db.Column(db.Text(140))
    date_posted = db.Column(db.DateTime, default=datetime.utcnow)

class approved(db.Model):
    __tablename__ = "approved_tweets"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    tweet = db.Column(db.Text(140))
    date_posted = db.Column(db.DateTime)

class rejected(db.Model):
    __tablename__ = "rejected_tweets"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    tweet = db.Column(db.Text(140))
    date_posted = db.Column(db.DateTime)
    reason = db.Column(db.Text(255))