# Smart Movie Finder

A modern, full-stack application that helps users discover and search movies from multiple sources including OMDb, IMDb, and web search. Built with React frontend and FastAPI backend.

## Features

- **OMDb Search**: Search for movies using the OMDb API with optional year filtering
- **Web Search**: Perform web searches using the Serper API to find movie information
- **IMDb Scraping**: Scrape IMDb pages to get detailed movie information including ratings, cast, genres, and plots
- **Retry Logic**: Automatic retry mechanism with exponential backoff for API calls
- **CORS Enabled**: Frontend can communicate with backend across different ports
- **Responsive Design**: Works seamlessly on desktop, tablet, and mobile devices
- **Modern UI**: Beautiful purple gradient design with smooth animations and hover effects

## Tech Stack

### Backend
- **Framework**: FastAPI
- **Language**: Python 3.14
- **APIs**: OMDb, Serper
- **Scraping**: BeautifulSoup4
- **Retry Logic**: Tenacity
- **HTTP Client**: Requests
- **Environment**: Python virtual environment

### Frontend
- **Framework**: React 18.2.0
- **Language**: JavaScript (ES6+)
- **HTTP Client**: Axios
- **Styling**: CSS3 with gradients and animations
- **Build Tool**: Create React App

## Project Structure

```
smart-movie-finder/
├── app/                           # Backend
│   ├── main.py                    # FastAPI application & routes
│   ├── config.py                  # Configuration settings
│   ├── services_omdb.py          # OMDb API integration
│   ├── services_serper.py        # Serper API integration
│   ├── services_imdb.py          # IMDb scraping logic
│   └── __pycache__/
├── frontend/                      # React frontend
│   ├── public/
│   │   ├── index.html            # Main HTML file
│   │   └── images/               # Static images
│   ├── src/
│   │   ├── components/
│   │   │   ├── SearchBar.js      # Search input component
│   │   │   ├── SearchBar.css
│   │   │   ├── MovieCard.js      # Movie details display
│   │   │   ├── MovieCard.css
│   │   │   ├── SearchResults.js  # Web search results
│   │   │   ├── SearchResults.css
│   │   │   ├── Hero.js           # Hero section with image
│   │   │   └── Hero.css
│   │   ├── App.js                # Main app component
│   │   ├── App.css
│   │   ├── index.js              # React entry point
│   │   └── index.css             # Global styles
│   ├── package.json
│   └── .gitignore
├── .env                          # Environment variables
├── .gitignore
├── requirements.txt              # Python dependencies
└── README.md
```

## Installation

### Backend Setup

1. Clone the repository:
```bash
git clone https://github.com/himanshudahiya-ns-commits/smart-movie-finder.git
cd smart-movie-finder
```

2. Create and activate virtual environment:
```bash
python3 -m venv .venv
source .venv/bin/activate
```

3. Install Python dependencies:
```bash
pip install -r requirements.txt
```

4. Create `.env` file with your API keys:
```env
OMDB_API_KEY=your_omdb_api_key_here
OMDB_BASE_URL=https://www.omdbapi.com

SERPER_API_KEY=your_serper_api_key_here
SERPER_BASE_URL=https://google.serper.dev
```

### Frontend Setup

1. Navigate to frontend directory:
```bash
cd frontend
```

2. Install dependencies:
```bash
npm install
```

## Running the Application

### Start Backend
```bash
# From project root
source .venv/bin/activate
uvicorn app.main:app --reload --port 8000
```

Backend will be available at: `http://localhost:8000`

### Start Frontend
```bash
# From frontend directory
npm start
```

Frontend will be available at: `http://localhost:3001`

## API Endpoints

### Health Check
- `GET /health` - Check if API is running

### OMDb Search
- `GET /movies/omdb?title=Inception&year=2010` - Search movies by title and optional year

### Web Search
- `GET /search/serper?query=Inception+movie&num_results=10` - Search movies on web

### IMDb Scrape
- `GET /movies/imdb-scrape?title=Inception&year=2010` - Find and scrape IMDb page

## Key Features Implemented

### 1. Retry Logic
- Automatic retry mechanism on API failures
- Exponential backoff: 2s, 4s, 8s between retries
- Maximum 3 retry attempts
- Applied to all external API calls and web scraping

### 2. CORS Support
- Backend configured to accept requests from localhost:3000 and 3001
- Supports both localhost and 127.0.0.1

### 3. Error Handling
- Custom exception classes for each service
- User-friendly error messages
- Graceful fallbacks for missing data

### 4. Responsive Design
- Mobile-first approach
- Breakpoints for tablets and desktops
- Optimized for all screen sizes

## Browser Support

- Chrome (latest)
- Firefox (latest)
- Safari (latest)
- Edge (latest)

## Dependencies

### Python (Backend)
- fastapi==0.109.0
- uvicorn==0.27.0
- requests==2.31.0
- beautifulsoup4==4.12.2
- tenacity==8.2.3
- python-dotenv==1.0.0

### JavaScript (Frontend)
- react@18.2.0
- react-dom@18.2.0
- axios@1.6.0

## Environment Variables

### Backend (.env)
```
OMDB_API_KEY=          # Your OMDb API key
OMDB_BASE_URL=https://www.omdbapi.com

SERPER_API_KEY=        # Your Serper API key
SERPER_BASE_URL=https://google.serper.dev
```

## Getting API Keys

### OMDb API
1. Visit: https://www.omdbapi.com/apikey.aspx
2. Select FREE tier
3. Enter your email
4. Receive API key via email

### Serper API
1. Visit: https://serper.dev
2. Sign up for free account
3. Get API key from dashboard

## Performance Optimization

- Exponential backoff prevents API rate limiting
- Retry logic ensures resilience against temporary failures
- Clean component-based architecture for efficient renders
- CSS optimizations with gradients instead of images

## Deployment

### Backend (Production)
```bash
# Use production ASGI server
gunicorn app.main:app -w 4 -k uvicorn.workers.UvicornWorker
```

### Frontend (Production)
```bash
# Build optimized production bundle
npm run build
```

## Contributing

1. Create a new branch for features
2. Commit changes with clear messages
3. Push to remote repository
4. Create pull request

## Git Branches

- `main` - Production ready code
- `feature/serper_integration` - Serper API integration
- `feature/frontend` - Frontend development

## Known Limitations

- IMDb scraping may fail if page layout changes
- OMDb API requires subscription for premium data
- Serper has rate limits on free tier

## Future Enhancements

- User authentication and saved favorites
- Movie recommendations based on search history
- Advanced filtering and sorting options
- Dark mode toggle
- Caching layer for improved performance
- Pagination for large result sets

## Troubleshooting

### Backend Issues
- **Port already in use**: Kill process on port 8000 or use different port
- **API key errors**: Verify .env file has correct keys
- **CORS errors**: Check backend is running and CORS middleware is configured

### Frontend Issues
- **Blank page**: Clear browser cache and restart npm
- **API not connecting**: Verify backend is running on port 8000
- **Styling issues**: Check all CSS files are imported correctly

## License

ISC

## Author

Himanshu Dahiya

## Support

For issues and questions, create a GitHub issue in the repository.
