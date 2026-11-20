import Hero from "../Components/Home/Hero";
import Categories from "../Components/Home/Categories";
import ProductSection from "../Components/Home/ProductSection";

import { all_products } from "../assets/data";

export default function Home() {

    const newArrivals = all_products.slice(0, 8);

    const bestSellers = all_products.slice(8, 16);

    return (
        <>
            <section>
              <Hero />
            </section>
            
            <Categories />

            <ProductSection
                title="New Arrivals"
                products={newArrivals}
                viewAllLink="/shop"
            />

            <ProductSection
                title="Best Sellers"
                products={bestSellers}
                viewAllLink="/shop"
            />

        </>
    );
}