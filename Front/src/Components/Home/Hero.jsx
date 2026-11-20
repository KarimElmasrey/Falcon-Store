import { Link } from "react-router-dom";
import { ShoppingCart, Sparkles, ArrowRight } from "lucide-react";
import heroImage from "../../assets/bgHero.png";

const Hero = () => {
  return (
    <section
      className="
        relative w-full min-h-[90vh] p-2 overflow-hidden
        bg-[#050816] text-white flex items-center
      "
    >
      {/* Background Overlays */}
      <div className="absolute top-20 right-0 w-[600px] h-[600px] bg-cyan-500/20 rounded-full blur-[180px] pointer-events-none" />
      <div className="absolute bottom-0 left-0 w-[500px] h-[500px] bg-pink-500/15 rounded-full blur-[180px] pointer-events-none" />
      <div className="absolute top-20 left-10 w-72 h-72 bg-cyan-500/20 rounded-full blur-[120px] pointer-events-none" />

      <div
        className="
          relative z-10 max-w-7xl mx-auto px-6 sm:px-10
          flex flex-col-reverse lg:flex-row items-center gap-12 lg:gap-20 py-12
        "
      >
        {/* Content Section */}
        <div className="flex-1 text-center lg:text-left space-y-8">
          {/* Badge */}
          <div className="inline-flex items-center gap-2 px-5 py-3 rounded-full bg-cyan-500/10 border border-cyan-400/20 bg-gradient-to-r from-cyan-400 to-pink-500 bg-clip-text text-transparent font-semibold">
            <Sparkles className="w-5 h-5 text-cyan-400" />
            NEW COLLECTION 2026
          </div>

          {/* Title */}
          <h1 className="text-5xl sm:text-6xl lg:text-8xl font-extrabold leading-tight">
            Elevate Your{" "}
            <span className="bg-gradient-to-r from-cyan-400 to-pink-500 bg-clip-text text-transparent">
              Style
            </span>
          </h1>

          {/* Description */}
          <p className="text-slate-400 text-base sm:text-lg lg:text-xl leading-relaxed max-w-xl mx-auto lg:mx-0">
            Premium fashion collections designed for modern people who value
            elegance, comfort and confidence.
          </p>

          {/* Buttons */}
          <div className="flex flex-col sm:flex-row items-center justify-center lg:justify-start gap-4 sm:gap-6 pt-4">
            <Link
              to="/shop"
              className="flex items-center justify-center gap-3 w-full sm:w-auto px-8 py-4 rounded-xl bg-gradient-to-r from-cyan-500 to-pink-500 text-white font-bold text-lg shadow-xl shadow-cyan-500/20 hover:scale-105 hover:shadow-cyan-500/40 transition-all duration-300"
            >
              <ShoppingCart className="w-6 h-6" />
              Shop Now
            </Link>

            <Link
              to="/categories"
              className="flex items-center justify-center gap-3 w-full sm:w-auto px-8 py-4 rounded-xl bg-[#0B1220] border border-slate-700 text-white font-bold text-lg hover:bg-white/10 hover:scale-105 transition-all duration-300"
            >
              Browse Categories
              <ArrowRight className="w-5 h-5" />
            </Link>
          </div>

          {/* Stats */}
          <div className="flex justify-around lg:-translate-x-12 sm:gap-12 pt-8">
            <div>
              <h3 className="text-2xl sm:text-3xl font-bold text-cyan-400">15K+</h3>
              <p className="text-slate-400 text-sm sm:text-base">Customers</p>
            </div>
            <div>
              <h3 className="text-2xl sm:text-3xl font-bold text-pink-500">5000+</h3>
              <p className="text-slate-400 text-sm sm:text-base">Products</p>
            </div>
            <div>
              <h3 className="text-2xl sm:text-3xl font-bold text-cyan-400">4.9</h3>
              <p className="text-slate-400 text-sm sm:text-base">Rating</p>
            </div>
          </div>
        </div>

        {/* Image & Shapes Section */}
        <div
          className="
            flex-1 relative w-full max-w-[300px] sm:max-w-[400px] md:max-w-[500px] lg:max-w-[650px]
            mx-auto mt-8 lg:mt-0 aspect-square flex items-center justify-center
          "
        >
          {/* Background Shapes Wrapper 
            حطينا هنا نفس أبعاد ومقاسات الصورة عشان الدوائر تتحرك وتكبر معاها بالظبط
          */}
          <div
            className="
              absolute inset-0 z-0
              scale-[1.25] lg:scale-[1.30]
              -translate-y-4 
              pointer-events-none
            "
          >
            {/* Cyan Half Circle */}
            <div
              className="
                absolute inset-0 rounded-full border-[3px] lg:border-4 border-cyan-400
                shadow-[0_0_30px_#22d3ee] lg:shadow-[0_0_60px_#22d3ee] opacity-90
                [clip-path:inset(0_50%_0_0)] sm:-translate-x-4 lg:-translate-x-0
              "
            />

            {/* Pink Half Circle */}
            <div
              className="
                absolute inset-0 rounded-full border-[3px] lg:border-4 border-pink-500
                shadow-[0_0_30px_#ec4899] lg:shadow-[0_0_60px_#ec4899] opacity-90
                [clip-path:inset(0_0_0_50%)] sm:translate-x-4 lg:translate-x-0
              "
            />

            {/* Cyan Glow Background */}
            <div className="absolute left-0 top-1/2 -translate-y-1/2 w-1/2 h-1/2 rounded-full bg-cyan-400/20 blur-[60px] lg:blur-[100px]" />

            {/* Pink Glow Background */}
            <div className="absolute right-0 top-1/2 -translate-y-1/2 w-1/2 h-1/2 rounded-full bg-pink-500/20 blur-[60px] lg:blur-[100px]" />
          </div>

          {/* Models Image */}
          <img
            src={heroImage}
            alt="Models"
            className="
              relative z-20 w-full h-full object-cover
              scale-[1.15] sm:scale-125 lg:scale-[1.45]
              drop-shadow-[0_20px_40px_rgba(0,0,0,.5)]
              select-none pointer-events-none 
              -translate-y-8 -translate-x-10 xl:-translate-x-22
            "
          />
        </div>
      </div>
    </section>
  );
};

export default Hero;