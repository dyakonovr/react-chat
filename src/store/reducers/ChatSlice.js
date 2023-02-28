import { createSlice } from '@reduxjs/toolkit'

const initialState = {
  data: [],
  isLoading: false,
  error: ''
}

export const chatSlice = createSlice({
  name: 'chat',
  initialState,
  reducers: {
    chatFetchingSuccess(state, action) {
      state.isLoading = true;
      state.data = action.payload;
    },

    chatFetchingFailed(action) {
      state.error = action.payload;
    }
  }
});

export default chatSlice.reducer;