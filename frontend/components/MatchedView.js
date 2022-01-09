import MatchItem from './MatchItem.js'

const MatchedView = ({ winner }) => {
    return (
        <div className="flex flex-col items-center justify-center ">
            <p className="text-center text-2xl text-whitish">
                Awesome! the image you gave us, it is an NFT!
            </p>
            <MatchItem item={winner} winner={true} />
        </div>
    )
}

export default MatchedView
