import React, { useState } from 'react';
import './App.css';
import Hero from './components/Hero';
import SearchBar from './components/SearchBar';
import MovieCard from './components/MovieCard';
import SearchResults from './components/SearchResults';

const API_BASE_URL = 'http://localhost:8000';

function App() {
  const [activeTab, setActiveTab] = useState('omdb');
  const [movieData, setMovieData] = useState(null);
  const [searchResults, setSearchResults] = useState(null);
  const [imdbData, setImdbData] = useState(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState(null);

  const handleSearch = async (query, year) => {
    setLoading(true);
    setError(null);
    setMovieData(null);
    setSearchResults(null);
    setImdbData(null);

    try {
      if (activeTab === 'omdb') {
        const params = new URLSearchParams();
        params.append('title', query);
        if (year) params.append('year', year);
        
        const response = await fetch(`${API_BASE_URL}/movies/omdb?${params}`);
        if (!response.ok) throw new Error('Movie not found');
        const data = await response.json();
        setMovieData(data);
      } else if (activeTab === 'serper') {
        const params = new URLSearchParams();
        params.append('query', query);
        params.append('num_results', 10);
        
        const response = await fetch(`${API_BASE_URL}/search/serper?${params}`);
        if (!response.ok) throw new Error('Search failed');
        const data = await response.json();
        setSearchResults(data);
      } else if (activeTab === 'imdb') {
        const params = new URLSearchParams();
        params.append('title', query);
        if (year) params.append('year', year);
        
        const response = await fetch(`${API_BASE_URL}/movies/imdb-scrape?${params}`);
        if (!response.ok) throw new Error('IMDb scrape failed');
        const data = await response.json();
        setImdbData(data);
      }
    } catch (err) {
      setError(err.message);
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="App">
      <Hero />

      <main className="container">
        <div className="tabs">
          <button
            className={`tab-button ${activeTab === 'omdb' ? 'active' : ''}`}
            onClick={() => setActiveTab('omdb')}
          >
            OMDb
          </button>
          <button
            className={`tab-button ${activeTab === 'serper' ? 'active' : ''}`}
            onClick={() => setActiveTab('serper')}
          >
            Web Search
          </button>
          <button
            className={`tab-button ${activeTab === 'imdb' ? 'active' : ''}`}
            onClick={() => setActiveTab('imdb')}
          >
            IMDb
          </button>
        </div>

        <SearchBar onSearch={handleSearch} activeTab={activeTab} />

        {error && <div className="error-message">{error}</div>}
        {loading && <div className="loading">Loading...</div>}

        {movieData && <MovieCard movie={movieData} source="OMDb" />}
        {searchResults && <SearchResults results={searchResults} />}
        {imdbData && <MovieCard movie={imdbData.imdb_data} source="IMDb" />}
      </main>
    </div>
  );
}

export default App;
