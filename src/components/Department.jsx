import React from "react"
import TextField from '@mui/material/TextField';
import Button from '@mui/material/Button';
import { Link  } from 'react-router-dom';

const Department=()=>{
    return(
       <div>
            <div>Add new Department</div>
            <div style={{marginTop:'20px',marginBottom:'16px'}}>
                <TextField id="outlined-basic" label="Enter Your name of the department" variant="outlined" style={{marginRight:'16px'}}/>
                <TextField id="outlined-basic" label="Department Code" variant="outlined" style={{marginRight:'16px'}} />
                <TextField id="outlined-basic" label="Department head" variant="outlined" style={{marginRight:'16px'}} />
            </div>
            <div style={{marginBottom:'20px'}}>
                <TextField id="outlined-basic" label="Department Description" variant="outlined" style={{marginRight:'16px'}} />
                <TextField id="outlined-basic" label="Enter Your password" type="password" variant="outlined" style={{marginRight:'16px'}} />
                <TextField id="outlined-basic" label="Confirm Your password" type="password" variant="outlined" style={{marginRight:'16px'}} />
            </div>
            <Button variant="contained">Register</Button>
            <div style={{marginTop:'16px'}}>
                <small>
                    <Link to="/CreateRecord">
                        Add New Employee 
                    </Link>
                </small>
            </div>
        </div>
    )
}
export default Department