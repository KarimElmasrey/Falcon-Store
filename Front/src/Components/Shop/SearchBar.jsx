import { Search } from "lucide-react";

export default function SearchBar({
    value,
    onChange,
}) {
    return (
        <div className="relative">

            <Search
                size={18}
                className="
                    absolute
                    left-4
                    top-1/2
                    -translate-y-1/2
                    text-gray-400
                "
            />

            <input
                type="text"
                placeholder="Search products..."

                value={value}

                onChange={onChange}

                className="
                    w-full

                    rounded-xl

                    bg-[#0B1120]

                    border
                    border-cyan-500/10

                    py-3
                    pl-11
                    pr-4

                    text-white

                    outline-none

                    focus:border-cyan-400
                "
            />

        </div>
    );
}