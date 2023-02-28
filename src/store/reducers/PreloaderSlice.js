import { createSlice } from '@reduxjs/toolkit'

const initialState = {
  preloaderIsVisible: false,
  currentClass: "preloader",
}

export const preloaderSlice = createSlice({
  name: 'preloader',
  initialState,
  reducers: {
    preloaderIsDone(state) {
      state.preloaderIsVisible = false;
      state.currentClass += " preloader_done";
    },

    chatIsChanged(state) {
      state.preloaderIsVisible = true;
    },

    setTransition(state, { payload }) {
      state.currentClass = `preloader ${payload}`;
    },

    resetPreloaderClasses(state) {
      state.currentClass = "preloader";
    }
  }
});

export default preloaderSlice.reducer;