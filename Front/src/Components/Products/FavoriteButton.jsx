import { useContext } from "react";
import { Heart } from "lucide-react";
import { ShopContext } from "../../Context/ShopContext";

export default function FavoriteButton({ productId }) {

    const {
        isFavorite,
        addToFavorites,
        removeFromFavorites,
    } = useContext(ShopContext);

    const favorite = isFavorite(productId);

    const handleFavorite = (e) => {

        // يمنع الـ Link من الفتح
        e.preventDefault();
        e.stopPropagation();

        if (favorite) {

            removeFromFavorites(productId);

        } else {

            addToFavorites(productId);

        }

    };

    return (
        <button
            onClick={handleFavorite}
            className="
                absolute
                top-4
                right-4
                z-20

                w-11
                h-11

                flex
                items-center
                justify-center

                rounded-full

                bg-white/90
                backdrop-blur-md

                shadow-lg

                transition-all
                duration-300

                hover:scale-110
            "
        >

            <Heart
                size={20}
                className={
                    favorite
                        ? "fill-red-500 text-red-500"
                        : "text-gray-700"
                }
            />

        </button>
    );
}