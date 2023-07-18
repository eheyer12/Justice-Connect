import React from 'react'
import Lawyer from './Lawyer'

function LawyerList({ lawyers }) {
    console.log(lawyers)
    const lawyerComponents = lawyers.map(lawyer => {
        console.log(lawyer)
        return <Lawyer key={lawyer.id} lawyer={lawyer} title={lawyer.title} />
    })

    return (
        <ul className="lawyer-list">{lawyerComponents}</ul>
    )
}

export default LawyerList