import './App.scss'
import Users from './components/Users/Users';
import Dialog from './components/Dialog/Dialog';
import { Provider } from 'react-redux';
import { store } from './store/store';


function App() {
  return (
    <Provider store={store}>
      <div className="App">
        <Users />
        <Dialog />

        {/* {isLoading ? console.log(data) : console.log(error)} */}
      </div>
    </Provider>
  )
}

export default App
