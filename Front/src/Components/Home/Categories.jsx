import CategoryCard from "./CategoryCard";

import { categoriesData } from "../../assets/categoryData";

export default function Categories() {
  return (
    <section className="max-w-7xl mx-auto px-6 py-20">

      {/* Section Header */}

      <div className="mb-12">

        <h2 className="text-4xl font-bold text-white">

          Shop By Category

        </h2>

        <p className="mt-3 text-gray-400">

          Explore our collections and find your perfect style.

        </p>

      </div>

      {/* Categories Grid */}

      <div
        className="
          grid

          grid-cols-1

          md:grid-cols-2

          xl:grid-cols-4

          gap-6
        "
      >
        {categoriesData.map((category) => (

          <CategoryCard
            key={category.id}
            {...category}
          />

        ))}
      </div>

    </section>
  );
}