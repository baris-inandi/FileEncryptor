import Subtitle from '../public/Subtitle';
import Title from '../public/Title';
import Button from '../public/Button'

interface Props {
    title: string;
    sub: string;
    action: () => void;
}

const ActionArea: React.FC<Props> = (props) => {
    return (
        <div className="flex flex-row w-full justify-between items-center my-3">
            <div className="max-w-2/3">
                <Title>
                    {props.title}
                </Title>
                <Subtitle>
                    {props.sub}
                </Subtitle>
            </div>
            <Button text={props.title} action={props.action}></Button>
        </div>
    )
}

export default ActionArea
