# Django News Portal

A modern news portal built with Django 4.2, featuring a clean design and comprehensive news management system.

## Features

- **Homepage**: Featured articles and latest news
- **Article System**: Full article management with categories
- **Search Functionality**: Search through articles
- **Responsive Design**: Mobile-friendly interface
- **Admin Panel**: Django admin for content management
- **SEO Friendly**: Clean URLs and meta tags

## Installation

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd news_portal
   ```

2. **Create a virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run migrations**
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

5. **Create a superuser**
   ```bash
   python manage.py createsuperuser
   ```

6. **Collect static files**
   ```bash
   python manage.py collectstatic
   ```

7. **Run the development server**
   ```bash
   python manage.py runserver
   ```

## Usage

1. Access the admin panel at `http://localhost:8000/admin/`
2. Create categories and articles
3. Visit the homepage at `http://localhost:8000/`

## Project Structure

```
news_portal/
├── news_portal/          # Main project directory
│   ├── settings.py       # Project settings
│   ├── urls.py          # Main URL configuration
│   └── wsgi.py          # WSGI configuration
├── news/                # News app
│   ├── models.py        # Database models
│   ├── views.py         # View functions
│   ├── urls.py          # App URL configuration
│   ├── admin.py         # Admin configuration
│   └── migrations/      # Database migrations
├── templates/           # HTML templates
│   ├── base.html        # Base template
│   └── news/           # News app templates
├── static/             # Static files (CSS, JS, images)
│   └── css/
│       └── style.css   # Custom CSS
├── media/              # User uploaded files
├── requirements.txt    # Python dependencies
└── manage.py          # Django management script
```

## Models

### Category
- Name and slug
- Description
- Created timestamp

### Article
- Title and slug
- Author (User FK)
- Category (Category FK)
- Content and excerpt
- Featured image
- Publication status
- Featured flag
- Timestamps

## Pages

- **Homepage**: `/` - Featured and latest articles
- **Article Detail**: `/article/<slug>/` - Individual article view
- **Category Detail**: `/category/<slug>/` - Articles by category
- **Search**: `/search/` - Search functionality
- **About**: `/about/` - About page
- **Contact**: `/contact/` - Contact page

## Admin Features

- Article management with rich editor
- Category management
- User management
- Content filtering and search
- Bulk actions

## Customization

### Adding New Fields
1. Update models in `news/models.py`
2. Create and run migrations
3. Update admin configuration
4. Update templates as needed

### Styling
- Edit `static/css/style.css` for custom styles
- Bootstrap 5 is included for rapid development

## Security Features

- CSRF protection
- XSS protection
- SQL injection protection
- User authentication system
- Media file handling

## Performance

- Database indexing on frequently queried fields
- Pagination for article lists
- Static file compression ready
- Media file optimization ready

## Deployment

For production deployment:

1. Set `DEBUG = False` in settings
2. Configure proper database (PostgreSQL recommended)
3. Set up static file serving
4. Configure media file serving
5. Set proper security settings
6. Use environment variables for sensitive data

## License

This project is open source and available under the MIT License.