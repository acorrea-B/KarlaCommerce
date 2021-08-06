const initialState = () => ({
    purchase: {},
    
  })
  
export default {
      state: initialState,
      getters: {
        purchase: state =>{
          return state.purchase
        }
  
      },
      mutations: {
        setpurchase(state, purchase) { 
              state.purchase = purchase
        },
        resetState (state) {
          const initial = initialState()
          Object.keys(initial).forEach(key => { state[key] = initial[key] })
        },
      },
      actions: {},
    }