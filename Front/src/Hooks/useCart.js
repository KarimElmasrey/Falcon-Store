import { useContext } from "react";
import { ShopContext } from "../Context/ShopContext";

export default function useCart() {
    return useContext(ShopContext);
}