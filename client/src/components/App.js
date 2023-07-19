import '../App.css';
import { useState, useEffect } from 'react'
import { Route, Switch } from "react-router-dom"

import NavBar from './NavBar'
import Header from './Header'
import NewCaseForm from './NewCaseForm'
import UpdateCaseForm from './UpdateCaseForm'
import LawfirmList from './LawfirmList.js';
import LawyerList from './LawyerList.js';
import CaseList from './CaseList';
import About from './About.js';
import ImageSlider from './ImageSlider';

function App() {

  const [cases, setCases] = useState([])
  const [lawfirms, setLawfirms] = useState([])
  const [lawyers, setLawyers] = useState([])
  const [postFormData, setPostFormData] = useState({})
  const [idToUpdate, setIdToUpdate] = useState(0)
  const [patchFormData, setPatchFormData] = useState({})

  useEffect(() => {
    fetch('/lawfirms')
      .then(response => response.json())
      .then(lawfirmData => setLawfirms(lawfirmData))
  }, [])

  useEffect(() => {
    fetch('/lawyers')
      .then(response => response.json())
      .then(lawyerData => setLawyers(lawyerData))
  }, [])

  useEffect(() => {
    fetch('/cases')
      .then(response => response.json())
      .then(caseData => setCases(caseData))
  }, [])

  useEffect(() => {
    if (cases.length > 0 && cases[0].id) {
      setIdToUpdate(cases[0].id)
    }
  }, [cases])

  function addCase(event) {
    event.preventDefault()

    fetch('/cases', {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
        "Accept": "application/json"
      },
      body: JSON.stringify(postFormData)
    })
      .then(response => response.json())
      .then(newCase => setCases([...cases, newCase]))
  }

  function updateCase(event) {
    event.preventDefault()

    fetch(`/cases/${idToUpdate}`, {
      method: "PATCH",
      headers: {
        "Content-Type": "application/json",
        "Accept": "application/json"
      },
      body: JSON.stringify(patchFormData)
    })
      .then(response => response.json())
      .then(updatedCase => {
        setCases(cases => {
          return cases.map(caseItem => {
            if (caseItem.id === updatedCase.id) {
              return updatedCase
            }
            else {
              return caseItem
            }
          })
        })
      })
  }

  function deleteCase(id) {
    fetch(`/cases/${id}`, {
      method: "DELETE"
    })
      .then(() => setCases(cases => {
        return cases.filter(cases => {
          return cases.id !== id
        })
      }))
  }

  function deleteLawfirm(id) {
    fetch(`/lawfirms/${id}`, {
      method: "DELETE"
    })
      .then(() => setLawfirms(lawfirms => {
        return lawfirms.filter(lawfirm => {
          return lawfirm.id !== id
        })
      }))
  }

  function updatePostFormData(event) {
    setPostFormData({ ...postFormData, [event.target.name]: event.target.value })
  }

  function updatePatchFormData(event) {
    setPatchFormData({ ...patchFormData, [event.target.name]: event.target.value })
  }

  return (
    <div className="app">
      <Header />
      <NavBar />
      <Switch>
        <Route exact path="/">
          <About />
          <ImageSlider />
        </Route>
        <Route exact path="/lawfirms">
          <h1 className='header'>Lawfirms</h1>
          <LawfirmList lawfirms={lawfirms} deleteLawfirm={deleteLawfirm} />
        </Route>
        <Route exact path="/lawyers">
          <h1 className='header'>Lawyers</h1>
          <LawyerList lawyers={lawyers} />
        </Route>
        <Route exact path="/cases">
          <h1 className='header'>Cases</h1>
          <CaseList cases={cases} deleteCase={deleteCase} />
        </Route>
        <Route path="/add_case">
          <NewCaseForm addCase={addCase} updatePostFormData={updatePostFormData} />
        </Route>
        <Route path="/update_case">
          <UpdateCaseForm updateCase={updateCase} setIdToUpdate={setIdToUpdate} updatePatchFormData={updatePatchFormData} cases={cases} />
        </Route>
      </Switch>
    </div>
  );
}

export default App;
