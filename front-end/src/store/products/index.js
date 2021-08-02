const initialState = () => ({
    products: [Object, Object],
    
  })
  
export default {
      state: initialState,
      getters: {
        products: state =>{
          return state.products
        }
  
      },
      mutations: {
        setproducts(state, products) { 
              state.products = products
        },
        resetState (state) {
          const initial = initialState()
          Object.keys(initial).forEach(key => { state[key] = initial[key] })
        },
      },
      actions: {},
    }