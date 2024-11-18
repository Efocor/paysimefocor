// src/components/PaymentForm.tsx
import React, { useState } from 'react';
import { useMutation } from '@apollo/client';
import { gql } from 'graphql-tag';

// Definimos la mutación GraphQL para crear un pago
const CREATE_PAYMENT_MUTATION = gql`
  mutation CreatePayment($amount: Float!) {
    createPayment(amount: $amount) {
      id
      amount
      status
    }
  }
`;

const PaymentForm = () => {
  const [amount, setAmount] = useState('');
  const [createPayment, { data, loading, error }] = useMutation(CREATE_PAYMENT_MUTATION);

  const handleSubmit = (e: React.FormEvent) => {
    e.preventDefault();
    createPayment({ variables: { amount: parseFloat(amount) } });
  };

  return (
    <div>
      <form onSubmit={handleSubmit}>
        <label>
          Payment Amount:
          <input
            type="number"
            value={amount}
            onChange={(e) => setAmount(e.target.value)}
            placeholder="Enter amount"
          />
        </label>
        <button type="submit">Submit Payment</button>
      </form>

      {loading && <p>Processing payment...</p>}
      {error && <p>Error: {error.message}</p>}

      {data && (
        <div>
          <h3>Payment Details</h3>
          <p>Payment ID: {data.createPayment.id}</p>
          <p>Amount: ${data.createPayment.amount}</p>
          <p>Status: {data.createPayment.status}</p>
        </div>
      )}
    </div>
  );
};

export default PaymentForm;