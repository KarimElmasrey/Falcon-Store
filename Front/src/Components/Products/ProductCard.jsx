import { Link } from "react-router-dom";

import Rating from "./Rating";
import Price from "./Price";
import Badge from "../UI/Badge";
import FavoriteButton from "./FavoriteButton";
import AddToCartButton from "../Cart/AddToCartButton";

export default function ProductCard({ product }) {
    return (
        <Link
            to={`/product/${product._id}`}
            className="block"
        >
            <div
                className="
                    group
                    relative
                    bg-[#0B1120]
                    rounded-3xl
                    overflow-hidden
                    border
                    border-cyan-500/10
                    hover:border-cyan-400/40
                    transition-all
                    duration-300
                "
            >
                {/* Favorite Button */}
                <FavoriteButton
                    productId={product._id}
                />

                {/* Product Image */}
                <div className="relative overflow-hidden">

                    {/* Discount Badge */}
                    {product.oldPrice > product.price && (
                        <Badge
                            text={`-${Math.round(
                                ((product.oldPrice - product.price) /
                                    product.oldPrice) *
                                    100
                            )}%`}
                        />
                    )}

                    <img
                        src={product.image}
                        alt={product.name}
                        className="
                            w-full
                            h-72
                            object-cover
                            group-hover:scale-110
                            transition-transform
                            duration-500
                        "
                    />
                </div>

                <div className="p-5">

                    {/* Category + Rating */}
                    <div className="flex items-center justify-between">

                        <span
                            className="
                                text-xs
                                font-semibold
                                uppercase
                                tracking-wider
                                text-cyan-400
                            "
                        >
                            {product.category}
                        </span>

                        <Rating
                            rating={product.rating}
                            reviews={product.reviews}
                        />

                    </div>

                    {/* Product Name */}
                    <h3
                        className="
                            mt-4
                            text-white
                            text-lg
                            font-semibold
                            line-clamp-2
                            leading-7
                        "
                    >
                        {product.name}
                    </h3>

                    {/* Price + Add To Cart */}
                    <div className="mt-6 flex items-center justify-between">

                        <Price
                            price={product.price}
                            oldPrice={product.oldPrice}
                        />

                        <AddToCartButton
                            product={product}
                        />

                    </div>

                </div>

            </div>
        </Link>
    );
}