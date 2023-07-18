import React from 'react'
import Case from './Case'

function CaseList({ cases, deleteCase }) {

    const caseComponents = cases.map(cases => {
        return <Case key={cases.id} cases={cases} title={cases.title} deleteCase={deleteCase} />
    })

    return (
        <ul className="case-list">{caseComponents}</ul>
    )
}

export default CaseList