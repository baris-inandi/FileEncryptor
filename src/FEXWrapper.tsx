import Header from './components/Header'
import FEXThemeProvider from './theme/FEXThemeProvider'

const FEXWrapper: React.FC = (props) => {
    return (
        <FEXThemeProvider>
            <Header />
            <main>
                {props.children}
            </main>
        </FEXThemeProvider>
    )
}

export default FEXWrapper
