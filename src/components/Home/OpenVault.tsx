import Subtitle from '../public/Subtitle';
import Title from '../public/Title';
import Button from '../public/Button'

const ActionArea: React.FC = (props) => {
    return (
        <div className="flex flex-row w-full items-center justify-between py-3">
            <div className="max-w-1/2">
                <Title>
                    Vault
                </Title>
                <Subtitle>
                    Somewhere safe to keep your encrypted files.
                </Subtitle>
            </div>
            <Button action={() => {}} text="Open Vault" sub />
        </div>
    )
}

export default ActionArea
