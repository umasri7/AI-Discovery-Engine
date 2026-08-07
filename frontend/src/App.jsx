import { useState } from "react";
import { FaSearch } from "react-icons/fa";
import API from "./api/api";
import "./App.css";

function App() {

  const [query, setQuery] = useState("");
  const [products, setProducts] = useState([]);
  const [recommendations, setRecommendations] = useState([]);
  const [loading, setLoading] = useState(false);

  // Search Products
  const searchProducts = async () => {

    if (!query) return;

    try {

      setLoading(true);

      const response = await API.get(`/search?query=${query}`);

      setProducts(response.data.products);

      setRecommendations([]);

    } catch (error) {

      console.log(error);

    } finally {

      setLoading(false);

    }

  };

  // Get Recommendations
  const getRecommendations = async (productName) => {

    try {

      const response = await API.get(
        
        `/recommend?product=${productName}`
      );

      setRecommendations(response.data.recommendations);

    } catch (error) {

      console.log(error);

    }

  };

  return (

    <div className="container">

      <h1>🤖 AI Discovery Engine</h1>

      <div className="searchBox">

        <input
          type="text"
          placeholder="Search anything..."
          value={query}
          onChange={(e) => setQuery(e.target.value)}
        />

        <button onClick={searchProducts}>
          <FaSearch />
        </button>

      </div>

      {loading && <h2>Searching...</h2>}

      {/* Search Results */}

      <div className="products">

        {products.map((item) => (

          <div
            className="card"
            key={item.id}
            onClick={() => getRecommendations(item.name)}
          >

            <h2>{item.name}</h2>

            <p>{item.category}</p>

            <p>
              <b>Brand:</b> {item.brand}
            </p>

            <h3>₹ {item.price}</h3>

          </div>

        ))}

      </div>

      {/* Recommendation Section */}

      {recommendations.length > 0 && (

        <div>

          <h1>✨ Recommended Products</h1>

          <div className="products">

            {recommendations.map((item) => (

              <div
                className="card"
                key={item.id}
              >

                <h2>{item.name}</h2>

                <p>{item.category}</p>

                <p>
                  <b>Brand:</b> {item.brand}
                </p>

                <h3>₹ {item.price}</h3>

              </div>

            ))}

          </div>

        </div>

      )}

    </div>

  );

}

export default App;