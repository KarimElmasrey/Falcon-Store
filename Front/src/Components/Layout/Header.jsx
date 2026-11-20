import { useState, useContext } from "react";
import { Link, useLocation, useNavigate} from "react-router-dom";
import {
  ShoppingCart,
  UserRound,
  Menu,
  X,
  Search,
} from "lucide-react";

import { ShopContext } from "../../Context/ShopContext";
import MenuItems from "./MenuItems";
import logo from "../../assets/Logo2.png";

export default function Header() {
  const { cartItems, cartAnimation } = useContext(ShopContext);
  const [menuOpen, setMenuOpen] = useState(false);
  const location = useLocation();
  const isCartActive = location.pathname === "/cart";
  // تحديد حالة البحث المفتوح أو المغلق
  const [isSearchOpen, setIsSearchOpen] = useState(false);
  // حفظ كلمة البحث في state
  const [searchQuery, setSearchQuery] = useState("");
  // تعريف داله للتوجه للصفحه البحث عند الضغط على زر Enter
  const navigate = useNavigate();

  const cartItemCount = Object.values(cartItems || {}).reduce(
    (total, item) => total + (item.quantity || 0) , 0
  );

  //  دالة تنفيذ البحث
  const handleSearch = () => {
    if (searchQuery.trim() !== "") {
      // توجيه المستخدم لصفحة البحث مع تمرير الكلمة في الرابط
      navigate(`/search?q=${searchQuery}`);
      // قفل القوائم بعد البحث
      setMenuOpen(false);
      setIsSearchOpen(false);
      setSearchQuery(""); // تفريغ الحقل (اختياري)
    }
  };

  // دالة لاكتشاف الضغط على زر Enter
  const handleKeyDown = (e) => {
    if (e.key === "Enter") {
      handleSearch();
    }
  };

  return (
    <header className="relative">
      <nav
        className="
        fixed
        top-0
        left-0
        w-full
        h-20
        z-50
        bg-[#050816]
        
        border-b
        border-cyan-500/10
        "
      >
        <div className="max-w-7xl mx-auto px-6 lg:px-10 h-full">

          {/* Desktop */}
          <div className="hidden md:flex h-full items-center justify-between">

            {/* Logo */}
            <Link to="/" className="flex items-center gap-2">
              <img
                src={logo}
                alt="Falcon Shop"
                className="h-14 object-contain"
              />

              <span
                className="
                text-2xl
                font-extrabold

                bg-gradient-to-r
                from-cyan-400
                via-sky-400
                to-pink-500

                bg-clip-text
                text-transparent
                "
              >
                Falcon Shop
              </span>
            </Link>

            {/* Center Menu */}
            <div className="flex items-center gap-5">
              <MenuItems isMobile={false} />

              {/* Search Bar With Icon */}
              <div className="relative flex items-center">
                {isSearchOpen && (
                    <input 
                      type="text" 
                      autoFocus
                      value={searchQuery}
                      onChange={(e) => setSearchQuery(e.target.value)}
                      onKeyDown={handleKeyDown}
                      className="
                        bg-transparent 
                        border border-slate-700 rounded-full 
                        focus:outline-none 
                        text-slate-300 placeholder:text-slate-500 
                        px-4 py-1 pr-10 
                        w-48 transition-all duration-300
                      " 
                      placeholder="Search..." 
                    /> 
                )}

                {/* أيقونة البحث */}
                <Search
                  className={`
                    ${isSearchOpen ? 'absolute right-3' : 'relative'}
                    w-5 h-5 text-slate-400 cursor-pointer transition-all duration-300 hover:scale-110
                  `}
                  onClick={() => {
                    if (isSearchOpen && searchQuery.trim() !== "") {
                      handleSearch(); // لو الحقل مفتوح وفيه كلام، ابحث
                    } else {
                      setIsSearchOpen(!isSearchOpen); // لو فاضي، افتح/اقفل الحقل
                    }
                  }}
                />
                
              </div>
            </div>

            {/* User */}
            <div className="flex items-center gap-6">

              <Link
                to="/login"
                className="
                flex
                items-center
                gap-2

                text-slate-300
                hover:text-cyan-400

                transition-all
                "
              >
                <UserRound className="w-5 h-5" />
                Login
              </Link>

              <Link
                to="/cart"
                className={`
                flex
                items-center
                gap-2
                transition-all
                hover:text-pink-500
                ${isCartActive ? "text-pink-500" : "text-slate-300"}
                `}
              >
                {/* تم تعديل هيكل أيقونة السلة لتتوافق مع الشاشات الكبيرة */}
                <div className="relative flex items-center">
                  <ShoppingCart className={`w-5 h-5 transition-transform duration-300 ${cartAnimation ? 'animate-bounce' : 'scale-100'}`} />
                  {cartItemCount > 0 && (
                    <span
                      className="
                      absolute
                      -top-2
                      -right-2
                      w-4
                      h-4
                      rounded-full
                      flex
                      items-center
                      justify-center
                      text-[10px]
                      text-white
                      bg-gradient-to-r
                      from-cyan-500
                      to-pink-500
                      "
                    >
                      {cartItemCount}
                    </span>
                  )}
                </div>
                Cart
              </Link>

            </div>

          </div>

          {/* ------------------------------------------------------ Mobile Menu ---------------------------------------------------------- */}
          <div className="md:hidden flex items-center justify-between h-full">

            <Link to="/" className="flex items-center gap-2">
              <img
                src={logo}
                alt="Falcon Shop"
                className="h-12"
              />

              <span
                className="
                font-bold

                bg-gradient-to-r
                from-cyan-400
                to-pink-500

                bg-clip-text
                text-transparent
                "
              >
                Falcon Shop
              </span>
            </Link>

            <button
              onClick={() => setMenuOpen(!menuOpen)}
              className="text-white"
            >
              {menuOpen ? (
                <X size={30} />
              ) : (
                <Menu size={30} />
              )}
            </button>
          </div>

          {/* ------------------------------------------------- Mobile Menu ---------------------------------------------------------- */}
          {menuOpen && (
            <div
              className="
              absolute
              top-20
              left-0

              w-full

              bg-[#0B1220]
              border-t
              border-slate-800
              shadow-2xl
              "
            >
              <div className="p-6 flex flex-col gap-5">

                {/* ------------------------------------ Search Bar For Mobile --------------------------------- */}
                <div className="relative flex items-center w-full mb-2">
                  <input
                    type="text"
                    className="
                      bg-transparent 
                      border border-slate-700 rounded-full 
                      focus:outline-none focus:border-cyan-500
                      text-slate-300 placeholder:text-slate-500 
                      px-4 py-2 pr-10 
                      w-full transition-all duration-300
                    "
                    placeholder="Search..."
                  />
                  <Search className="absolute right-4 w-5 h-5 text-slate-400" />
                </div>
                

                <MenuItems
                  isMobile={true}
                  setsideBarOpen={setMenuOpen}
                />

                <Link
                  to="/login"
                  onClick={() => setMenuOpen(false)}
                  className="
                  text-slate-300
                  hover:text-cyan-400
                  w-[61px]
                  flex
                  items-center
                  gap-2
                  "
                >
                  <div className="relative">
                    <UserRound className="w-5 h-5" />
                  </div>

                  Login
                </Link>

                <Link
                  to="/cart"
                  onClick={() => setMenuOpen(false)}
                  className={`
                  hover:text-pink-500
                  flex
                  items-center
                  w-[61px]
                  gap-2
                  ${isCartActive ? "text-pink-500" : "text-slate-300"}
                  `}
                >
                  <div className="relative">
                    <ShoppingCart className="w-5 h-5" />
                    {cartItemCount > 0 && (
                      <span
                        className="
                        absolute
                        -top-2
                        -right-2
                        w-5
                        h-5
                        rounded-full
                        flex
                        items-center
                        justify-center
                        text-[10px]
                        text-white
                        bg-gradient-to-r
                        from-cyan-500
                        to-pink-500
                        "
                      >
                        {cartItemCount}
                      </span>
                    )}
                  </div>
                  Cart
                </Link>

              </div>
            </div>
          )}
        </div>
      </nav>

      <div className="h-20" />
    </header>
  );
}
