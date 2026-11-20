import { createContext, useEffect, useState } from "react";
import { all_products } from "../assets/data";

// Create Context
// eslint-disable-next-line react-refresh/only-export-components
export const ShopContext = createContext();

const ShopContextProvider = ({ children }) => {

    // ✅ تحميل الكارت من localStorage بشكل آمن
    const [cartItems, setCartItems] = useState(() => {
        try {
            const saved = localStorage.getItem("cartItems");
            return saved ? JSON.parse(saved) : {};
        // eslint-disable-next-line no-unused-vars
        } catch (err) {
            return {};
        }
    });

    const [favorites, setFavorites] = useState(() => {
        try {
            const saved = localStorage.getItem("favorites");
            return saved ? JSON.parse(saved) : [];
        } catch {
            return [];
        }
    });

    const [allProducts] = useState(all_products);

    // ✅ حفظ الكارت في localStorage
    useEffect(() => {
        localStorage.setItem("cartItems", JSON.stringify(cartItems));
    }, [cartItems]);

    // ✅ حفظ المفضلة في localStorage
    useEffect(() => {
        localStorage.setItem(
            "favorites",
            JSON.stringify(favorites)
        );
    }, [favorites]);

    
    // Making a state for cart animation
    const [cartAnimation, setCartAnimation] = useState(false);

    // ➕ إضافة منتج
    const addToCart = (id, quantity = 1) => {

        setCartItems((prev) => ({
            ...prev,
            [id]: (prev[id] || 0) + quantity,
        }));

        setCartAnimation(true);

        setTimeout(() => {
            setCartAnimation(false);
        }, 300);

    };

    // ➖ حذف منتج
    const removeFromCart = (id, removeAll = false) => {
        setCartItems((prev) => {
            const updated = { ...prev };

            if (removeAll || updated[id] === 1) {
                delete updated[id];
            } else {
                updated[id] -= 1;
            }

            return updated;
        });
    };

    // 💖 إضافة منتج للمفضلة
    const addToFavorites = (id) => {

        setFavorites(prev => {

            if (prev.includes(id)) {

                return prev;

            }

            return [...prev, id];

        });
    };

    // 💔 إزالة منتج من المفضلة
     const removeFromFavorites = (id) => {

            setFavorites(prev =>
                prev.filter(item => item !== id)
            );

        };

    // 💖 التحقق إذا كان المنتج في المفضلة
    const isFavorite = (id) => {

        return favorites.includes(id);

    };

    // 💰 حساب الإجمالي
    const getTotalCartAmount = () => {
        return Object.entries(cartItems).reduce((total, [id, qty]) => {
            const product = allProducts.find(
                p => String(p._id) === String(id)
            );
            return total + (product ? product.price * qty : 0);
        }, 0);
    };

    const contextValue = {
        allProducts,
        cartItems,
        addToCart,
        removeFromCart,
        getTotalCartAmount,
        favorites,
        addToFavorites,
        removeFromFavorites,
        isFavorite,
        cartAnimation,
    };

    return (
        <ShopContext.Provider value={contextValue}>
            {children}
        </ShopContext.Provider>
    );
};

export default ShopContextProvider;