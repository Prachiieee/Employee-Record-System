import React from "react"
import TextField from '@mui/material/TextField';
import Button from '@mui/material/Button';
import { Link  } from 'react-router-dom';

const Login=()=>{
    return(
       <div>
            <div>Login to your account</div>
            <div style={{marginTop:'20px'}}>
                <TextField id="outlined-basic" label="Enter Your email" variant="outlined" style={{marginRight:'16px'}} />
                <TextField id="outlined-basic" label="Enter Your password" type="password" variant="outlined" style={{marginRight:'16px'}} />
                <Button variant="contained">Login</Button>
            </div>
            <div style={{marginTop:'16px'}}>
                <small>
                    <Link to="/register">
                        Register Your Account
                    </Link>
                </small>
                <p><small>forgot passsword?</small></p>
            </div>
       </div>
    )
}
export default Login