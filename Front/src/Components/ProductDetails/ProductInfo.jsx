import Rating from "../Products/Rating";

export default function ProductInfo({ product }) {
    return (
        <div>

            <span
                className="
                    text-cyan-400
                    uppercase
                    tracking-wider
                    text-sm
                    font-semibold
                "
            >
                {product.category}
            </span>

            <h1
                className="
                    mt-3
                    text-4xl
                    font-bold
                    text-white
                "
            >
                {product.name}
            </h1>

            <div className="mt-4">

                <Rating
                    rating={product.rating}
                    reviews={product.reviews}
                />

            </div>

            <div
                className="
                    mt-6
                    space-y-3
                    text-gray-300
                "
            >

                <p>

                    <span className="text-white font-semibold">

                        Brand:

                    </span>

                    {" "}
                    {product.brand}

                </p>

                <p>

                    <span className="text-white font-semibold">

                        Stock:

                    </span>

                    {" "}

                    {
                        product.stock > 0
                            ? `${product.stock} Available`
                            : "Out Of Stock"
                    }

                </p>

            </div>

        </div>
    );
}