const initialState = () => ({
    cart: [Object, Object],
    
  })
  
export default {
      state: initialState,
      getters: {
        cart: state =>{
          return state.cart
        }
  
      },
      mutations: {
        addCartItem(state, item) {
            item.quantity = 1;
            state.cart.push(item);
          },
          updateCartItem(state, updatedItem) {
            state.cart = state.cart.map((cartItem) => {
              if (cartItem.id == updatedItem.id) {
                return updatedItem;
              }
      
              return cartItem;
            });
          },
          removeCartItem(state, item) {
            state.cart = state.cart.filter((cartItem) => {
              return cartItem.id != item.id;
            });
          }
      },
      actions: {},
    }