import FilterSection from "./FilterSection";
import PriceRange from "./PriceRange";

export default function FilterSidebar({
    filters,
    setFilters,
    minPrice,
    maxPrice,
    categoryOptions,
    brandOptions,
}) {
    
    return (
        <aside
            className="
                w-full
                lg:w-64
                rounded-2xl
                bg-[#0B1120]
                p-6
                border
                border-cyan-500/10
            "
        >
            <h2
                className="
                    text-2xl
                    font-bold
                    text-white
                    mb-8
                "
            >
                Filters
            </h2>

            <FilterSection
                title="Category"
                options={categoryOptions}
                selectedValue={filters.category}
                onChange={(value) =>
                    setFilters((prev) => ({
                        ...prev,
                        category: value,
                    }))
                }
            />

            <FilterSection
                title="Brand"
                options={brandOptions}
                selectedValue={filters.brand}
                onChange={(value) =>
                    setFilters((prev) => ({
                        ...prev,
                        brand: value,
                    }))
                }
            />

            <PriceRange
                minPrice={minPrice}
                maxPrice={maxPrice}
                filters={filters}
                setFilters={setFilters}     
            />
        </aside>
    );
}