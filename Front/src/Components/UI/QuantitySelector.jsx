export default function QuantitySelector({
    quantity,
    setQuantity,
    stock,
    showTitle = true,
}) {

    const decreaseQuantity = () => {
        setQuantity(prev => Math.max(1, prev - 1));
    };

    const increaseQuantity = () => {
        setQuantity(prev => Math.min(stock, prev + 1));
    };

    return (

        <div>

            {showTitle && (
                <h3
                    className="
                        text-white
                        font-semibold
                        mb-3
                    "
                >
                    Quantity
                </h3>
            )}

            <div
                className="
                    flex
                    items-center
                    gap-4
                "
            >

                <button
                    onClick={decreaseQuantity}
                    className="
                        w-10
                        h-10
                        rounded-lg
                        bg-white
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
                        text-white
                        font-bold
                    "
                >
                    {quantity}
                </span>

                <button
                    onClick={increaseQuantity}
                    className="
                        w-10
                        h-10
                        rounded-lg
                        bg-white
                        border
                        border-cyan-500/10
                        hover:bg-cyan-500
                        transition
                    "
                >
                    +
                </button>

            </div>

        </div>

    );

}