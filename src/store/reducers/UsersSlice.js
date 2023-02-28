import { createSlice } from '@reduxjs/toolkit'

const initialState = {
  data: [],
  isLoading: false,
  error: ''
}

export const usersSlice = createSlice({
  name: 'users',
  initialState,
  reducers: {
    usersFetchingSuccess(state, action) {
      state.isLoading = true;
      state.data = action.payload;
    },

    usersFetchingFailed(action) {
      state.error = action.payload;
    }
  }
});

export default usersSlice.reducer;