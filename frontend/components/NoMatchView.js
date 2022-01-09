import ClosestMatchesViewer from './ClosestMatchesViewer.js'

const NoMatchView = ({ matches }) => {
    return (
        <div>
            <p className="text-center text-2xl text-whitish">
                Ow! We don't think the image you gave us is an NFT, these are
                the closest matches we found:
            </p>
            <ClosestMatchesViewer matches={matches} />
        </div>
    )
}

export default NoMatchView
