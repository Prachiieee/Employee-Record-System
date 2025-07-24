import React from "react"
import TextField from '@mui/material/TextField';
import Button from '@mui/material/Button';
import { Link  } from 'react-router-dom';

const Register=()=>{
    return(
       <div>
            <div>Register to your account</div>
            <div style={{marginTop:'20px',marginBottom:'16px'}}>
                <TextField id="outlined-basic" label="Enter Your email" variant="outlined" style={{marginRight:'16px'}}/>
                <TextField id="outlined-basic" label="Enter Your username" variant="outlined" style={{marginRight:'16px'}} />
            </div>
            <div style={{marginBottom:'20px'}}>
                <TextField id="outlined-basic" label="Enter Your password" type="password" variant="outlined" style={{marginRight:'16px'}} />
                <TextField id="outlined-basic" label="Confirm Your password" type="password" variant="outlined" style={{marginRight:'16px'}} />
            </div>
            <Button variant="contained">Register</Button>
            <div style={{marginTop:'16px'}}>
                <small>
                    <Link to="/Login">
                        forgot passsword?
                    </Link>
                </small>
            </div>
        </div>
    )
}
export default Register