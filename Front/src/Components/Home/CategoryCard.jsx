import { Link } from "react-router-dom";
import { ArrowRight } from "lucide-react";

export default function CategoryCard({
    title,
    image,
    link,
    accent,
}) {

    const accentColors = {
        cyan: {
            text: "text-cyan-400",
            border: "hover:border-cyan-400/40",
            shadow: "hover:shadow-cyan-500/20",
        },

        pink: {
            text: "text-pink-400",
            border: "hover:border-pink-400/40",
            shadow: "hover:shadow-pink-500/20",
        },

        slate: {
            text: "text-slate-300",
            border: "hover:border-slate-300/40",
            shadow: "hover:shadow-slate-400/20",
        },

        amber: {
            text: "text-amber-400",
            border: "hover:border-amber-400/40",
            shadow: "hover:shadow-amber-500/20",
        },
    };

    const currentAccent = accentColors[accent];

    return (
        <Link
            to={link}
            className={`
                group
                relative

                overflow-hidden

                h-40

                rounded-2xl

                border
                border-white/10

                bg-[#0B1120]

                transition-all
                duration-300

                hover:-translate-y-1

                ${currentAccent.border}
                ${currentAccent.shadow}
            `}
        >
            <div className="flex h-full items-center justify-between px-6">

                <div className="z-10">

                    <h3 className="text-2xl font-bold text-white">
                        {title}
                    </h3>

                    <p className="mt-1 text-sm text-gray-400">
                        Collection
                    </p>

                    <div
                        className={`
                            mt-6

                            inline-flex
                            items-center
                            gap-2

                            transition-all
                            duration-300

                            ${currentAccent.text}
                        `}
                    >
                        <span>Shop Now</span>

                        <ArrowRight
                            size={16}
                            className="
                                transition-transform
                                duration-300
                                group-hover:translate-x-1
                            "
                        />
                    </div>

                </div>

                <img
                    src={image}
                    alt={title}
                    className="
                        absolute

                        right-0
                        bottom-0

                        h-[120%]

                        object-contain

                        transition-all
                        duration-500

                        group-hover:scale-110
                        group-hover:-translate-y-2
                    "
                />

            </div>
        </Link>
    );
}