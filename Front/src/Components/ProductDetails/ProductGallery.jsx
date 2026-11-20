import { useState } from "react";

export default function ProductGallery({ product }) {

    const images =
        product.images?.length > 0
            ? product.images
            : [product.image];

    const [selectedImage, setSelectedImage] = useState(images[0]);

    return (

        <div className="flex flex-col gap-6">

            {/* Gallery */}

            <div className="flex gap-4">

                {/* Thumbnails */}

                <div className="flex flex-col gap-4">

                    {images.map((image, index) => (

                        <button
                            key={index}
                            type="button"
                            onClick={() => setSelectedImage(image)}
                            className={`
                                w-16
                                h-20

                                rounded-xl

                                overflow-hidden

                                border

                                transition-all
                                duration-300

                                ${
                                    selectedImage === image
                                        ? "border-cyan-400"
                                        : "border-cyan-500/10 hover:border-cyan-400/50"
                                }
                            `}
                        >

                            <img
                                src={image}
                                alt={`${product.name} ${index + 1}`}
                                className="
                                    w-full
                                    h-full
                                    object-cover
                                "
                            />

                        </button>

                    ))}

                </div>


                {/* Main Image */}

                <div
                    className="
                        group
                        relative

                        flex-1

                        min-h-[500px]

                        bg-[#0B1120]

                        rounded-2xl

                        border
                        border-cyan-500/10

                        overflow-hidden

                        flex
                        items-center
                        justify-center
                    "
                >

                    {/* Discount */}

                    {product.discount > 0 && (

                        <span
                            className="
                                absolute
                                top-4
                                right-4
                                z-10

                                px-4
                                py-2

                                rounded-lg

                                bg-pink-500

                                text-white

                                font-bold
                                text-sm
                            "
                        >
                            -{product.discount}%
                        </span>

                    )}


                    {/* Main Image */}

                    <img
                        src={selectedImage}
                        alt={product.name}
                        className="
                            w-full
                            h-full

                            max-h-[600px]

                            object-contain

                            transition-transform
                            duration-500

                            group-hover:scale-105
                        "
                    />

                </div>

            </div>

        </div>

    );
}