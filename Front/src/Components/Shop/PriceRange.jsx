export default function PriceRange({
    minPrice,
    maxPrice,
    filters,
    setFilters,
}) {
    return (
        <div className="mb-8">

            <h3
                className="
                    mb-4
                    text-lg
                    font-semibold
                    text-white
                "
            >
                Price
            </h3>

            <input
                type="range"

                min={minPrice}
                max={maxPrice}

                value={filters.selectedMinPrice}

                onChange={(e) => {

                    const value = Number(e.target.value);

                    if (value <= filters.selectedMaxPrice) {

                        setFilters(prev => ({
                            ...prev,
                            selectedMinPrice: value,
                        }));

                    }

                }}

                className="w-full"
            />

            <input
                type="range"
                min={minPrice}
                max={maxPrice}
                value={filters.selectedMaxPrice}
                onChange={(e) => {

                    const value = Number(e.target.value);

                    if (value >= filters.selectedMinPrice) {

                        setFilters(prev => ({
                            ...prev,
                            selectedMaxPrice: value,
                        }));

                    }

                }}
                className="w-full mt-4"
            />

            <div
                className="
                    mt-3
                    flex
                    justify-between
                    text-sm
                    text-gray-400
                "
            >
                <span>
                    Min: ${filters.selectedMinPrice}
                </span>

                <span>
                    Max: ${filters.selectedMaxPrice}
                </span>
            </div>

        </div>
    );
}