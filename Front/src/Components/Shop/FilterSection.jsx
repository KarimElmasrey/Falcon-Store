export default function FilterSection({
    title,
    options,
    selectedValue,
    onChange,
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
                {title}
            </h3>

            <div className="space-y-3">

                {options.map((option) => (

                    <label
                        key={option.value}
                        className="flex
                        items-center
                        gap-3
                        cursor-pointer
                      text-gray-300
                      hover:text-white"
                    >

                        <input
                            type="radio"

                            name={title}

                            value={option.value}

                            checked={selectedValue === option.value}

                            onChange={() => onChange(option.value)}

                            className="accent-cyan-400"
                        />

                        {option.label}

                    </label>

                ))}

            </div>

        </div>
    );
}