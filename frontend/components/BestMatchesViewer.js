import React from "react";
import styles from "./BestMatchesViewer.module.css";

const BestMatchItem = ({item}) =>{
    return <div className={styles.itemCard}>
        <img className={styles.itemImg} src = {item.asset.url} />
        <div className={styles.footer}>
            {item.asset.id}: {item.asset.name}
        </div>
    </div>
}




const BestMatchesViewer = ({bestMatches}) => {
    return (
        <div className={styles.container} >
            {bestMatches.map((m) => <BestMatchItem item={m}/> )}
        </div>
    )
}

export default BestMatchesViewer;
