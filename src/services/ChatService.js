import { createApi, fetchBaseQuery } from '@reduxjs/toolkit/dist/query/react'

export const chatAPI = createApi({
  reducerPath: 'chatAPI',
  baseQuery: fetchBaseQuery({ baseUrl: 'https://63cd060bfba6420d4d67391b.mockapi.io/react_chat' }),
  endpoints: build => ({
    getChatData: build.query({ query: () => '' })
  })
});

export const { useGetChatDataQuery } = chatAPI;