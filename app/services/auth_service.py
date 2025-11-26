from app.extensions import db, bcrypt
from app.models import User
from flask_jwt_extended import create_access_token
from datetime import timedelta

class AuthService:

    @staticmethod
    def register_user(name, email, password):
        existing = User.query.filter(User.email == email).first()
        if existing:
            return None, "Email already exists"

        hashed_pw = bcrypt.generate_password_hash(password).decode("utf-8")

        user = User(
            name = name,
            email = email,
            password = hashed_pw
        )

        db.session.add(user)
        db.session.commit()
        return user,None
    
    @staticmethod
    def login_user(email, password):
        user = User.query.filter_by(email=email).first()
        if not user:
            return None, "Invalid email or password"
        
        if not bcrypt.check_password_hash(user.password, password):
            return None, "Invalid email or password"

        access_token = create_access_token(
            identity=str(user.id),
            additional_claims={
                "email": user.email,
                "role": user.role
            },
            expires_delta = timedelta(days = 1)
        )

        return access_token, None