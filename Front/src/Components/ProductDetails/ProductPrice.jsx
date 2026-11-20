export default function ProductPrice({ product }) {

    const discount =
        product.oldPrice - product.price;

    const discountPercentage =
        Math.round(
            (discount / product.oldPrice) * 100
        );

    return (

        <div className="mt-8">

            <div className="flex items-center gap-4">

                <span
                    className="
                        text-4xl
                        font-bold
                        text-cyan-400
                    "
                >
                    ${product.price}
                </span>

                {
                    product.oldPrice > product.price && (
                        <span
                            className="
                                text-xl
                                line-through
                                text-gray-500
                            "
                        >
                            ${product.oldPrice}
                        </span>
                    )
                }

            </div>

            {
                product.oldPrice > product.price && (

                    <p
                        className="
                            mt-3
                            text-green-400
                            font-medium
                        "
                    >
                        You Save ${discount}
                        ({discountPercentage}% OFF)
                    </p>

                )
            }

        </div>

    );

}