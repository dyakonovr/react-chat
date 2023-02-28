import './App.scss'
import Users from './components/Users/Users';
import Dialog from './components/Dialog/Dialog';
import { useEffect } from 'react';
import { store } from './store/store';
import { fetchUsers } from './store/reducers/ActionCreators';

function App() {
  useEffect(() => {
    store.dispatch(fetchUsers());
  });

  return (
    <div className="App">
      <Users />
      <Dialog />

      {/* {isLoading ? console.log(data) : console.log(error)} */}
    </div>
  )
}

export default App
