// Dashboard.js
import React, { useState } from 'react';
import axios from 'axios';

function Dashboard() {
  const [formData, setFormData] = useState({
    age: 22,
    gender: 'M',
    location: 'Lagos',
    education: 'University',
    employment: 'Yes',
    voter_registered: 1
  });

  const [result, setResult] = useState(null);

  const handleSubmit = async () => {
    const res = await axios.post('http://your-server.com/predict', formData);
    setResult(res.data);
  };

  return (
    <div className="dashboard">
      <h1>🗳️ PMEVACS: Voter Apathy Checker</h1>
      <p>Find your voting likelihood and get personalized tips.</p>

      <form onSubmit={handleSubmit}>
        <input placeholder="Age" name="age" onChange={(e) => setFormData({...formData, age: e.target.value})} />
        <select name="gender" onChange={(e) => setFormData({...formData, gender: e.target.value})}>
          <option value="M">Male</option>
          <option value="F">Female</option>
        </select>
        {/* Add other fields */}
        <button type="submit">Check My Score</button>
      </form>

      {result && (
        <div className="result">
          <h3>Your Voting Likelihood: {result.voting_likelihood * 100}%</h3>
          <p>🎯 Risk: <strong>{result.apathy_risk}</strong></p>
          <p>💡 Tip: {result.recommendation}</p>
        </div>
      )}

      <GamificationWidget />
    </div>
  );
}

function GamificationWidget() {
  return (
    <div className="gamify">
      <h3>🏆 Your Badges</h3>
      <p>✅ Voter Pledge | 🔘 Quiz Master | 🎯 3 Friends Referred</p>
      <progress value="60" max="100"></progress> 60/100 pts
    </div>
  );
}

export default Dashboard;