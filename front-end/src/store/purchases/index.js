const initialState = () => ({
    purchase: {},
    purchases:[],
  })
  
export default {
      state: initialState,
      getters: {
        purchase: state =>{
          return state.purchase
        },
        purchases: state =>{
          return state.purchases
        }
  
      },
      mutations: {
        setpurchase(state, purchase) { 
              state.purchase = purchase
        },
        setPurchases(state, purchases) { 
              state.purchases = purchases
        },
        resetState (state) {
          const initial = initialState()
          Object.keys(initial).forEach(key => { state[key] = initial[key] })
        },
      },
      actions: {},
    }