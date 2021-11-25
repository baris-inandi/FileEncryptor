import Header from './components/Header'

const FEXWrapper: React.FC = (props) => {
    return (
        <>
            <Header />
            <main>
                {props.children}
            </main>
        </>
    )
}

export default FEXWrapper
