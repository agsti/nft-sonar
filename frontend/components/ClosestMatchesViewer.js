import React from 'react'
import MatchItem from './MatchItem.js'

const BestMatchesViewer = ({ matches }) => {
    return (
        <div className="container flex flex-wrap justify-center items-center">
            {matches.map((m, i) => (
                <MatchItem item={m} key={i} />
            ))}
        </div>
    )
}

export default BestMatchesViewer
