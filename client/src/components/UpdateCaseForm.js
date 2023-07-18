import { useState } from 'react'

function UpdateCaseForm({ updateCase, setIdToUpdate, updatePatchFormData, cases }) {

    const [updateFormSubmitted, setUpdateFormSubmitted] = useState(false)

    return (
        <div className="case-form">
            <h2>Update Case Form</h2>
            {updateFormSubmitted ? <h1>Case Updated!</h1> :
                <form onSubmit={event => {
                    updateCase(event)
                    setUpdateFormSubmitted(updateFormSubmitted => !updateFormSubmitted)
                }}>
                    <label>Choose a Case: </label>
                    <select onChange={(event) => {
                        setIdToUpdate(event.target.value)
                    }} name="id">
                        {cases.map(cases => {
                            return <option key={cases.id} value={cases.id}>{`${cases.id}: ${cases.title}`}</option>
                        })}
                    </select>
                    <input onChange={updatePatchFormData} type="text" name="name" placeholder="Law Type" />
                    <input onChange={updatePatchFormData} type="text" name="summary" placeholder="Summary" />
                    <input type="submit" value="Update Case" />
                </form>}
        </div>
    )
}

export default UpdateCaseForm