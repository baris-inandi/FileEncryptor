interface Props {
    text: string;
    action: () => void;
    sub?: boolean;
}

const Button: React.FC<Props> = (props) => {
    return (
        <button
            onClick={props.action}
            className={
                `
                transition duration-150 rounded-lg text-md font-medium py-2 h-fit-content
                ${!props.sub ? `
                bg-blue-500 text-white
                hover:bg-blue-600 px-8
                ` : `
                text-gray-500
                hover:text-gray-700
                `}
                `
        }
        >
            {props.text}
        </button>
    )
}

export default Button
