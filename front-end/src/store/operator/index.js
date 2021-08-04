const initialState = () => ({
    redirect: "Home",
    identification: "",
    pass:"",
    token:"",
    auth:false,
  })
  
  export default {
      state: initialState,
      getters: {
        identification: state =>{
          return state.identification
        },
        pass: state=> {
            return state.pass
        },token: state=> {
            return state.token
        },auth: state=> {
            return state.auth
        }
  
      },
      mutations: {
        setIdentification(state, identification) { 
              state.identification = identification
        },
        setpass(state, pass) {
            state.pass = pass
        },
        setToken(state, token) {
            state.token = token
        },
        setAuth(state, auth) {
            state.auth = auth
        },
        resetState (state) {
          const initial = initialState()
          Object.keys(initial).forEach(key => { state[key] = initial[key] })
        },
      },
      actions: {},
    }