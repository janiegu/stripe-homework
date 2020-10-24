import React from 'react';
import './App.css';

import {Elements} from '@stripe/react-stripe-js';
import {loadStripe} from '@stripe/stripe-js';

import CheckoutForm from './CheckoutForm';

const stripePromise = loadStripe("pk_test_51HeNvWCnovgGvFVa2aHYWZ1Jp1JO8rYFRbTEdd5CYoGnEANtv3sSmluJfPC0lMb5EtQb5uRNs3RdQnrrfNqPOHO70032TA3fQa");

function App() {
  return (
    <Elements stripe={stripePromise}>
      <CheckoutForm />
    </Elements>
  );
}

export default App;
