import gql from 'graphql-tag'

export const NewPurchase = gql`
mutation NewPurchase($total_value: Int!, $costumer: CostumerPurchaseInput!, $products: [ProductPurchase]!) {
    newPurchase(input: {totalValue: $total_value, costumer: $costumer, products: $products}) {
      purchase {
        id
        totalValue
        costumer {
          firstName
        }
      }
      payment {
        tpagaPaymentUrl
        expiresAt
      }
      error {
        status
        message
      }
    }
  }
`
export const Auth = gql`
mutation auth($identification:String!, $password:String!){
    tokenAuth(identification:$identification, password:$password){
      token
    }
  }
`