import { useState, useEffect  } from "react";

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

        ...[
            ...new Set(
                allProducts.map(product => product.category)
            ),
        ].map(category => ({
            label: category,
            value: category,
        })),
    ];

    const brandOptions = [
        {
            label: "All",
            value: "",
        },

        ...[
            ...new Set(
                allProducts
                    .map(product => product.brand)
                    .filter(Boolean)
            ),
        ].map(brand => ({
            label: brand,
            value: brand,
        })),
    ];

    const minPrice =
        allProducts.length > 0
            ? Math.min(...allProducts.map(product => product.price))
            : 0;

    const maxPrice =
        allProducts.length > 0
            ? Math.max(...allProducts.map(product => product.price))
            : 0;

    
    const [filters, setFilters] = useState({
        category: "",
        brand: "",
        selectedMinPrice: 0,
        selectedMaxPrice: 0,
    })

    useEffect(() => {

        if (allProducts.length === 0) return;

        setFilters(prev => ({
            ...prev,
            selectedMinPrice: minPrice,
            selectedMaxPrice: maxPrice,
        }));

    }, [minPrice, maxPrice]);

    const [searchTerm, setSearchTerm] = useState("");

    const [sortBy, setSortBy] = useState("default");

    const filteredProducts = allProducts.filter((product) => {

        const matchesSearch =
            product.name
                .toLowerCase()
                .includes(searchTerm.toLowerCase());

        const matchesCategory =
            !filters.category ||
            product.category === filters.category;

        const matchesBrand =
            !filters.brand ||
            product.brand === filters.brand;


        const matchesPrice =
            product.price >= filters.selectedMinPrice &&
            product.price <= filters.selectedMaxPrice;

        return (
            matchesSearch &&
            matchesCategory &&
            matchesBrand &&
            matchesPrice
        );
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
        <section className="max-w-screen-2xl mx-auto px-6 py-10">

            {/* Header */}

            <div className="flex flex-col gap-4 md:flex-row md:justify-between">

                <SearchBar
                    value={searchTerm}
                    onChange={(e) => setSearchTerm(e.target.value)}
                />

                <SortDropdown
                    value={sortBy}
                    onChange={(e) => setSortBy(e.target.value)}
                />

            </div>
            {/* SideBar */}


            <div className="mt-10 flex gap-8">

                <FilterSidebar
                    filters={filters}
                    setFilters={setFilters}
                    minPrice={minPrice}
                    maxPrice={maxPrice}
                    categoryOptions={categoryOptions}
                    brandOptions={brandOptions}
                />

                <div className="flex-1">

                    <ProductGrid
                        products={sortedProducts}
                    />

                </div>

            </div>

        </section>
    );
}