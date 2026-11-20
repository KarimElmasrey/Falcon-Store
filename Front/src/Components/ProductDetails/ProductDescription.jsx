export default function ProductDescription({ product }) {

    return (
        <div
            className="
               mt-6
            "
        >

            <h2
                className="
                    text-2xl
                    font-bold
                    text-white
                "
            >
                Description
            </h2>

            <p
                className="
                    mt-2
                    ml-3
                    leading-8
                    text-gray-300
                "
            >
                {product.description}
            </p>

        </div>
    );
}