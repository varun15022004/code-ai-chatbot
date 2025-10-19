import React from 'react';

const LoadingSpinner = () => {
  return (
    <div className="inline-flex items-center">
      <div className="loading-dots">
        <div className="loading-dot"></div>
        <div className="loading-dot"></div>
        <div className="loading-dot"></div>
      </div>
    </div>
  );
};

export default LoadingSpinner;
