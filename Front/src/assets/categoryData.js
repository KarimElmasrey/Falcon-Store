import Men from "../../public/Categories/Men.jpeg";
import Women from "../../public/Categories/Women.jpeg";
import Shoes from "../../public/Categories/Shoes.jpeg";
import Accessories from "../../public/Categories/Accessories.jpeg";

export const categoriesData = [
  {
    id: 1,
    title: "Men",
    image: Men,
    accent: "cyan",
    link: "/shop?category=Men",
  },
  {
    id: 2,
    title: "Women",
    image: Women,
    accent: "pink",
    link: "/shop?category=Women",
  },
  {
    id: 3,
    title: "Shoes",
    image: Shoes,
    accent: "slate",
    link: "/shop?category=Shoes",
  },
  {
    id: 4,
    title: "Accessories",
    image: Accessories,
    accent: "amber",
    link: "/shop?category=Accessories",
  },
];