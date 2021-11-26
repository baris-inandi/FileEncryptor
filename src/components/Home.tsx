import ActionArea from "./Home/ActionArea"
import OpenVault from './Home/OpenVault'

const Home: React.FC = () => {
    return (
        <div className="flex flex-col items-center justify-center w-full h-full">
            <ActionArea action={()=>{}} title="Encrypt" sub="Password protect your files" />
            <ActionArea action={()=>{}} title="Decrypt" sub="Password protect your files" />
            <div className="w-full border-b-2 border-gray-200 my-4"></div>
            <OpenVault />
        </div>
    )
}

export default Home
