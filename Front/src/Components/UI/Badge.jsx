export default function Badge({
    text,
    bgColor = "bg-red-500",
}) {

    return (

        <span
            className={`
                absolute
                top-4
                left-4

                px-3
                py-1

                rounded-full

                text-xs
                font-bold
                text-white

                ${bgColor}
            `}
        >

            {text}

        </span>

    );

}