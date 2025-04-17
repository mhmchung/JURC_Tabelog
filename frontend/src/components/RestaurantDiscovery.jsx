import React from "react";

const RestaurantDiscovery = () => {
  return (
    <div>
      {/* Logo */}
      <div 
        className="flex justify-center items-center mt-4 mb-6"  
        style={{
          display: 'flex',
          justifyContent: 'center',
          alignItems: 'center'
        }}>
        <img
          src="/JURC_LOGO.png"
          alt="Logo"
          style={{ height: "400px", maxHeight: "400px", objectFit: "contain" }}
          className="mx-auto"
        />
      </div>

      {/* Top navigation buttons */}
      <div 
        className="flex justify-center gap-6 mb-6"
        style={{
          display: 'flex',
          justifyContent: 'center',
          alignItems: 'center'
        }}>
        {["Reserve", "Search", "Explore", "Featured", "Near Me"].map((label) => (
          <button
            key={label}
            className="px-4 py-2 text-lg font-medium bg-white shadow rounded hover:bg-gray-100 transition"
          >
            {label}
          </button>
        ))}
      </div>

      {/* Search bar row */}
      <div 
        className="flex justify-center mb-10"
        style={{
          display: 'flex',
          justifyContent: 'center',
          alignItems: 'center'
        }}>
        <div className="flex gap-4 flex-wrap justify-center">
          <input className="p-2 rounded border w-40" placeholder="Location" />
          <input className="p-2 rounded border w-40" placeholder="Keyword" />
          <input className="p-2 rounded border w-40" placeholder="Category" />
          <input type="date" className="p-2 rounded border w-40" />
          <input type="time" className="p-2 rounded border w-40" />
          <input type="number" className="p-2 rounded border w-40" placeholder="# Customers" />
        </div>
      </div>

      {/* Placeholder for future content */}
      <div 
        className="text-center text-gray-600 text-xl font-light"
        style={{
          display: 'flex',
          justifyContent: 'center',
          alignItems: 'center'
        }}>
        Content goes here...
      </div>
    </div>
  );
};

export default RestaurantDiscovery;
