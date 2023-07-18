import React from "react"

function Lawyer({ lawyer }) {
    return (
        <div className="lawyer">
            <h1>{lawyer.title}</h1>
            <h2>Lawfirm: {lawyer.lawfirm_id}</h2>
        </div>
    )
}

export default Lawyer