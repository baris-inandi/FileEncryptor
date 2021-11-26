const Title: React.FC = (props) => {
    return (
        <h1 className="font-title font-bold text-xl leading-snug">
            {props.children}
        </h1>
    )
}

export default Title
