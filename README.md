# Search Project

Search is a web application built using Python and Django framework. It provides functionality to search for specific terms within paragraphs and returns the paragraphs containing the search terms. PostgreSQL is used as the database management system for storing paragraph data.

## Features

- Search functionality to find specific terms within paragraphs.
- PostgreSQL database integration for storing and managing paragraph data.
- User-friendly interface with HTML and CSS for an enhanced user experience.
- Authentication system with signup and login pages.
- Additional pages for various functionalities.

## Requirements

- Python 3.x
- Django
- PostgreSQL
- HTML
- CSS

## Installation

1. Clone the repository: https://github.com/swati07010/Codemonk1/tree/master/Search
2. Navigate to the project directory:cd Search
3. Configure PostgreSQL:
   - Install PostgreSQL if not already installed.
   - Create a new database for the project.
   - Update the database settings in `settings.py` with the database name, user, password, and host.
4. Apply migrations:python manage.py migrate
5.Run the development server:python manage.py runserver
6. Access the application in your web browser at `http://localhost:8000/`.
   ## Usage

1. Navigate to the signup page (`/signup`) to create a new account.
2. Once signed up, you can proceed to the search page (`/search`) to search.
3. if logging you can utilize the search functionality provided on the search page (`/search`) to search for specific terms within paragraphs.
4. Explore additional pages within the app for other functionalities.

## App Structure

### MyApp

- `signup`: Page for user registration.
- `login`: Page for user authentication.
- `home`: Landing page with the search functionality.
- `search` for search the word from paragraph
- Other pages: Add more pages for additional functionalities as needed.
### URL:
    present  in inside of search/url
## Contributors

- [Swati Kumari Singh](https://github.com/swati07010/Codemonk1)
