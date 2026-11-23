import { useState, useEffect } from "react";

import useCart from "../Hooks/useCart";

import SearchBar from "../Components/Shop/SearchBar";
import SortDropdown from "../Components/Shop/SortDropdown";
import ProductGrid from "../Components/Shop/ProductGrid";
import FilterSidebar from "../Components/Shop/FilterSidebar";

export default function Shop() {
    const { allProducts } = useCart();

    const categoryOptions = [
        {
            label: "All",
            value: "",
        },
        ...[...new Set(allProducts.map((product) => product.category))].map(
            (category) => ({
                label: category,
                value: category,
            })
        ),
    ];

    const brandOptions = [
        {
            label: "All",
            value: "",
        },
        ...[
            ...new Set(
                allProducts.map((product) => product.brand).filter(Boolean)
            ),
        ].map((brand) => ({
            label: brand,
            value: brand,
        })),
    ];

    const minPrice =
        allProducts.length > 0
            ? Math.min(...allProducts.map((product) => product.price))
            : 0;

    const maxPrice =
        allProducts.length > 0
            ? Math.max(...allProducts.map((product) => product.price))
            : 0;

    const [filters, setFilters] = useState({
        category: "",
        brand: "",
        selectedMinPrice: 0,
        selectedMaxPrice: 0,
    });

    const [showFilters, setShowFilters] = useState(false);

    useEffect(() => {
        if (allProducts.length === 0) return;

        setFilters((prev) => ({
            ...prev,
            selectedMinPrice: minPrice,
            selectedMaxPrice: maxPrice,
        }));
    }, [minPrice, maxPrice, allProducts.length]);

    const [searchTerm, setSearchTerm] = useState("");
    const [sortBy, setSortBy] = useState("default");

    const filteredProducts = allProducts.filter((product) => {
        const matchesSearch = product.name
            .toLowerCase()
            .includes(searchTerm.toLowerCase());

        const matchesCategory =
            !filters.category || product.category === filters.category;

        const matchesBrand =
            !filters.brand || product.brand === filters.brand;

        const matchesPrice =
            product.price >= filters.selectedMinPrice &&
            product.price <= filters.selectedMaxPrice;

        return matchesSearch && matchesCategory && matchesBrand && matchesPrice;
    });

    const sortedProducts = [...filteredProducts];

    switch (sortBy) {
        case "low":
            sortedProducts.sort((a, b) => a.price - b.price);
            break;

        case "high":
            sortedProducts.sort((a, b) => b.price - a.price);
            break;

        case "rating":
            sortedProducts.sort((a, b) => b.rating - a.rating);
            break;

        default:
            break;
    }

    return (
        <section className="max-w-screen-2xl mx-auto px-4 md:px-6 py-6 md:py-10 pb-24 overflow-x-hidden">
            {/* Header */}
            <div className="flex flex-col gap-3 md:flex-row md:justify-between md:items-center">
                <SearchBar
                    value={searchTerm}
                    onChange={(e) => setSearchTerm(e.target.value)}
                />

                <div className="flex items-center gap-3">
                    {/* زرار فتح وقفل الفلاتر على الموبايل فقط */}
                    <button
                        type="button"
                        onClick={() => setShowFilters((prev) => !prev)}
                        className="md:hidden flex-1 px-4 py-2.5 rounded-xl bg-slate-800 border border-cyan-500/40 text-white text-sm font-semibold active:scale-95 transition"
                    >
                        {showFilters ? "Hide Filters ✕" : "Filters ☰"}
                    </button>

                    <div className="flex-1 md:flex-none">
                        <SortDropdown
                            value={sortBy}
                            onChange={(e) => setSortBy(e.target.value)}
                        />
                    </div>
                </div>
            </div>

            {/* Sidebar + Products */}
            <div className="mt-6 md:mt-10 flex flex-col md:flex-row gap-6 md:gap-8">
                <div
                    className={`${
                        showFilters ? "block" : "hidden"
                    } md:block w-full md:w-auto shrink-0`}
                >
                    <FilterSidebar
                        filters={filters}
                        setFilters={setFilters}
                        minPrice={minPrice}
                        maxPrice={maxPrice}
                        categoryOptions={categoryOptions}
                        brandOptions={brandOptions}
                    />
                </div>

                <div className="flex-1 min-w-0">
                    <ProductGrid products={sortedProducts} />
                </div>
            </div>
        </section>
    );
}