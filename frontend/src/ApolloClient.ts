// src/ApolloClient.ts
import { ApolloClient, InMemoryCache, HttpLink } from '@apollo/client';

// Crea un enlace HTTP para apuntar a tu servidor GraphQL
const link = new HttpLink({
  uri: 'http://localhost:8000/graphql', // Asegúrate de que esta URL apunte a tu backend
});

const client = new ApolloClient({
  link: link,
  cache: new InMemoryCache(),
});

export default client;
