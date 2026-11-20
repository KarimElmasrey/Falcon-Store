import { useContext } from "react";
import { ShopContext } from "../Context/ShopContext";
import CartItem from "../Components/Cart/CartItem";
import OrderSummary from "../Components/Cart/OrderSummary";
import EmptyCart from "../Components/Cart/EmptyCard";

export default function Cart() {
    const {
              cartItems,
              allProducts,
          } = useContext(ShopContext);

          const isCartEmpty = Object.keys(cartItems).length === 0;

              const cartProducts = Object.entries(cartItems)
                .map(([id, quantity]) => {

                    const product = allProducts.find(
                        product => product._id === id
                    );

                    if (!product) return null;

                    return {
                        product,
                        quantity,
                    };

                })
                .filter(Boolean);

    return (

        <section
            className="
                min-h-screen
                bg-[#050816]
                py-20
            "
        >

            <div
                className="
                    max-w-7xl
                    mx-auto
                    px-6
                "
            >

                <h1
                    className="
                        text-4xl
                        font-bold
                        text-white
                        mb-12
                    "
                >

                    Shopping Cart

                </h1>

                {
                  isCartEmpty ? (

                      <EmptyCart />

                  ) : (

                        <div
                            className="
                                grid
                                lg:grid-cols-3
                                gap-10
                            "
                        >
                            <div
                                className="
                                    lg:col-span-2
                                    space-y-6
                                "
                            >
                                {
                                  cartProducts.map(({ product, quantity }) => (

                                      <CartItem

                                          key={product._id}

                                          product={product}

                                          quantity={quantity}

                                      />

                                  ))
                                }
                            </div>

                            <OrderSummary />

                        </div>

                      )
                }

            </div>

        </section>

    );

}