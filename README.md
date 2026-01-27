# Support Dashboard

A Flask-based support ticket management system for handling customer support queries.

## Features

- 🎫 **Ticket Management**: View, assign, and resolve support tickets
- 👥 **User Roles**: Manager and Agent roles with different permissions
- 🔄 **Round-Robin Assignment**: Automatic ticket assignment to available agents
- 📊 **Dashboard Analytics**: Real-time statistics and metrics
- 🔐 **Authentication**: Secure login system with Flask-Login
- 🗄️ **Database Support**: Works with SQLite (development) and PostgreSQL (production)

## Quick Start (Local Development)

### Prerequisites

- Python 3.8+
- pip

### Installation

1. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

2. **Set up environment variables**

   Create a `.env` file in the "Support Dashboard" directory:
   ```env
   SUPPORT_SECRET_KEY=your-secret-key-here
   FLASK_ENV=development
   ```

3. **Initialize the database**
   ```bash
   python init_support_db.py
   ```

4. **Run the application**
   ```bash
   python support_app.py
   ```

   The app will be available at: `http://localhost:8001`

### Default Credentials

- **Manager**: `admin` / `admin123`
- **Agent**: `agent1` / `agent123`
- **Agent**: `agent2` / `agent123`

⚠️ Change these passwords immediately in production!

## Deployment

See [DEPLOYMENT_GUIDE.md](./DEPLOYMENT_GUIDE.md) for detailed instructions on deploying to Render.

Quick deploy with Render Blueprint:
1. Push code to Git
2. Connect to Render
3. Click "New" → "Blueprint"
4. Select your repository
5. Deploy!

## Project Structure

```
Support Dashboard/
├── support_app.py          # Main Flask application
├── init_support_db.py      # Database initialization script
├── requirements.txt        # Python dependencies
├── render.yaml            # Render deployment configuration
├── .env                   # Environment variables (local)
├── .env.production        # Production environment template
├── templates/             # Jinja2 HTML templates
│   ├── login.html
│   ├── dashboard.html
│   ├── tickets.html
│   └── view_ticket.html
├── static/                # Static assets (CSS, JS, images)
└── instance/              # Database files (gitignored)
```

## Technology Stack

- **Backend**: Flask 2.3.3
- **Authentication**: Flask-Login
- **Database**: SQLAlchemy (SQLite/PostgreSQL)
- **Production Server**: Gunicorn
- **Frontend**: Jinja2 templates with Bootstrap

## API Endpoints

### Authentication
- `GET/POST /login` - User login
- `GET /logout` - User logout

### Dashboard
- `GET /` - Main dashboard (requires login)
- `GET /tickets` - View all tickets with filters
- `GET /ticket/<ticket_id>` - View ticket details

### Ticket Management
- `POST /ticket/<ticket_id>/assign` - Assign ticket to agent
- `POST /ticket/<ticket_id>/update_status` - Update ticket status

### API (for Client App Integration)
- `POST /api/tickets` - Receive new ticket from client app
- `PUT /api/tickets/<ticket_id>/user_update` - Handle user updates
- `GET /api/stats` - Get dashboard statistics

## Environment Variables

| Variable | Description | Required | Default |
|----------|-------------|----------|---------|
| `SUPPORT_SECRET_KEY` | Flask secret key | Yes | - |
| `FLASK_ENV` | Environment mode | No | `development` |
| `SUPPORT_DATABASE_URL` | Database connection string | No | SQLite (local) |
| `CLIENT_API_URL` | Client app API endpoint | No | `http://localhost:5000/api` |

## Development

### Running in Development Mode

```bash
export FLASK_ENV=development
python support_app.py
```

### Database Migrations

To recreate the database:
```bash
rm instance/dump_analyzer.db  # Remove old database
python init_support_db.py     # Create new database
```

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

## License

MIT License - See LICENSE file for details

## Support

For deployment issues, see [DEPLOYMENT_GUIDE.md](./DEPLOYMENT_GUIDE.md)

---

**Last Updated**: January 2026
