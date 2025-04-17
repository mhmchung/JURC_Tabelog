import React, { useState } from 'react';

const restaurantsData = [
  { id: 1, name: 'Sushi Zen', cuisine: 'Japanese', image: 'https://source.unsplash.com/800x600?sushi', description: 'Best sushi in town!' },
  { id: 2, name: 'Pizza Roma', cuisine: 'Italian', image: 'https://source.unsplash.com/800x600?pizza', description: 'Authentic Italian pizza.' },
  { id: 3, name: 'Burger Joint', cuisine: 'American', image: 'https://source.unsplash.com/800x600?burger', description: 'Juicy burgers and crispy fries.' }
];

function App() {
  const [selected, setSelected] = useState(null);

  return (
    <div style={{ padding: '2rem', maxWidth: '960px', margin: '0 auto' }}>
      <h1>JURC Restaurant Reviews</h1>
      <div style={{ display: 'flex', gap: '1rem' }}>
        {restaurantsData.map(restaurant => (
          <div key={restaurant.id} style={{ border: '1px solid #ccc', borderRadius: '10px', overflow: 'hidden', width: '30%' }}>
            <img src={restaurant.image} alt={restaurant.name} style={{ width: '100%', height: '180px', objectFit: 'cover' }} />
            <div style={{ padding: '1rem' }}>
              <h2>{restaurant.name}</h2>
              <p>{restaurant.cuisine}</p>
              <button onClick={() => setSelected(restaurant)}>View Details</button>
            </div>
          </div>
        ))}
      </div>
      {selected && (
        <div style={{ marginTop: '2rem' }}>
          <h2>{selected.name}</h2>
          <img src={selected.image} alt={selected.name} style={{ width: '100%', height: '300px', objectFit: 'cover' }} />
          <p>{selected.description}</p>
          <button style={{ marginRight: '1rem' }}>Book Now</button>
          <button>Check Reviews</button>
        </div>
      )}
    </div>
  );
}

export default App;
