import { Link, useLocation } from "react-router-dom";
import {
  House,
  ShoppingBag,
  Mail,
  Heart,
} from "lucide-react";

const menuItemsData = [
  {
    name: "Home",
    path: "/",
    icon: House,
  },
  {
    name: "Shop",
    path: "/shop",
    icon: ShoppingBag,
  },
  {
    name: "Favorites",
    path: "/favorites",
    icon: Heart,
  },
  {
    name: "Contact",
    path: "/contact",
    icon: Mail,
  },
];

export default function MenuItems({
  setsideBarOpen,
  isMobile,
}) {
  const location = useLocation();

  return (
    <div
      className={`flex ${
        isMobile
          ? "flex-col items-start gap-6"
          : "items-center gap-8"
      }`}
    >
      {menuItemsData.map(({ name, path, icon: Icon }) => {
        const isActive = location.pathname === path;

        return (
          <Link
            key={path}
            to={path}
            onClick={() => {
              if (isMobile && setsideBarOpen) {
                setsideBarOpen(false);
              }
            }}
            className={`
              group
              relative
              flex
              items-center
              gap-2

              font-medium

              transition-all
              duration-300

              ${
                isActive
                  ? "text-cyan-400"
                  : "text-slate-300 hover:text-cyan-400"
              }
            `}
          >
            <Icon
              className="
                w-5
                h-5

                group-hover:scale-110
                transition-all
                duration-300
              "
            />

            <span>{name}</span>

            {/* Active Indicator */}
            <span
              className={`
                absolute
                -bottom-2
                left-0

                h-[2px]

                bg-gradient-to-r
                from-cyan-400
                to-pink-500

                transition-all
                duration-300

                ${
                  isActive
                    ? "w-full"
                    : "w-0 group-hover:w-full"
                }
              `}
            />
          </Link>
        );
      })}
    </div>
  );
}
