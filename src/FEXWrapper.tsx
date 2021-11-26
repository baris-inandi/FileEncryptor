import Header from './components/Header'
import './index.css'

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
