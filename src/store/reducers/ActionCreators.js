import axios from 'axios';
import { store } from '../store';
import { usersSlice } from './UsersSlice';
import { chatSlice } from './ChatSlice';
import { preloaderSlice } from './PreloaderSlice';

export const fetchUsers = () => async () => {
  try {
    const urlToUsersFile = './json/users.json';

    const response = await axios.get(urlToUsersFile);
    store.dispatch(usersSlice.actions.usersFetchingSuccess(response.data));
  } catch (e) {
    store.dispatch(usersSlice.actions.usersFetchingFailed(e.message))
  }
};

export const fetchChatData = (userData) => async () => {
  try {
    const urlToUserFile = `./json/${userData}.json`;

    const response = await axios.get(urlToUserFile);
    store.dispatch(chatSlice.actions.chatFetchingSuccess(response.data));
  } catch (e) {
    console.log(e);

    store.dispatch(chatSlice.actions.chatFetchingFailed(e.message))
  }
};

export const preloaderIsDone = () => async () => {
  store.dispatch(preloaderSlice.actions.preloaderIsDone());
}

export const chatIsChanged = () => async () => {
  store.dispatch(preloaderSlice.actions.chatIsChanged());
}

export const setTransition = (className) => async () => {
  store.dispatch(preloaderSlice.actions.setTransition(className))
};

export const resetPreloaderClasses = () => async () => {
  store.dispatch(preloaderSlice.actions.resetPreloaderClasses());
}