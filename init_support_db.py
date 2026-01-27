#!/usr/bin/env python
"""
Database initialization script for Support Dashboard
Run this after deploying to create tables and default users
"""
from support_app import app, db, SupportStaff
import logging
import sys

logging.basicConfig(level=logging.INFO)

def init_database():
    """Initialize database with tables and default users"""
    with app.app_context():
        try:
            # Create all tables
            db.create_all()
            logging.info("Database tables created successfully")

            # Check if admin already exists
            if SupportStaff.query.filter_by(username='admin').first():
                logging.info("Default users already exist")
                return True

            # Create default admin user
            admin = SupportStaff(
                username='admin',
                email='admin@support.com',
                role='manager'
            )
            admin.set_password('admin123')

            # Create default agents
            agent1 = SupportStaff(
                username='agent1',
                email='agent1@support.com',
                role='agent'
            )
            agent1.set_password('agent123')

            agent2 = SupportStaff(
                username='agent2',
                email='agent2@support.com',
                role='agent'
            )
            agent2.set_password('agent123')

            db.session.add_all([admin, agent1, agent2])
            db.session.commit()

            logging.info("Default support staff created successfully")
            logging.info("Manager: admin / admin123")
            logging.info("Agent: agent1 / agent123")
            logging.info("Agent: agent2 / agent123")
            logging.info("\n⚠️  IMPORTANT: Change these default passwords immediately!")

            return True

        except Exception as e:
            logging.error(f"Error initializing database: {str(e)}")
            db.session.rollback()
            return False

if __name__ == '__main__':
    success = init_database()
    if success:
        print("\nYou can now start the support dashboard!")
    else:
        print("\nFailed to initialize support database.")
        sys.exit(1)