import React from 'react';
import './MovieCard.css';

function MovieCard({ movie, source }) {
  const isOmdb = source === 'OMDb';
  const isImdb = source === 'IMDb';

  return (
    <div className="movie-card">
      <div className="movie-header">
        <h2 className="movie-title">
          {isOmdb ? movie.Title : isImdb ? movie.title : movie.title}
        </h2>
        <span className="source-badge">{source}</span>
      </div>

      <div className="movie-content">
        {isOmdb && movie.Poster && movie.Poster !== 'N/A' && (
          <img src={movie.Poster} alt="Poster" className="poster" />
        )}
        {isImdb && (
          <div className="movie-details">
            <p>
              <strong>Rating:</strong> {movie.rating || 'N/A'}
            </p>
            <p>
              <strong>Genres:</strong> {movie.genres?.join(', ') || 'N/A'}
            </p>
            {movie.summary && (
              <p>
                <strong>Plot:</strong> {movie.summary}
              </p>
            )}
            {movie.top_cast && movie.top_cast.length > 0 && (
              <p>
                <strong>Cast:</strong> {movie.top_cast.join(', ')}
              </p>
            )}
          </div>
        )}

        {isOmdb && (
          <div className="movie-details">
            {movie.Year && (
              <p>
                <strong>Year:</strong> {movie.Year}
              </p>
            )}
            {movie.Rated && movie.Rated !== 'N/A' && (
              <p>
                <strong>Rated:</strong> {movie.Rated}
              </p>
            )}
            {movie.Runtime && movie.Runtime !== 'N/A' && (
              <p>
                <strong>Runtime:</strong> {movie.Runtime}
              </p>
            )}
            {movie.Director && movie.Director !== 'N/A' && (
              <p>
                <strong>Director:</strong> {movie.Director}
              </p>
            )}
            {movie.Cast && movie.Cast !== 'N/A' && (
              <p>
                <strong>Cast:</strong> {movie.Cast}
              </p>
            )}
            {movie.Genre && movie.Genre !== 'N/A' && (
              <p>
                <strong>Genre:</strong> {movie.Genre}
              </p>
            )}
            {movie.imdbRating && movie.imdbRating !== 'N/A' && (
              <p>
                <strong>IMDb Rating:</strong> {movie.imdbRating}/10
              </p>
            )}
            {movie.Plot && movie.Plot !== 'N/A' && (
              <p>
                <strong>Plot:</strong> {movie.Plot}
              </p>
            )}
          </div>
        )}
      </div>
    </div>
  );
}

export default MovieCard;
