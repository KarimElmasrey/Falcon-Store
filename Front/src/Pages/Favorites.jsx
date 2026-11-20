import { useContext } from "react";
import { ShopContext } from "../Context/ShopContext";
import ProductCard from "../Components/Products/ProductCard";

export default function Favorites() {

    const {
        allProducts,
        favorites,
    } = useContext(ShopContext);

    const favoriteProducts = allProducts.filter(product =>
        favorites.includes(product._id)
    );

    return (

        <section className="bg-[#050816] min-h-screen py-6">

            <div className="max-w-7xl mx-auto px-6">

                <h1 className="text-4xl font-bold text-white mb-12">

                    My Favorites

                </h1>

                {
                    favoriteProducts.length === 0 ?

                    (

                        <div className="text-center py-24">

                            <h2 className="text-3xl text-white font-bold">

                                No Favorites Yet

                            </h2>

                            <p className="text-gray-400 mt-4">

                                Start adding your favorite products ❤️

                            </p>

                        </div>

                    )

                    :

                    (

                        <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-8">

                            {

                                favoriteProducts.map(product => (

                                    <ProductCard
                                        key={product._id}
                                        product={product}
                                    />

                                ))

                            }

                        </div>

                    )
                }

            </div>

        </section>

    );

}