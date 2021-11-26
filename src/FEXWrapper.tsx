import Header from './components/Header'
import './index.css'

const FEXWrapper: React.FC = (props) => {
    return (
        <div className="w-screen h-screen flex items-center justify-center select-none">
            <div style={{
                height: '100%',
                width: '100%',
                maxHeight: '420px',
                maxWidth: '500px'
            }} className="border-2 border-gray-200 flex flex-col">
                <Header />
                <main className="h-full px-10">
                    {props.children}
                </main>
                <footer className="text-xs text-gray-400 px-2 py-1 bg-gray-200">
                    FileEncryptor v0.0.1-beta
                </footer>
            </div>
        </div>
    )
}

export default FEXWrapper
