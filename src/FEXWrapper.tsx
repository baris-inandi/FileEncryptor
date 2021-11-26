import Header from './components/Header/Header'
import './global.sass'

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
