from app.utils.database import db

class Animals(db.Model):
    __tablename__ = "animal"
    
    id = db.Column(db.Integer, primary_key=True)
    species = db.Column(db.String(100), nullable=False)
    age = db.Column(db.Integer, nullable=False)
    gender = db.Column(db.String(100), nullable=False)
    special_requirements = db.Column(db.String(100), nullable=True)
    
    def as_dict(self):
        return {
                    "id": self.id,
                    "species": self.species,
                    "age": self.age,
                    "gender": self.gender,
                    "special_requirements": self.special_requirements
                }