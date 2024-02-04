import React from 'react';
import {GoogleLogin} from 'reaction-google-login' 

function App() {

    const responseGoogle = () => {
        console.log(response)
    }

    const responseError = error => {
        console.log(error)
    }

    return (
        <div>
            <div className='App'>

            </div>
            <div>
                <GoogleLogin clientId="546833222170-bhr1buedvlek62ins1p98rjkk5eo7fvg.apps.googleusercontent.com" buttonText="Sign in & Authorize Calendar" 
                onSucess={responseGoogle}
                onFailure={responseError}
                cookiePolicy={'single_host_origin'}
                // this is important
                responseType='code'
                accessType='offline'
                scope='openid email profile https://www.googleapis.com/auth/calendar'
                />
            </div>

        </div>
    )
}