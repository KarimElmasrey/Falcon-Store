import { useContext } from "react";
import { ShopContext } from "../../Context/ShopContext";

export default function OrderSummary() {

    const { getTotalCartAmount } = useContext(ShopContext);

    const subtotal = getTotalCartAmount();

    const shipping = subtotal > 0 ? 0 : 0;

    const total = subtotal + shipping;

    return (

        <div
            className="
                bg-[#0B1220]
                border
                border-cyan-500/10
                rounded-2xl
                p-6
                sticky
                top-24
            "
        >

            <h2
                className="
                    text-2xl
                    font-bold
                    text-white
                    mb-8
                "
            >
                Order Summary
            </h2>

            <div className="space-y-5">

                <div className="flex justify-between">

                    <span className="text-gray-400">

                        Subtotal

                    </span>

                    <span className="text-white font-semibold">

                        ${subtotal.toFixed(2)}

                    </span>

                </div>

                <div className="flex justify-between">

                    <span className="text-gray-400">

                        Shipping

                    </span>

                    <span className="text-green-400">

                        Free

                    </span>

                </div>

                <hr className="border-cyan-500/10" />

                <div className="flex justify-between">

                    <span
                        className="
                            text-white
                            text-xl
                            font-bold
                        "
                    >
                        Total
                    </span>

                    <span
                        className="
                            text-cyan-400
                            text-xl
                            font-bold
                        "
                    >
                        ${total.toFixed(2)}
                    </span>

                </div>

                <button
                    className="
                        mt-8
                        w-full

                        bg-cyan-500
                        hover:bg-cyan-400

                        transition-all
                        duration-300

                        py-4

                        rounded-xl

                        text-white
                        font-semibold

                        hover:scale-[1.02]
                        active:scale-95
                    "
                >

                    Proceed To Checkout

                </button>

            </div>

        </div>

    );

}