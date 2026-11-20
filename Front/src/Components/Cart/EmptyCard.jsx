import { ShoppingCart, ArrowRight } from "lucide-react";
import { Link } from "react-router-dom";

export default function EmptyCart() {
    return (
        <div
            className="
                flex
                flex-col
                items-center
                justify-center

                text-center

                py-24
                px-6
            "
        >
            <div
                className="
                    w-28
                    h-28

                    flex
                    items-center
                    justify-center

                    rounded-full

                    bg-cyan-500/10
                    border
                    border-cyan-500/20

                    mb-8
                "
            >
                <ShoppingCart
                    size={48}
                    className="text-cyan-400"
                />
            </div>

            <h2
                className="
                    text-3xl
                    font-bold
                    text-white
                "
            >
                Your Cart is Empty
            </h2>

            <p
                className="
                    mt-4
                    text-gray-400
                    max-w-md
                "
            >
                Looks like you haven't added any products yet.
                Start shopping and discover our latest collection.
            </p>

            <Link
                to="/"
                className="
                    mt-8

                    inline-flex
                    items-center
                    gap-2

                    bg-cyan-500
                    hover:bg-cyan-400

                    text-white
                    font-semibold

                    px-6
                    py-3

                    rounded-xl

                    transition-all
                    duration-300

                    hover:scale-105
                    active:scale-95
                "
            >
                Continue Shopping

                <ArrowRight size={18} />
            </Link>
        </div>
    );
}