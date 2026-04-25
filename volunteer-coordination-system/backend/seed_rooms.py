from app import create_app, db
from app.models.message import ChatRoom
from datetime import datetime

def seed_rooms():
    app = create_app()
    with app.app_context():
        # Check if rooms already exist to avoid duplicates
        if ChatRoom.query.first():
            print("Chat rooms already exist. Skipping seeding.")
            return

        rooms = [
            {
                'name': 'General Community',
                'description': 'Open discussion for everyone',
                'type': 'general',
                'pin_order': 1
            },
            {
                'name': 'Urgent Alerts',
                'description': 'Post critical emergencies here',
                'type': 'urgent',
                'pin_order': 2
            },
            {
                'name': 'NGO Announcements',
                'description': 'Official NGO announcements',
                'type': 'announcements',
                'pin_order': 3
            },
            {
                'name': 'Volunteers Only',
                'description': 'Private coordination for volunteers',
                'type': 'volunteers_only',
                'pin_order': 4
            },
            {
                'name': 'Palladam Hub',
                'description': 'Coordination for Palladam area',
                'type': 'location_based',
                'location': 'Palladam',
                'pin_order': 5
            },
            {
                'name': 'Ukkadam Hub',
                'description': 'Coordination for Ukkadam area',
                'type': 'location_based',
                'location': 'Ukkadam',
                'pin_order': 6
            },
            {
                'name': 'Peelamedu Hub',
                'description': 'Coordination for Peelamedu area',
                'type': 'location_based',
                'location': 'Peelamedu',
                'pin_order': 7
            },
            {
                'name': 'NGO & Community',
                'description': 'Shared space for NGO and Community members',
                'type': 'ngo_community',
                'pin_order': 8
            }
        ]

        for r_data in rooms:
            room = ChatRoom(**r_data)
            db.session.add(room)
        
        try:
            db.session.commit()
            print("Chat rooms seeded successfully!")
        except Exception as e:
            db.session.rollback()
            print(f"Error seeding rooms: {e}")

if __name__ == '__main__':
    seed_rooms()
