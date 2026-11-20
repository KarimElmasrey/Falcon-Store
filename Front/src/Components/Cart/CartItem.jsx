import { useContext } from "react";
import { Trash2 } from "lucide-react";

import { ShopContext } from "../../Context/ShopContext";

export default function CartItem({ product, quantity }) {

   const { removeFromCart } = useContext(ShopContext);

    return (

        <div
            className="
                flex
                items-center
                gap-6

                bg-[#0B1220]

                border
                border-cyan-500/10

                rounded-2xl

                p-5
            "
        >

            <img
                src={product.image}
                alt={product.name}
                className="
                    w-28
                    h-28

                    object-cover

                    rounded-xl
                "
            />

            <div className="flex-1">

                <h3
                    className="
                        text-white
                        font-bold
                        text-lg
                    "
                >
                    {product.name}
                </h3>

                <p
                    className="
                        text-cyan-400
                        mt-2
                    "
                >
                    ${product.price}
                </p>

                <div className="mt-5">

                    <span
                        className="
                            inline-flex
                            items-center

                            px-3
                            py-1

                            rounded-full

                            bg-cyan-500/10
                            text-cyan-400

                            text-sm
                            font-medium
                        "
                    >
                        Qty: {quantity}
                    </span>

                </div>

            </div>

            <div
                className="
                    flex
                    flex-col
                    items-end
                    gap-4
                "
            >

                <button

                    onClick={() =>
                        removeFromCart(product._id, true)
                    }

                    className="
                        text-red-500

                        hover:text-red-400

                        transition
                    "
                >

                    <Trash2 size={22} />

                </button>

                <p
                    className="
                        text-white
                        font-bold
                    "
                >

                    $

                    {(product.price * quantity).toFixed(2)}

                </p>

            </div>

        </div>

    );

}