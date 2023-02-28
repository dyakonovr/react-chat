import { combineReducers, configureStore } from '@reduxjs/toolkit';
import usersReducer from './reducers/UsersSlice';
import chatReducer from "./reducers/ChatSlice";
import preloaderReducer from "./reducers/PreloaderSlice";

const rootReducer = combineReducers({ usersReducer, chatReducer, preloaderReducer });

export const store = configureStore({
  reducer: rootReducer,
});