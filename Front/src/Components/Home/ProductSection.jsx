import { Link } from "react-router-dom";
import { ArrowRight } from "lucide-react";

import ProductCard from "../Products/ProductCard";

export default function ProductSection({
    title,
    products,
    viewAllLink,
}) {
    return (
        <section className="max-w-7xl mx-auto px-6 py-16">

            {/* Header */}

            <div className="flex items-center justify-between mb-10">

                <h2 className="text-4xl font-bold text-white">
                    {title}
                </h2>

                <Link
                    to={viewAllLink}
                    className="
                        group
                        flex
                        items-center
                        gap-2

                        text-cyan-400
                        hover:text-white

                        transition-all
                    "
                >
                    View All

                    <ArrowRight
                        size={18}
                        className="
                            transition-transform
                            group-hover:translate-x-1
                        "
                    />

                </Link>

            </div>

            {/* Products */}

            <div
                className="
                    grid

                    gap-8

                    grid-cols-1

                    sm:grid-cols-2

                    lg:grid-cols-3

                    xl:grid-cols-4
                "
            >

                {products.map((product) => (

                    <ProductCard
                        key={product._id}
                        product={product}
                    />

                ))}

            </div>

        </section>
    );
}