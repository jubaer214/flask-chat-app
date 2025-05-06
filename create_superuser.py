from website import create_app, db
from website.models import User
from werkzeug.security import generate_password_hash
from datetime import datetime
import uuid

def main():
    app = create_app()
    with app.app_context():
        # Check if superuser already exists
        if User.query.filter_by(username='root').first():
            print("Superuser 'root' already exists.")
            return

        root = User(
            id=str(uuid.uuid4()),
            username='root',
            nickname='root',                              # required
            email='root@example.com',
            password=generate_password_hash(
                "T9x!rV@5mL#8wQz&Kd3", method='pbkdf2:sha256'
            ),
            dob='1990-01-01',                             # required
            country='N/A',                                # required
            aboutme='Superuser account',
            last_seen=datetime.utcnow(),
            random_search_enabled=True,
            img='',                                       # optional
            gender='Other',                               # optional
            is_superuser=True
        )
        db.session.add(root)
        db.session.commit()
        print("✅ Superuser 'root' created successfully.")

if __name__ == "__main__":
    main()
