const initialState = () => ({
    purchases: [Object, Object],
    
  })
  
export default {
      state: initialState,
      getters: {
        purchases: state =>{
          return state.purchases
        }
  
      },
      mutations: {
        setpurchases(state, purchases) { 
              state.purchases = purchases
        },
        resetState (state) {
          const initial = initialState()
          Object.keys(initial).forEach(key => { state[key] = initial[key] })
        },
      },
      actions: {},
    }