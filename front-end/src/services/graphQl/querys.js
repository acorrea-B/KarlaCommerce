import gql from 'graphql-tag'

export const ListProducts = gql`
query ListProducts{
    listProducts{
      id
      name
      value
      description
      image
    }
  }
`