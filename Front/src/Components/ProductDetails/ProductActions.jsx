import AddToCartButton from "../Cart/AddToCartButton";

export default function ProductActions({
    product,
    quantity,
    setQuantity,
}) {

    return (

        <div className="mt-10">

            <h3
                className="
                    text-white
                    font-semibold
                    mb-3
                "
            >
                Quantity
            </h3>

            <div
                className="
                    flex
                    items-center
                    gap-4
                    mb-8
                "
            >

                <button
                    onClick={() =>
                        setQuantity((prev) =>
                            Math.max(1, prev - 1)
                        )
                    }
                    className="
                        w-10
                        h-10
                        rounded-lg
                        bg-[#0B1120]
                        border
                        border-cyan-500/10
                        hover:bg-cyan-500
                        transition
                    "
                >
                    -
                </button>

                <span
                    className="
                        w-10
                        text-center
                        text-xl
                        font-bold
                    "
                >
                    {quantity}
                </span>

                <button
                    onClick={() =>
                        setQuantity((prev) =>
                            Math.min(product.stock, prev + 1)
                        )
                    }
                    className="
                        w-10
                        h-10
                        rounded-lg
                        bg-[#0B1120]
                        border
                        border-cyan-500/10
                        hover:bg-cyan-500
                        transition
                    "
                >
                    +
                </button>

            </div>

            <div className="flex gap-4">

                <AddToCartButton
                    product={product}
                    quantity={quantity}
                />

                <button
                    className="
                        flex-1
                        py-3
                        rounded-xl

                        border
                        border-cyan-500

                        text-cyan-400

                        hover:bg-cyan-500/10

                        transition
                    "
                >
                    Buy Now
                </button>

            </div>

        </div>

    );

}