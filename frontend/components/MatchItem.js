const MatchItem = ({ item }) => {
    return (
        <div className="border-solid w-64 border-slate-600 border-1 p-3 m-6 rounded-md bg-white shadow-lg">
            <div className="w-200">
                <div className="relative">
                    <img
                        className="rounded-md"
                        src={item.asset.url}
                        alt="blabla"
                    />
                    <div className="absolute bottom-0 bg-white rounded-tl-md right-0">
                        {(item.score * 100).toFixed(0)}%
                    </div>
                </div>

                <div className="my-1 text-left font-bold">
                    {item.asset.name}
                </div>
                <div className="text-left ">
                    <a href={item.asset.marketplace_url}>BUY ON OPEN SEA</a>
                </div>
            </div>
        </div>
    )
}

export default MatchItem
