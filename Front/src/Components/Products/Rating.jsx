import { Star } from "lucide-react";

export default function Rating({ rating, reviews }) {
  return (
    <div className="flex items-center gap-1">

      <Star
        size={16}
        className="fill-yellow-400 text-yellow-400"
      />

      <span className="text-sm text-gray-300">
        {rating}
      </span>

      <span className="text-xs text-gray-500">
        ({reviews})
      </span>

    </div>
  );
}