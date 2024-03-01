import React, { useState } from 'react';
import axios from 'axios';
import { useNavigate } from 'react-router-dom';


const LoginPage = () => {
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');
  const navigate = useNavigate(); 

  const handleLogin = async (e) => {
    e.preventDefault(); 
    try {
      const response = await axios.post('http://127.0.0.1:8000/prototyping/api/login/', {
        email,
        password,
      });
      const token = response.data.token;
      localStorage.setItem('token', token); 
      console.log('Login successful', token);
      navigate('/home'); 
    } catch (error) {
      console.error('Login failed', error.response);
    }
  };

  return (
    <div className="app" id="app">
      <div className="center-block w-xxl w-auto-xs p-y-md">
        <div className="navbar">
          <div className="pull-center">
          </div>
        </div>
        <div className="p-a-md box-color r box-shadow-z1 text-color m-a">
          <div className="m-b text-sm">
            Sign in with your Flatkit Account
          </div>
          <form name="form" onSubmit={handleLogin}>
            <div className="md-form-group float-label">
              <input type="email" className="md-input" required value={email} onChange={(e) => setEmail(e.target.value)} />
              <label>Email</label>
            </div>
            <div className="md-form-group float-label">
              <input type="password" className="md-input" required value={password} onChange={(e) => setPassword(e.target.value)} />
              <label>Password</label>
            </div>      
            <div className="m-b-md">        
              <label className="md-check">
                <input type="checkbox" /><i className="primary"></i> Keep me signed in
              </label>
            </div>
            <button type="submit" className="btn primary btn-block p-x-md">Sign in</button>
          </form>
        </div>
        <div className="p-v-lg text-center">
          <div className="m-b"><a href="forgot-password.html" className="text-primary _600">Forgot password?</a></div>
        </div>
      </div>
    </div>
  );
}

export default LoginPage;
