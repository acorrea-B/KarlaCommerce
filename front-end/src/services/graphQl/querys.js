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
export const PurchaseInfo = gql`
query PurchaseInfo($purchase_id:String!){
  purchase(purchaseId:$purchase_id){
    id
    state
    purchaseDate
    purchaseConfirmationDate
    totalValue
    costumer{
      firstName
      lastName
    }
  }
}
`
