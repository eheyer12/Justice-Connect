import { NavLink } from "react-router-dom"

function NavBar() {
    return (
        <nav>
            <div>
                <NavLink to="/">Home</NavLink>
                <NavLink to="/lawfirms">Lawfirms</NavLink>
                <NavLink to="/lawyers">Lawyers</NavLink>
                <NavLink to="/cases">Cases</NavLink>
            </div>
            <div>
                <NavLink to="/add_case">Create Case</NavLink>
                <NavLink to="/update_case">Update Case</NavLink>
            </div>
        </nav>
    )
}

export default NavBar;