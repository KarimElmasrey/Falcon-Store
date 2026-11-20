export default function SortDropdown({
    value,
    onChange,
}) {
    return (
        <select
            value={value}
            onChange={onChange}
            className="
                rounded-xl

                bg-[#0B1120]

                border
                border-cyan-500/10

                px-4
                py-3

                text-white

                outline-none
            "
        >
            <option value="default">
                Default
            </option>

            <option value="low">
                Price: Low → High
            </option>

            <option value="high">
                Price: High → Low
            </option>

            <option value="rating">
                Rating
            </option>
        </select>
    );
}