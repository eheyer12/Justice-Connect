import React from 'react'
import Lawfirm from './Lawfirm'

function LawfirmList({ lawfirms, deleteLawfirm }) {

    const lawfirmComponents = lawfirms.map(lawfirm => {
        return <Lawfirm key={lawfirm.id} lawfirm={lawfirm} title={lawfirm.title} deleteLawfirm={deleteLawfirm} />
    })

    return (
        <ul className="lawfirm-list">{lawfirmComponents}</ul>
    )
}

export default LawfirmList