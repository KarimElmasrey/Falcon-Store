// *Import files and Methods*
import {Routes , Route} from 'react-router-dom'
// ^ Pages ^
import Home from "./Pages/Home"
import Product from "./Pages/Product"
import Cart from "./Pages/Cart"
import Favorites from "./Pages/Favorites"
import Shop from "./Pages/Shop";
import Contact from "./Pages/Contact";
// import Order from "../Pages/Order"
// import Verify from "../Pages/Verify"
// import MyOrders from "../Pages/MyOrders"
// import Signup from "../Pages/Signup"
// import Login from "../Pages/Login"
// ^ Components ^
import Layout from "./Components/Layout/Layout"
// ^ ShopContext (Provider) ^
import ShopContextProvider from "./Context/ShopContext"

export default function App() {

  return (
    <ShopContextProvider>
          <Routes>
              <Route element={<Layout />}>
                  <Route path="/" element={<Home />} />

                  <Route path="/shop" element={<Shop />} />

                  <Route path="/product/:productId" element={<Product />} />

                  <Route path="/cart" element={<Cart />} />

                  <Route path="/favorites" element={<Favorites />} />

                  <Route path="/contact" element={<Contact />} />
              </Route>
          </Routes>
    </ShopContextProvider>
  )
}


