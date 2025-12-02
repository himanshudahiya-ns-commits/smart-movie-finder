import React from 'react';
import './SearchResults.css';

function SearchResults({ results }) {
  return (
    <div className="search-results">
      <h3 className="results-title">Search Results</h3>
      <div className="results-list">
        {results.results.map((result, index) => (
          <div key={index} className="result-item">
            <div className="result-content">
              <h4 className="result-title">{result.title}</h4>
              <p className="result-snippet">{result.snippet}</p>
              <a href={result.link} target="_blank" rel="noopener noreferrer" className="result-link">
                Visit Website
              </a>
            </div>
          </div>
        ))}
      </div>
    </div>
  );
}

export default SearchResults;
