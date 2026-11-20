export default function Price({
  price,
  oldPrice,
}) {
  return (
    <div className="flex items-end gap-3">

      {/* Current Price */}

      <span
        className="
        text-2xl
        font-bold
        text-white"
      >
        ${price}
      </span>

      {/* Old Price */}

      {
        oldPrice > price && (

          <span
            className="
            text-sm
            text-gray-500
            line-through"
          >
            ${oldPrice}
          </span>

        )
      }

    </div>
  );
}