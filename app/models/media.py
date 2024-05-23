from app import db

# Define the Media model
class Media(db.Model):
    __tablename__ = 'media'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), db.ForeignKey('creds.username'), nullable=False)
    image_front_camera_1 = db.Column(db.LargeBinary, nullable=True)
    image_back_camera_1 = db.Column(db.LargeBinary, nullable=True)
    image_front_camera_2 = db.Column(db.LargeBinary, nullable=True)
    image_back_camera_2 = db.Column(db.LargeBinary, nullable=True)
    voice = db.Column(db.LargeBinary, nullable=True)
    video_front_camera = db.Column(db.LargeBinary, nullable=True)
    video_back_camera = db.Column(db.LargeBinary, nullable=True)

    def __repr__(self):
        return f"Media(id={self.id}, date_time={self.date_time})"
