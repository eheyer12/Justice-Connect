import React from "react"

function Lawfirm({ lawfirm, deleteLawfirm }) {
    return (
        <div className="lawfirm">
            <h1>{lawfirm.title}</h1>
            <h2>rank: {lawfirm.rank}</h2>
            <button onClick={() => deleteLawfirm(lawfirm.id)}>Delete Lawfirm {lawfirm.id}</button>
        </div>
    )
}

export default Lawfirm