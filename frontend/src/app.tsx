// src/App.tsx
import React from 'react';
import { ApolloProvider } from '@apollo/client';
import client from './ApolloClient';
import PaymentForm from './components/PaymentForm';

function App() {
  return (
    <ApolloProvider client={client}>
      <div>
        <h1>Payment Simulator</h1>
        <PaymentForm />
      </div>
    </ApolloProvider>
  );
}

export default App;