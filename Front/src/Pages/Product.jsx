import { useState } from "react";
import { useParams } from "react-router-dom";

import useCart from "../Hooks/useCart";

import ProductGallery from "../Components/ProductDetails/ProductGallery";
import ProductInfo from "../Components/ProductDetails/ProductInfo";
import ProductDescription from "../Components/ProductDetails/ProductDescription";
import ProductPrice from "../Components/ProductDetails/ProductPrice";
import ProductActions from "../Components/ProductDetails/ProductActions";

export default function Product() {

    const { productId } = useParams();

    const { allProducts } = useCart();

    const [quantity, setQuantity] = useState(1);

    const product = allProducts.find(
        (item) => item._id === productId
    );

    if (!product) {
        return (
            <section
                className="
                    min-h-screen
                    bg-[#050816]
                    flex
                    flex-col
                    items-center
                    justify-center
                    text-white
                "
            >
                <h2 className="text-3xl font-bold">
                    Product Not Found
                </h2>

                <p className="mt-3 text-gray-400">
                    The product you're looking for doesn't exist.
                </p>
            </section>
        );
    }

    return (
        <section
            className="
                min-h-screen
                bg-[#050816]
                text-white
                py-12
            "
        >
            <div
                className="
                    max-w-7xl
                    mx-auto
                    px-6

                    grid
                    lg:grid-cols-2
                    gap-12
                "
            >

                <ProductGallery
                    product={product}
                />

                <div>

                    <ProductInfo
                        product={product}
                    />

                    <ProductDescription
                        product={product}
                    />

                    <ProductPrice
                        product={product}
                    />

                    <ProductActions
                        product={product}
                        quantity={quantity}
                        setQuantity={setQuantity}
                    />

                </div>

            </div>

        </section>
    );

}