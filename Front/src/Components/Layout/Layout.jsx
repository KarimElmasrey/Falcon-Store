import { Outlet } from "react-router-dom";

import Header from "./Header";
// import Footer from "./Footer";
import FalconChat from "../UI/FalconChat/FalconChat"; // تأكد من صحة مسار الملف حسب مكان حفظه الفعلي لديك

export default function Layout() {
    return (
        <>
            <Header />

            <main className="min-h-screen bg-[#050816]">
                <Outlet />
            </main>

            {/* <Footer /> */}

            {/* شات بوت Falcon Shop متفعل ويعمل في جميع الصفحات */}
            <FalconChat />
        </>
    );
}