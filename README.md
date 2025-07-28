# 🎬 Top Movies - Movie Rating Application

> A Flask-based web application that allows users to search for movies, add them to a personal collection, and rate/review them. The app integrates with The Movie Database (TMDB) API to fetch movie information and provides a beautiful, responsive interface using Bootstrap.

---

## 📋 Table of Contents

- [✨ Features](#-features)
- [🛠️ Tech Stack](#️-technologies-used)
- [📋 Prerequisites](#-prerequisites)
- [🚀 Quick Start](#-installation)
- [🎯 How to Use](#-usage)
- [📁 Project Structure](#-project-structure)
- [🗄️ Database Choice](#️-database-choice)
- [🔧 Configuration](#-configuration)
- [🎨 Features Deep Dive](#-features-in-detail)
- [🐛 Troubleshooting](#-troubleshooting)
- [🙏 Acknowledgments](#-acknowledgments)

---

## ✨ Features

| Feature | Description |
|---------|-------------|
| 🎥 **Movie Search** | Search for movies using the TMDB API |
| 📚 **Movie Collection** | Add movies to your personal collection |
| ⭐ **Rating System** | Rate movies on a scale of 0-10 with validation |
| 📝 **Review System** | Add personal reviews for each movie |
| 🏆 **Ranking System** | Automatic ranking based on ratings |
| 📱 **Responsive Design** | Beautiful UI using Bootstrap 5 |
| ✅ **Form Validation** | Input validation with error messages |
| 💾 **Database Storage** | SQLite database to persist movie data |


---

## 🛠️ Technologies Used

<div align="center">

| Category | Technology |
|----------|------------|
| 🐍 **Backend** | Flask (Python web framework) |
| 🗄️ **Database** | SQLAlchemy with SQLite |
| 🎨 **Frontend** | Bootstrap 5 for responsive design |
| 📋 **Forms** | WTForms for form handling and validation |
| 🌐 **API** | The Movie Database (TMDB) API |
| 🎯 **Styling** | Custom CSS with Bootstrap components |

</div>

---

## 📋 Prerequisites

Before running this application, you need:

1. **🐍 Python 3.7+** installed on your system
2. **🔑 TMDB API Key** - Get a free API key from [The Movie Database](https://www.themoviedb.org/settings/api)
3. **⚙️ Environment Variables** set up (see Installation section)

---

## 🚀 Installation

### 1️⃣ Clone the Repository
```bash
git clone <your-repository-url>
cd top-movies
```

### 2️⃣ Create Virtual Environment
```bash
python -m venv .venv
```

### 3️⃣ Activate Virtual Environment

<details>
<summary><b>Windows</b></summary>

```bash
.venv\Scripts\activate
```

</details>

<details>
<summary><b>macOS/Linux</b></summary>

```bash
source .venv/bin/activate
```

</details>

### 4️⃣ Install Dependencies
```bash
pip install -r requirements.txt
```

### 5️⃣ Set Up Environment Variables

Create a `.env` file in the root directory with the following variables:

```env
FLASK_KEY=your_flask_secret_key_here
MOVIE_DB_API_KEY=your_tmdb_api_key_here
MOVIE_DB_AUTH_KEY=your_tmdb_auth_key_here
MOVIE_DB_URI=sqlite:///movies.db
```

#### 🔑 How to get TMDB API keys:

1. Go to [The Movie Database](https://www.themoviedb.org/settings/api)
2. Create an account and request an API key
3. Use the API key (v3) for `MOVIE_DB_API_KEY`
4. Use the Bearer token for `MOVIE_DB_AUTH_KEY`

### 6️⃣ Initialize Database
The database will be automatically created when you run the application for the first time.

---

## 🎯 Usage

### 🚀 Starting the Application
```bash
python main.py
```

The application will be available at `http://localhost:5000`

### 📱 How to Use the Application

| Page | Description |
|------|-------------|
| 🏠 **Home Page** (`/`) | View all your rated movies, automatically ranked by rating. Edit or delete existing movies. |
| ➕ **Add Movie** (`/add`) | Search for movies by title and select from search results. Movie will be added to your collection. |
| ✏️ **Edit Movie** (`/edit`) | Rate movies on a scale of 0-10 and add personal reviews. Form validation ensures proper input. |
| 🗑️ **Delete Movie** (`/delete`) | Remove movies from your collection. |

---

## 📁 Project Structure

```
top-movies/
├── 🐍 main.py                 # Main Flask application
├── 📦 requirements.txt        # Python dependencies
├── 📖 README.md              # This file
├── 🔐 .env                   # Environment variables (create this)
├── 📄 templates/             # HTML templates
│   ├── 🏗️ base.html         # Base template
│   ├── 🏠 index.html        # Home page
│   ├── ➕ add.html          # Add movie page
│   ├── ✏️ edit.html         # Edit movie page
│   └── 🎯 select.html       # Movie selection page
├── 🎨 static/               # Static files
│   ├── 🎨 css/             # Stylesheets
│   └── 🖼️ assets/          # Images and other assets
├── 💾 instance/             # Database files (auto-generated)
└── 🐍 .venv/               # Virtual environment
```

## 🗄️ Database Choice

This project uses **SQLite** for simplicity and ease of setup. While PostgreSQL would be more suitable for production deployment, SQLite was chosen because:

| ✅ **Easy for others to run locally** | No database server setup required |
| ✅ **Perfect for learning/portfolio** | Demonstrates Flask + SQLAlchemy fundamentals |
| ✅ **Quick development** | Zero configuration needed |
| ✅ **GitHub-friendly** | Anyone can clone and run immediately |

> **💡 Note**: For production deployment, this would be migrated to PostgreSQL using the same SQLAlchemy models.
---

## 🔧 Configuration

### Environment Variables

| Variable | Description | Required |
|----------|-------------|----------|
| `FLASK_KEY` | Flask secret key for session management | ✅ Yes |
| `MOVIE_DB_API_KEY` | TMDB API key for movie data | ✅ Yes |
| `MOVIE_DB_AUTH_KEY` | TMDB Bearer token for API requests | ✅ Yes |
| `MOVIE_DB_URI` | Database URI (defaults to SQLite) | ❌ No |

### Database Schema

The application uses a `Movie` table with the following fields:

| Field | Type | Description |
|-------|------|-------------|
| `id` | Integer | Primary key |
| `title` | String(250) | Movie title (unique) |
| `year` | Integer | Release year |
| `description` | String(500) | Movie overview |
| `ranking` | Integer | Automatic ranking based on rating |
| `rating` | Float | User rating (0-10) |
| `review` | String(250) | User review text |
| `image_url` | String(250) | Movie poster URL |

---

## 🎨 Features in Detail

### ✅ Form Validation
- Rating must be a number between 0 and 10
- All fields are required
- Error messages are displayed to users

### 🌐 API Integration
- Searches TMDB for movie titles
- Fetches detailed movie information
- Retrieves movie posters and metadata

### 📱 Responsive Design
- Mobile-friendly interface
- Bootstrap 5 components
- Clean and modern UI

---

## 🐛 Troubleshooting

### Common Issues

<details>
<summary><b>🔑 API Key Errors</b></summary>

- Ensure your TMDB API keys are correct
- Check that environment variables are properly set

</details>

<details>
<summary><b>💾 Database Issues</b></summary>

- Delete the `instance/movies.db` file to reset the database
- Ensure write permissions in the project directory

</details>

<details>
<summary><b>📦 Import Errors</b></summary>

- Make sure virtual environment is activated
- Run `pip install -r requirements.txt` again

</details>

<details>
<summary><b>🔌 Port Already in Use</b></summary>

- Change the port in `main.py` or kill the process using the port

</details>

---

## 📝 License

This project is open source and available under the [MIT License](LICENSE).

---

## 🙏 Acknowledgments

| Resource | Description |
|----------|-------------|
| [The Movie Database (TMDB)](https://www.themoviedb.org/) | For providing the movie data API |
| [Bootstrap](https://getbootstrap.com/) | For the responsive UI components |
| [Flask](https://flask.palletsprojects.com/) | For the web framework |
| [WTForms](https://wtforms.readthedocs.io/) | For form handling |

---

<div align="center">

# 🎬 Happy Movie Rating! ✨

</div>