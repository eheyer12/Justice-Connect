import { useState } from 'react'

function NewCaseForm({ addCase, updatePostFormData }) {

    const [formSubmitted, setFormSubmitted] = useState(false)

    return (
        <div className="case-form">
            <h2>Create Case Form</h2>
            {formSubmitted ? <h1>Thanks for adding a new case, a lawyer will reach out soon!</h1> :
                <form onSubmit={event => {
                    addCase(event)
                    setFormSubmitted(formSubmitted => !formSubmitted)
                }}>
                    <input onChange={updatePostFormData} type="text" name="title" placeholder="Law Type" required />
                    <input onChange={updatePostFormData} type="text" name="body" placeholder="Summary" required />
                    <button type="submit">Create Case</button>
                </form>}
        </div>
    )
}

export default NewCaseForm