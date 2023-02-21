import { combineReducers, configureStore, getDefaultMiddleware } from '@reduxjs/toolkit';
import { chatAPI } from '../services/ChatService';

const rootReducer = combineReducers({
  [chatAPI.reducerPath]: chatAPI.reducer
});

export const store = configureStore({
  reducer: rootReducer,
  middleware: (getDefaultMiddleware) => getDefaultMiddleware().concat(chatAPI.middleware),
});