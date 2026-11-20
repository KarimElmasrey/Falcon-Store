import { useContext } from "react";
import { ShoppingCart } from "lucide-react";
import { ShopContext } from "../../Context/ShopContext";

export default function AddToCartButton({
    product,
    quantity = 1,
}) {

    const { addToCart } = useContext(ShopContext);

    const handleAdd = (e) => {

        e.preventDefault();
        e.stopPropagation();

        addToCart(
            product._id,
            quantity
        );

    };

    return (

        <button
            onClick={handleAdd}
            disabled={product.stock === 0}
            className={`
                flex-1

                flex
                items-center
                justify-center
                gap-2

                py-3

                rounded-xl

                font-semibold

                transition-all
                duration-300

                ${
                    product.stock === 0
                        ? "bg-gray-700 text-gray-400 cursor-not-allowed"
                        : "bg-cyan-500 hover:bg-cyan-400 text-white hover:scale-105 active:scale-95"
                }
            `}
        >

            <ShoppingCart size={18} />

            {
                product.stock === 0
                    ? "Out Of Stock"
                    : "Add To Cart"
            }

        </button>

    );

}