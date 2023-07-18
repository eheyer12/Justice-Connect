import React from "react"

function Case({ cases, deleteCase }) {
    return (
        <div className="case">
            <h1>{cases.title}</h1>
            <h2>Summary: {cases.body}</h2>
            <button onClick={() => deleteCase(cases.id)}>Delete Case {cases.id}</button>
        </div>
    )
}

export default Case