import { useState } from 'react'

function UpdateCaseForm({ updateCase, setIdToUpdate, updatePatchFormData, cases }) {

    const [updateFormSubmitted, setUpdateFormSubmitted] = useState(false)

    return (
        <div className="case-form">
            <h2>Update Case Form</h2>
            {updateFormSubmitted ? (
                <h1>Case Updated!</h1>
            ) : (
                <form
                    onSubmit={event => {
                        updateCase(event)
                    }}
                >
                    <label>Choose a Case: </label>
                    <select
                        onChange={(event) => {
                            setIdToUpdate(event.target.value)
                        }}
                        name="id"
                    >
                        {cases.map(caseItem => {
                            return (
                                <option key={caseItem.id} value={caseItem.id}>
                                    {`${caseItem.id}: ${caseItem.title}`}
                                </option>
                            );
                        })}
                    </select>
                    <input
                        onChange= {updatePatchFormData}
                        type="text"
                        name="title"
                        placeholder="Law Type"
                    />
                    <input
                        onChange={updatePatchFormData}
                        type="text"
                        name="body"
                        placeholder="Summary"
                    />
                    <input type="submit" value="Update Case" />
                </form>
            )}
        </div>
    )
}

export default UpdateCaseForm