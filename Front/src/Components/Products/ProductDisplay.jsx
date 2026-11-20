import { useState, useContext } from 'react';
import { ShopContext } from '../../Context/ShopContext';
import ProductCard from "./ProductCard";

// 👇 نحط الـ Array هنا
const filters = [
  "All",
  "Men",
  "Women",
  "Kids",
  "Accessories",
  "Cosmetics",
];

export default function ProductDisplay() {
  // * Logic *
  const { allProducts } = useContext(ShopContext);
  const [activeFilter, setActiveFilter] = useState("All");

  const filteredProducts =
          activeFilter === "All"
            ? allProducts
            : allProducts.filter((product) => product.category === activeFilter);

            console.log("Filtered Products:", filteredProducts); // Debugging line

  // * UI *
  return (
    <section className="bg-[#050816] py-20">

      <div className="max-w-7xl mx-auto px-6">

        {/* Header */}

        <div className="flex items-center justify-between">

          <div>
            <p className="text-cyan-400 uppercase tracking-[4px] text-sm">
              Our Collection
            </p>

            <h2 className="text-white text-4xl font-bold mt-2">
              Featured Products
            </h2>
          </div>

          <button
            className="
            text-gray-400
            hover:text-cyan-400
            transition
            duration-300"
          >
            View All
          </button>

        </div>

        {/* 👇 نحط الفلاتر هنا */}

        <div className="flex flex-wrap justify-center gap-4 mt-3">

          {filters.map((filter) => (

            <button
              key={filter}
              onClick={() => setActiveFilter(filter)}
              className={`
                px-5
                py-2
                rounded-full
                border
                transition-all
                duration-300

                ${
                  activeFilter === filter
                    ? "bg-cyan-500 border-cyan-500 text-white"
                    : "border-gray-700 text-gray-300 hover:border-cyan-400 hover:text-white"
                }
              `}
            >
              {filter}
            </button>

          ))}

        </div>

        {/* Products Grid */}
        <div
          className="
            mt-13
            grid
            grid-cols-1
            sm:grid-cols-2
            lg:grid-cols-3
            xl:grid-cols-4
            gap-8"
        >

          {filteredProducts.map((product) => (

              <ProductCard
                key={product._id}
                product={product}
              />

          ))}

        </div>

      </div>

    </section>
  );
}